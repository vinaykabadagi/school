from django import forms 

from .models import student
class studentForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = student 
        fields = ['name','standard']
        name = forms.CharField()
        standard=forms.IntegerField()