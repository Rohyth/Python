from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"Home.html")
    

def about_page(request):
    return HttpResponse("<h1> Rohyth is Awesome </h1>")

def contact_page(request):
    return HttpResponse("<h1> Rohyth is Smart </h1>")