from django.shortcuts import render

def home(request):
    title = "Welcome"
    template = "Home.html"

    return render(request,template,{'title':title})

def index(request):
    title = "Index"
    template = "index.html"

    return render(request,template,{'title':title})

def country(request):
    title = "country"
    template = "Country.html"

    return render(request,template,{'title':title})