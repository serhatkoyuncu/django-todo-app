from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title"]
        
class TodoUpdate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","completed"]