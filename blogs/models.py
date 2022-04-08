from distutils.command.upload import upload
from email.policy import default
from enum import unique
from logging import lastResort
from pydoc import describe
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from autoslug import AutoSlugField



class User(AbstractUser):
    mobile_number = models.IntegerField(blank=True,null=True)
    mail = models.EmailField()
    company = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=10,null = True)
    country = models.CharField(max_length=10,null=True)
    about = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='user_image/',null=True,blank=True)


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name',unique=True,null=True)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=110)
    description  = models.TextField()
    slug = AutoSlugField(populate_from='name',unique=True , null=True)


    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    thumbnailImage = models.ImageField(upload_to='thumbnail_images/',null=True,blank=True)
    featureImage = models.ImageField(upload_to='feature_images/',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True, related_name='blog_category')
    tag = models.ManyToManyField(Tag,blank=True)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments', default='')
    parent = models.ForeignKey('self', null=True,blank=True,on_delete=models.CASCADE, related_name='replies',default='')
    mail = models.EmailField(blank=True, null=True)
    comment = models.TextField(blank=True,null=True)
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.comment