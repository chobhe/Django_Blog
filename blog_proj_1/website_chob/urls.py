"""website_chob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .settings import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include

from pages.views import home_view
from pages.views import contact_view
#from blog.views import blog_view
from pages.views import index
from pages.views import create
from pages.views import view
from pages.views import article

from pages.views import projects

from user_registration.views import register

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name='home'),
    #path('blog/', blog_view), #when we go to url/blog/ we then get this page
    path('contact/', contact_view),
    path('admin/', admin.site.urls), #this is the admin page that we do our stuff on
    path('<int:id>', index, name = 'blogs'),
    path('create/', create, name = 'create_blog'),
    path('projects/', projects, name = 'projects_area'),
    path('view', view, name = 'different_blog_storages'),
    path('b'+'<int:id>', article, name = 'article'),
    path('register/', register, name = 'register'),
    path('', include('django.contrib.auth.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
