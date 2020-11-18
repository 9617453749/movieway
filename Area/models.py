from django.db import models

# Create your models here.

class movies(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    link = models.CharField(max_length=200,null='True')
    link1 = models.CharField(max_length=200,null='True')
    link7 = models.CharField(max_length=200,null='True')
    Image = models.ImageField(upload_to="media/pics")

