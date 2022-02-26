from django.db import models

# Create your models here.

class Location(models.Model):
  location_name=models.CharField(max_length=500)
  location_slug=models.CharField(max_length=200,blank=True)
  location_description=models.CharField(max_length=500)
  created_at=models.DateTimeField(auto_now_add=True)


  def save_location(self):
    """
    Method that saves a new location
    Args: 
        self: a new instance of the location model
    """
    self.save()
