from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import student
from django.db.models import Q
from .forms import studentForm 
from django.contrib import messages
# Create your views here.

class SearchResultsView(ListView):
    model = student
    template_name = 'search_results.html'
    
    def get_queryset(self):
        if  self.request.method == 'GET':
            query = self.request.GET.get('q')
            if query==None:
                return student.objects
            else:
                object_list = student.objects.filter(
                Q(name__icontains=query) | Q(standard__icontains=query)  
                )
            return object_list
        return student.objects

def HomePageView(request): 
    if request.method == 'POST':
        fm = studentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sd = fm.cleaned_data['standard']
            reg = student(name=nm, standard=sd)
            reg.save()
            messages.info(request, "Student Added") 
    else:
        fm = studentForm()
    
    return render(request,'home.html',{'form':fm})

def remove(request, item_id): 
    item = student.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "Student removed !!!") 
    return redirect('home') 

def update(request, item_id):
    if request.method == 'GET':
        query = request.GET.get('q')
        obj = get_object_or_404(student, id=item_id)
        obj.standard = query
        obj.save(update_fields=["standard"])
        messages.info(request, "Updated !!!") 
    return redirect('home') 