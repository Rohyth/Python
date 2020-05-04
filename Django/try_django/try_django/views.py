from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "Home"
    myl = [1,2,3,5,6]
    return render(request,"Home.html",{'title':title,'myl':myl})
    

def about_page(request):
    title = "About"
    return render(request,"About.html",{'title':title})

def contact_page(request):
    title = "Contact"
    return render(request,"Contact.html",{'title':title})