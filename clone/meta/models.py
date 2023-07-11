from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class BlogCategory(models.Model):
    post_cate = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.post_cate}'

    def get_absolute_url(self):
        return reverse('home') 

class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    blogcategory = models.CharField(max_length=200, default='testing')
    image = models.ImageField(null=True, blank=True, upload_to= 'images/')
    social_instagram = models.CharField( max_length=200, null= True, blank=True )
    social_facebook = models.CharField( max_length=200, null= True, blank=True )
    social_telegram = models.CharField( max_length=200, null= True, blank=True )
    # comment =  models.CharField( max_length=800, null= True, blank=True )
    created = models.DateTimeField(auto_now_add=True)
    slug= models.SlugField(null=True)

    def __str__(self):
        return f'{self.author}- {self.title}'

    def get_absolute_url(self):
        return reverse('home')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to= 'images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}- {self.job_title}'

    def get_absolute_url(self):
        return reverse('home')

    
class Blogcat(models.Model):    
    cate_name = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.cate_name}'

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:

    #     varbose_name = 'Comment'
    #     varbose_name_plural = 'Comments'

    def __str__(self):
        return self.name



    