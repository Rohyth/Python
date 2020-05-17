from django.shortcuts import render,get_object_or_404
from .models import BlogPost

from .forms import BlogPostModelForm
#Get --> Single Object
#filter -- > Multiple Objecs

#CRUD

#CREATE
#RETRIEVE
#UPDATE
#DELETE


def blog_list(request):

    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list':qs}
    return render(request,template_name,context)

def blog_create(request):
    #Using Forms
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        #obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title") + "0"
        obj.save()
        
        form = BlogPostModelForm()

    template_name = 'form.html'
    context = {'form':form}
    return render(request,template_name,context)

#def blog_retrieve(request,slug):
def blog_detail(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = 'blog/details.html'  
    return render(request,template_name,context)

def blog_update(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj,'form':None}
    template_name = 'blog/update.html'  
    return render(request,template_name,context)

def blog_delete(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = 'blog/delete.html'  
    return render(request,template_name,context)

