from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/Home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'Blog/About.html', context)
