
from re import template
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
 
from django.contrib.auth.views  import LoginView

from . models import *
# Create your views here.


# def home(request):

#     return render(request , 'home.html')


class CostomLogin(LoginView):
    fields = '__all__'
    redirect_authenticated_user= True
    template_name= 'login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')






class TaskList(LoginRequiredMixin ,ListView):
    model= Task
    template_name= 'home.html'
    context_object_name= 'tasks'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)
        return context



class TaskDetail(LoginRequiredMixin,DetailView):
    model= Task
    template_name= 'detail.html'
    context_object_name= 'item'


class CreateTask(LoginRequiredMixin,CreateView):
    model= Task
    fields= ['title','description','is_completed']
    template_name= 'create.html'
    # context_object_name= 'tasks'
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super(CreateTask, self).form_valid(form)
        


class UpdateTask(LoginRequiredMixin,UpdateView):
    model= Task
    fields= '__all__'
    template_name= 'update.html'
    success_url= reverse_lazy('home')
    context_object_name= 'task'

class DeleteTask(LoginRequiredMixin,DeleteView):
    model= Task
    # fields= '__all__'
    template_name= 'delete.html'
    success_url= reverse_lazy('home')
    context_object_name= 'task'
