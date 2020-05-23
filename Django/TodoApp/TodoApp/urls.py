
from django.contrib import admin
from django.urls import path

from TodoApp import views

urlpatterns = [
    path('',views.home),
    path('add_todo/',views.add_todo),
    path('delete_todo/<int:id>/',views.delete_todo),
    path('admin/', admin.site.urls),
]
