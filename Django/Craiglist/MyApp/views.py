from django.shortcuts import render,redirect


def home(request):
    return render(request,'Base.html')


def new_search(request):
    search = request.POST.get('search')
    print(search)
    return render(request,'index.html')