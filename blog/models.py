from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1000,blank=True,null=True)
    summary = models.TextField(blank=True,null=True)
    bold = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="blog/images/",blank=True,null=True)