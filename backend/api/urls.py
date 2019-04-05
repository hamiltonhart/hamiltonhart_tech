from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'api'

router = SimpleRouter()
router.register('users', views.UserViewSet, base_name='users')
router.register('posts', views.PostViewSet, base_name='posts')
router.register(
    'todo_lists', 
    views.TodoListViewSet, 
    base_name='todo_lists')
router.register(
    'todo_items', 
    views.TodoItemViewSet,
    base_name='todo_items')

urlpatterns = router.urls
