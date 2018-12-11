from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models

# ToDo List

class TodoListListView(ListView):
    model = models.TodoList
    template_name = "todos/todo_list_list.html"
    context_object_name = "todo_list"
    

class TodoListDetailView(DetailView):
    model = models.TodoList
    template_name = "todos/todo_list_detail.html"
    context_object_name = "todo_list"

class TodoListCreateView(CreateView):
    model = models.TodoList
    template_name = 'todos/todo_list_new.html'
    fields = ['name', 'description']

class TodoListUpdateView(CreateView):
    model = models.TodoList
    template_name = 'todos/todo_list_update.html'
    fields = ['name', 'description']

class TodoListDeleteView(DeleteView):
    model = models.TodoList
    template_name = 'todos/todo_list_delete.html'
    success_url = reverse_lazy('todo_list_list')
    context_object_name = 'todo_list'

# ToDo Items

class TodoItemCreateView(CreateView):
    model = models.TodoItem
    template_name = 'todos/todo_item_new.html'
    fields = ['todo_list', 'item_name']


class TodoItemUpdateView(CreateView):
    model = models.TodoItem
    template_name = 'todos/todo_item_update.html'
    fields = ['todo_list', 'item_name']