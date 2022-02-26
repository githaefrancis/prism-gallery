from django.test import TestCase

# Create your tests here.
from .models import Image,Category,Location

class ImageTestClass(TestCase):
  def setUp(self):
    self.nairobi=Location(location_name='Nairobi',location_slug='nairobi_city',location_description='Capital City of Kenya')
    self.buildings=Category(category_name='Buildings',category_slug_name='photos_of_buildings')

    self.cat_img=Image(image_name='KICC',image_description='A picture of KICC building',category=self.buildings,location=self.nairobi)

  def test_instance(self):
    self.assertTrue(self.cat_img,Image)


  def test_save_image(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()
    self.assertTrue(len(Image.objects.all())>0)


