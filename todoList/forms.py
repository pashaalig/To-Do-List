from django.forms import ModelForm
from todoList.models import Task

class todoform(ModelForm):
    class Meta:
        model= Task
        fields = ['title','status','priority']