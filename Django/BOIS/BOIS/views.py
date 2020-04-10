from django.shortcuts import render

def home(request):
    title = "Welcome"
    template = "Base.html"

    return render(request,template,{'title':title})