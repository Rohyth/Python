from django.urls import path
from .views import (
    #blog_create,
    blog_detail,
    blog_list,
    blog_update,
    blog_delete,
)

urlpatterns = [
    
    path('',blog_list),
    #path('details-new/',blog_create),
    path('<str:slug>/',blog_detail),
    path('<str:slug>/edit/',blog_update),
    path('<str:slug>/delete/',blog_delete),

]   
