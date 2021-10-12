from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from base.models import Task

# Create your views here.

#View that lists all tasks
class TasksList(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'task_create_form.html'
    success_url = reverse_lazy('tasks')
    fields = ['title', 'description']


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')



class TaskDelete(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks')






