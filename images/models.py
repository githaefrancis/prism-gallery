from distutils.command.upload import upload
from django.db import models
from category.models import Category

from location.models import Location
# Create your models here.

class Image(models.Model):
  image_name=models.CharField(max_length=100)
  image_description=models.CharField(max_length=500)
  image=models.ImageField(upload_to='photos/images')
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  location=models.ForeignKey(Location,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)

  def save_image(self):
    self.save()
