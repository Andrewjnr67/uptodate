from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('blog/', views.blog, name= 'blog'),
    path('singleblog/<slug:slug>', views.singleblog, name= 'singleblog'),
    path('base/', views.base, name= 'base'),
    path('addPost/', views.addPost, name= 'addpost'),
    path('room/', views.room, name= 'room'),
    path('AddCategoryView/', views.AddCategoryView.as_view(), name= 'addcate'),
    path('teammember/', views.TeamMember.as_view(), name= 'teammember'),
    path('admintable/', views.admintable, name= 'admintable'),
    path('CategoryView/<str:cate>', views.CategoryView, name= 'category'),
    path('form/', views.Form.as_view(), name= 'form'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('fashion/', views.fashion, name= 'fashion'),
    path('deleteProject/<str:pk>', views.deleteProject, name= 'deleteProject'),
    path('updateProject/<str:pk>', views.updateProject, name= 'updateProject'),
    path('SearchView/', views.SearchView, name= 'SearchView'),
    
   
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
