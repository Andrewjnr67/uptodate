from django.shortcuts import render
from .models import ImageGallery

# Create your views here.
def home(request):
    return render(request, 'index.html')

def gallery(request):
    images = ImageGallery.objects.all()
    return render(request, 'gallery.html', {'images': images})   

def blog(request):
    images = ImageGallery.objects.all()
    return render(request, 'blog.html', {'images': images})   

def blogsingle(request):
    return render(request, 'blogsingle.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def uploadfile(request):
    if request.method == "POST":
       images = request.FILES.getlist('images')
       for image in images:
           ImageGallery.objects.create(images=image)
 

    return render(request, 'uploadfile.html')    


   

