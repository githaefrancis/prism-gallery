from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
  category_name=models.CharField(max_length=100)
  category_slug_name=models.CharField(max_length=100,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)


  def save_category(self):
    self.save()