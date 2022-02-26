from unicodedata import category
from django.test import TestCase

# Create your tests here.
from .models import Category


class CategoryTestClass(TestCase):
  def setUp(self):
    self.buildings=Category(category_name='Buildings',category_slug_name='photos_of_buildings')

  def test_instance(self):
    self.assertTrue(self.buildings,Category)

  def test_instance_variables(self):
    self.assertEquals(self.buildings.category_name,'Buildings')
    self.assertEquals(self.buildings.category_slug_name,'photos_of_buildings')

  def test_save_category(self):
    self.buildings.save_category()
    self.assertTrue(len(Category.objects.all())>0)