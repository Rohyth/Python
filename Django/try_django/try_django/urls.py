
from django.contrib import admin
from django.urls import path
from blog.views import (
    blog_post_details_page,
)

from .views import (
    home_page,
    about_page,
    contact_page,
)
urlpatterns = [
    
    path('',home_page),
    path('about/',about_page),
    path('contact/',contact_page),
    path('details/<str:slug>/',blog_post_details_page),
    path('admin/', admin.site.urls),

]   
