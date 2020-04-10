from django.shortcuts import render

def home(request):
    title = "Welcome"
    template = "Home.html"

    return render(request,template,{'title':title})