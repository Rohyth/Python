
from django.contrib import admin
from django.urls import path

from .views import home,index,country

urlpatterns = [
    path('',home,name='home'),
    path('index/',index,name='Index'),
    path('country/',country,name='Country'),
    path('admin/', admin.site.urls),
]
