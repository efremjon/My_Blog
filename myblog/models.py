from audioop import reverse
from distutils.command.upload import upload
import imp
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    body=models.TextField(blank=True,null=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    telegram=models.CharField(max_length=100,null=True,blank=True)
    facebook=models.CharField(max_length=100,null=True,blank=True)
    twitter=models.CharField(max_length=100,null=True,blank=True)
    instagram=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.user)
class Catagory(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title 
    def get_absolute_url(sefl):
        return reverse ('home')

class Post(models.Model):
    title=models.CharField(max_length=100)
    title_tag=models.CharField(max_length=100,default='efa bloogs')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    catagory2=models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    like=models.ManyToManyField(User,related_name='blog_post')
    hader_image=models.ImageField(null=True,blank=True, upload_to='Image/')
    def total_likes(self):
        return self.like.count()
    def __str__(self) -> str:
        return self.title + ' | '+ str(self.author)
    def get_absolute_url(sefl):
        return reverse ('home')