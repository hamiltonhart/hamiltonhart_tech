from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post
from todos.models import TodoList, TodoItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'title', 
            'author', 
            'body_text', 
            'date',
            )


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = (
            'id',
            'name',
            'date',
            'description',
            'todo_items',
        )


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = (
            'id',
            'todo_list',
            'item_name',
            'item_detail',
            'assigned_date',
            'complete',
            'complete_date',
            'edit_date',
        )

