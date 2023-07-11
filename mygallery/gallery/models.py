from django.db import models

# Create your models here.
class ImageGallery(models.Model):
    images = models.FileField()
 