from django.db import models
import re
from django.db import models
from django_google_maps import fields as map_fields

from django.utils import timezone


from django import urls

# Create your models here.

class imggal(models.Model):
    imgtitle= models.CharField(max_length=100)
    imgdesc= models.TextField()
    image= models.ImageField(upload_to='images/', default= "")

    def __str__(self):
        return  self.imgtitle
  
    


class Contact(models.Model):
   # sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    message= models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from  ' + self.name + '  - ' + self.email



class homedesc(models.Model):
    home= models.TextField()



class Ourservice(models.Model):
    mainimage= models.ImageField(upload_to='images/', default= "")
    iconimage= models.ImageField(upload_to='images/', default= "")
    servicetitle= models.CharField(max_length=100 , default= "")
    servicedesc= models.TextField(max_length=250, default= "" )
    timeStamp= models.DateTimeField(null=True, blank=True, default= "")
    servicereadmore= models.CharField(max_length=16, default= "")

    def __str__(self):
        return self.servicetitle



class about(models.Model):
    aboutdesc= models.TextField()
    aboutimage= models.ImageField(upload_to='images/', default= "")
    timeStamp= models.DateTimeField(null=True, blank=True, default= "")

   
    

    