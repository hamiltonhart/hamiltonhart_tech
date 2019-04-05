from django.urls import path
from rest_framework.routers import SimpleRouter
from . import apiviews

app_name = 'blog'

router = SimpleRouter()
router.register('users', apiviews.UserViewSet, base_name='users')
router.register('posts', apiviews.PostViewSet, base_name='posts')

urlpatterns = router.urls


# urlpatterns = [
#     path('list/', apiviews.PostListView.as_view()),
#     path('<int:pk>/', apiviews.DetailPostView.as_view()),
#     path('users/', apiviews.UserList.as_view()),
#     path('users/<int:pk>/', apiviews.UserDetail.as_view()),
# ]

# urlpatterns = [
#     path('post/all/', views.PostListView.as_view(), name='post_list'),
#     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
#     path('post/new/', views.PostCreateView.as_view(), name='post_new'),
#     path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
#     path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
# ]
