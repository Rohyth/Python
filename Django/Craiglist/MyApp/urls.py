from django.urls import path
from .views import home,new_search


urlpatterns = [
    path('',home),
    path('new_search/',new_search),
]
