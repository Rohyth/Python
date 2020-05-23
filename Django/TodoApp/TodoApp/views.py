from django.shortcuts import render
from django.utils import timezone
from lister.models import Todo
from django.http import HttpResponseRedirect

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html',{'todo_items':todo_items})

def add_todo(request):
    #print(request.POST)
    current_date = timezone.now()
    content = request.POST['content'] 
    #print(added_date,content)
    #sending data to database
    created_obj = Todo.objects.create(added_date=current_date,text=content)


    return HttpResponseRedirect("/")


def delete_todo(request,id):
    #print(id)
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect("/")