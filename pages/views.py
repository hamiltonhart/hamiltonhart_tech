from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from todos.models import TodoList, TodoItem

class HomePageList(ListView):
    context_object_name = "home_list"
    template_name = "pages/index.html"
    queryset = TodoItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['todos'] = TodoList.objects.all()
        return context

