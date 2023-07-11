from django.db import models

# Create your models here.
# class ImageGallery(models.Model):
#     images = models.FileField()
 

class Feature(models.Model):
    # id: int
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)
    # is_true: bool


class Service(models.Model):
    # id: int
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)
    # is_true: bool