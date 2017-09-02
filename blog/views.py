from django.shortcuts import render, HttpResponse
from .models import Post


def blog(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'blog/list.html', context)
