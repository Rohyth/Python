from django.db import models

# Create your models here.

class BlogPost(models.Model):
    
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,null=False)
    content = models.TextField(null=True,blank=True)

