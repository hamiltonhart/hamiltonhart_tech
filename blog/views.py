from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body_text']


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'author', 'body_text']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'