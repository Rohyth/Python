
from django.contrib import admin
from django.urls import path

from .views import home,index

urlpatterns = [
    path('',home,name='home'),
    path('index/',index,name='Index'),
    path('admin/', admin.site.urls),
]
