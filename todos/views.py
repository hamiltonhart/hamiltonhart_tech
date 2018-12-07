from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models

class TodoListListView(ListView):
    model = models.TodoList
    template_name = "todos/todo_list_list.html"
    context_object_name = "todo_list"
    
class TodoListDetailView(DetailView):
    model = models.TodoList
    template_name = "todos/todo_list_detail.html"
    context_object_name = "todo_list"

