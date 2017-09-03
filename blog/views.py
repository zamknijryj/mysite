from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    template_name = 'blog/list.html'

    def get_queryset(self):
        return Post.objects.filter(status='publish')


class PostDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
