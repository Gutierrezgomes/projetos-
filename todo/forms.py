from django import forms 
from .models import Task

class taskform(forms.ModelForm):
    title = forms.CharField(widget =forms.TextInput(attrs={"class": ".myipute", "placeholder":"enter todo app" })), 
    class Meta:
        model = Task
        fields = ["title"]
