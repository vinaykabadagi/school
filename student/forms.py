from django import forms 

from .models import student
class studentForm(forms.ModelForm): 
    class Meta: 
        model = student 
        fields = ['name','standard']
        name = forms.CharField()
        standard=forms.IntegerField(min_value=1,max_value=12)