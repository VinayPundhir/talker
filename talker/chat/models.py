from __future__ import unicode_literals

from django.db import models
from PIL import Image

class user_data(models.Model):
   image=models.ImageField(upload_to='pictures')
   name=models.CharField(max_length=20)
   user=models.CharField(max_length=20)
   password=models.CharField(max_length=20)
   age=models.IntegerField()
   color=models.CharField(max_length=20,default="white")
   

class relation(models.Model):
   name=models.CharField(max_length=20)
   Request=models.CharField(max_length=20)

class friend(models.Model):
    name=models.CharField(max_length=20)
    friend_name=models.CharField(max_length=20)

class chat_data(models.Model):
    name=models.CharField(max_length=20)
    friend_name=models.CharField(max_length=20)
    msg=models.CharField(max_length=254,default="")
    image=models.ImageField(upload_to='pictures',default="cht2.jpeg")
    num=models.IntegerField()
    
class record(models.Model):
  name=models.CharField(max_length=5)
  num =models.IntegerField()

class active(models.Model):
  name=models.CharField(max_length=30)

class channel(models.Model):
  channel_name=models.CharField(max_length=40)
  name=models.CharField(max_length=20)
  friend_name=models.CharField(max_length=20)

