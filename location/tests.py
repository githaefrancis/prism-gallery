from django.test import TestCase

# Create your tests here.

from .models import Location

class LocationTestClass(TestCase):

  def setUp(self):
    self.nairobi=Location(location_name='Nairobi',location_slug='nairobi_city',location_description='Capital City of Kenya')

  def test_instance(self):
    self.assertTrue(isinstance(self.nairobi,Location))

  def test_instance_variables(self):
    self.assertEquals(self.nairobi.location_name,'Nairobi')
  
  def test_save_location(self):
    self.nairobi.save_location()
    locations=Location.objects.all()
    self.assertTrue(len(locations)>0)
