"""
URL configuration for myclone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from meta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meta.appurl')),
    path('', include('loginapp.appurl2')),
    path('blog/', views.blog, name='blog'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('base/', views.base, name='base'),
    path('addPost/', views.addPost, name='addPost'),
    path('category/', views.CategoryView, name= 'CategoryView'),
    path('teammember/', views.TeamMember.as_view(), name='teammember'),
    path('admintable/', views.admintable, name='admintable'),
    path('form/', views.Form.as_view(), name='form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
