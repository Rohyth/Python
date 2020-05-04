from django.shortcuts import render,get_object_or_404
from .models import BlogPost

#Get --> Single Object
#filter -- > Multiple Objecs

#CRUD

#CREATE
#RETRIEVE
#UPDATE
#DELETE


def blog_list(request):

    qs = BlogPost.objects.all()
    template_name = 'blog_list.html'
    context = {'object_list':qs}
    return render(request,template_name,context)

def blog_create(request):
    #Using Forms
    template_name = 'blog_create.html'
    context = {'form':''}
    return render(request,template_name,context)

#def blog_retrieve(request,slug):
def blog_detail(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = 'blog_post_details.html'  
    return render(request,template_name,context)

def blog_update(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj,'form':None}
    template_name = 'blog_post_update.html'  
    return render(request,template_name,context)

def blog_delete(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = 'blog_post_delete.html'  
    return render(request,template_name,context)

