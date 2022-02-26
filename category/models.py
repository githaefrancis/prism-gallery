from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
  category_name=models.Charfield(max_length=100)
  category_slug_name=models.CharField(max_length=100,blank=True)