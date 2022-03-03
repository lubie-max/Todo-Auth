from re import template
from django.shortcuts import render

from django.views.generic.list import ListView

from . models import *
# Create your views here.


# def home(request):

#     return render(request , 'home.html')


class TaskList(ListView):
    model= Task
    template_name= 'home.html'
    # context_object_name= 'tasks'