# from django.contrib.auth import get_user_model
# from rest_framework import viewsets
# from .permissions import IsAuthorOrReadyOnly

# from . import models
# from . import serializers


# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthorOrReadyOnly,)
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = serializers.UserSerializer


# # class PostCreateView(LoginRequiredMixin, CreateView):
# #     model = models.Post
# #     template_name = 'blog/post_new.html'
# #     fields = ['title', 'author', 'body_text']


# # class PostUpdateView(LoginRequiredMixin, UpdateView):
# #     model = models.Post
# #     template_name = 'blog/post_update.html'
# #     fields = ['title', 'author', 'body_text']


# # class PostDeleteView(LoginRequiredMixin, DeleteView):
# #     model = models.Post
# #     template_name = 'blog/post_delete.html'
# #     success_url = reverse_lazy('post_list')
# #     context_object_name = 'post'

# # class PostListView(generics.ListCreateAPIView):
# #     queryset = models.Post.objects.all()
# #     serializer_class = serializers.PostSerializer

# # class DetailPostView(generics.RetrieveUpdateDestroyAPIView):
# #     permission_classes = (IsAuthorOrReadyOnly,)
# #     queryset = models.Post.objects.all()
# #     serializer_class = serializers.PostSerializer

# # class UserList(generics.ListCreateAPIView):
# #     queryset = get_user_model().objects.all()
# #     serializer_class = serializers.UserSerializer

# # class UserDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = get_user_model().objects.all()
# #     serializer_class = serializers.UserSerializer