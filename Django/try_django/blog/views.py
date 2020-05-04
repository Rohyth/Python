from django.shortcuts import render,get_object_or_404
from .models import BlogPost

#Get --> Single Object
#filter -- > Multiple Objecs

def blog_post_details_page(request,slug):
    #obj = BlogPost.objects.get(id=id)
    obj = BlogPost.objects.filter(slug='')
    #obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog_post_details.html'
    context = {"object":obj}
    return render(request,template_name,context)