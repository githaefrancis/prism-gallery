from distutils.command.upload import upload
from unicodedata import category
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

  def __str__(self):
    return self.image_name

  def save_image(self):
    self.save()

  def delete_image(self):
    '''
    method to delete an image from the database
    '''
    self.delete()

  @classmethod
  def get_image_by_id(cls,id):
    '''
    method that fetches and image by id
    '''
    return Image.objects.filter(id=id).first()


  @classmethod
  def search_image(cls,category):
    '''
    method that searches for images per category
    '''
    target_category=Category.objects.filter(category_name__contains=category).first()
    return Image.objects.filter(category=target_category).all()

  @classmethod
  def filter_by_location(cls,location):
    '''
    method that fetches images based on location
    '''
    target_location=Location.objects.filter(location_name__contains=location).first()
    return Image.objects.filter(location=target_location).all()

  def update_image(self,**kwargs):
    '''
    Method to update image object details
    '''
    for key,value in kwargs.items():
      setattr(self,key,value)
    self.save()
    return