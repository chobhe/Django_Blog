from django.db import models
import PIL
from django.contrib.auth.models import User
# Create your models here.


class Blog_storage(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_storage', null = True)
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class Blog(models.Model):
    blog_storage = models.ForeignKey(Blog_storage, on_delete = models.CASCADE)     #creates a blog_set in Blog_storage where you add all your blogs
    #inherit from default Django Class of model
    title = models.CharField(max_length = 100) #max_length is a mandatory parameter
    author = models.CharField(max_length = 50)
    date = models.DateField(auto_now=False, auto_now_add=True) #look for fields that we want in django field documentation
    preview = models.TextField(default = 'qewrhakdjflzvxyiuoasdf')
    entry = models.TextField()
    im = models.ImageField(upload_to= 'images/', height_field=None, width_field=None, max_length=100, null = True, blank = True)
    read = models.BooleanField(default = False) # we can say null= True or default = True


    def __str__(self):
        return self.title
