from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "Home"
    return render(request,"Home.html",{'title':title})
    

def about_page(request):
    title = "About"
    return HttpResponse("<h1> Rohyth is Awesome </h1>")

def contact_page(request):
    title = "Contact"
    return HttpResponse("<h1> Rohyth is Smart </h1>")