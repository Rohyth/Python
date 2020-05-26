from django.contrib import admin
from MyApp import views
from django.urls import path, include

urlpatterns = [
    path('', include('MyApp.urls')),
    path('admin/', admin.site.urls),

]
