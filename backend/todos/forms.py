from django import forms

from . import models


class TodoForm(forms.ModelForm):
    class Meta:
        model = models.TodoList
        fields = ['name', 'description']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['todo_list', 'item_name', 'item_detail']