from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from . import models

# ToDo List

class TodoListListView(LoginRequiredMixin, ListView):
    model = models.TodoList
    template_name = "todos/todo_list_list.html"
    context_object_name = "todo_list"
    

class TodoListDetailView(LoginRequiredMixin, DetailView):
    model = models.TodoList
    template_name = "todos/todo_list_detail.html"
    context_object_name = "todo_list"

class TodoListCreateView(LoginRequiredMixin, CreateView):
    model = models.TodoList
    template_name = 'todos/todo_list_new.html'
    fields = ['name', 'description']

class TodoListUpdateView(LoginRequiredMixin, CreateView):
    model = models.TodoList
    template_name = 'todos/todo_list_update.html'
    fields = ['name', 'description']

class TodoListDeleteView(LoginRequiredMixin, DeleteView):
    model = models.TodoList
    template_name = 'todos/todo_list_delete.html'
    success_url = reverse_lazy('todo_list_list')
    context_object_name = 'todo_list'

# ToDo Items

class TodoItemCreateView(LoginRequiredMixin, CreateView):
    model = models.TodoItem
    template_name = 'todos/todo_item_new.html'
    fields = ['todo_list', 'item_name', 'item_detail']


class TodoItemUpdateView(LoginRequiredMixin, CreateView):
    model = models.TodoItem
    template_name = 'todos/todo_item_update.html'
    fields = ['todo_list', 'item_name']

class TodoItemDetail(LoginRequiredMixin, DetailView):
    model = models.TodoItem
    template_name = 'todos/todo_item_detail.html'
    context_object_name = 'todo_item'


@login_required
def todo_item_complete_list(request, pk):
    todo_item = get_object_or_404(models.TodoItem, pk=pk)
    todo_list_pk = todo_item.todo_list.pk
    todo_item.mark_completed()
    
    return redirect('todo_list_detail', pk=todo_list_pk)

@login_required
def todo_item_complete_home(request, pk):
    todo_item = get_object_or_404(models.TodoItem, pk=pk)
    todo_list_pk = todo_item.todo_list.pk
    todo_item.mark_completed()
    
    return redirect('home')
    
