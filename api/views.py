from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .permissions import IsAuthorOrReadyOnly

from blog.models import Post
from todos.models import TodoList, TodoItem
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadyOnly,)
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer
