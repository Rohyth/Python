from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def home_page(request):
    title = "Home"
    
    return render(request,"Home.html",{'title':title})
    

def about_page(request):
    title = "About"
    return render(request,"About.html",{'title':title})

def contact_page(request):
    title = "Contact"
    return render(request,"Contact.html",{'title':title})