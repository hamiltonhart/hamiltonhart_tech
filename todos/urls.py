from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoListListView.as_view(), name='todo_list_list'),
]