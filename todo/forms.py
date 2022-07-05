from .models import todolist
from django import forms
class todolistform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['title','description']
