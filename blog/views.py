from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'

