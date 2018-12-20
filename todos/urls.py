from django.urls import path
from . import views

urlpatterns = [
    path('list/', 
        views.TodoListListView.as_view(), 
        name='todo_list_list'),
    path('<int:pk>/', 
        views.TodoListDetailView.as_view(), 
        name='todo_list_detail'),
    path('list/new/', 
        views.TodoListCreateView.as_view(), 
        name='todo_list_new'),
    path('item/new', 
        views.TodoItemCreateView.as_view(), 
        name='todo_item_new'),
    path('list/<int:pk>/update/', 
        views.TodoListUpdateView.as_view(), 
        name='todo_list_update'),
    path('item/<int:pk>/update/', 
        views.TodoItemUpdateView.as_view(), 
        name='todo_item_update'),
    path('list/<int:pk>/delete',
        views.TodoListDeleteView.as_view(),
        name='todo_list_delete'),
    path('items/<int:pk>/', 
        views.TodoItemDetail.as_view(), 
        name='todo_item_detail'),
    path('items/<int:pk>/complete/home',
        views.todo_item_complete_home, 
        name='todo_item_complete_home'),
    path('items/<int:pk>/complete/list',
        views.todo_item_complete_list, 
        name='todo_item_complete_list'),
    path('items/<int:pk>/not_complete', 
        views.todo_item_not_complete, 
        name='todo_item_not_complete')
    
]