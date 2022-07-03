from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    success_url ="/task/list/"

    def form_valid(self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)

class TasksList(LoginRequiredMixin,ListView):
    context_object_name = 'tasks' 
    def get_queryset(self) :
        tasks = Task.objects.filter(user=self.request.user)
        return tasks


class ChangeToDone(LoginRequiredMixin,View):
    """
    change a status of task to done
    """
    
    def get (self,request,pk):
        task = Task.objects.get(pk=pk)
        task.done = True
        task.save()
        return HttpResponseRedirect("/task/list/")

class UpdateTask(LoginRequiredMixin,UpdateView):
    """ this class use task_form template same create class for edit a task"""
    model = Task
    form_class = TaskForm
    success_url = "/task/list/"

class DeleteTAsk(LoginRequiredMixin,DeleteView):
    """delete a task this class use task_confirm_delete template"""
    model =Task
    success_url = "/task/list/"