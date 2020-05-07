from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    #print('Rohyth Says',request.method, request.path,request.user)
    title = "Home"
    myl = [1,2,3,5,6]
    return render(request,"Home.html",{'title':title,'myl':myl})
    

def about_page(request):
    title = "About"
    return render(request,"About.html",{'title':title})

def contact_page(request):
    title = "Contact"
    #print(request.POST)
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        print(form.cleaned_data)
    
    return render(request,"form.html",{'title':title})