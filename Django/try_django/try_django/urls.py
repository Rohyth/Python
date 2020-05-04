
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    blog_create,
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

    path('details-new/',blog_create),
    path('details/', include('blog.urls')),

    path('admin/', admin.site.urls),

]   
