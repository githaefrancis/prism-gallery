from django.test import TestCase

# Create your tests here.
from .models import Image,Category,Location

class ImageTestClass(TestCase):
  def setUp(self):
    self.nairobi=Location(location_name='Nairobi',location_slug='nairobi_city',location_description='Capital City of Kenya')
    self.buildings=Category(category_name='Buildings',category_slug_name='photos_of_buildings')

    self.cat_img=Image(image_name='KICC',image_description='A picture of KICC building',category=self.buildings,location=self.nairobi)

  # def tearDown(self):
  #   Image.objects.all().delete()

  def test_instance(self):
    self.assertTrue(self.cat_img,Image)


  def test_save_image(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()
    self.assertTrue(len(Image.objects.all())>0)


  def test_delete_image(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()
    self.cat_img.delete_image()

    self.assertTrue(len(Image.objects.all())==0)


  def test_get_image_by_id(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()
    print(self.cat_img.id)
    self.image_result=Image.get_image_by_id(self.cat_img.id)
    self.assertEquals(self.image_result.id,self.cat_img.id)

  def test_search_image(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()

    self.search_results=Image.search_image('Buildings')
    print(self.search_results)
    self.assertTrue(len(self.search_results)>0)


  def test_filter_by_location(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()

    self.filter_results=Image.filter_by_location('Nairobi')

    self.assertTrue(len(self.filter_results)>0)

  def test_update_image(self):
    self.buildings.save_category()
    self.nairobi.save_location()
    self.cat_img.save_image()

    self.target_image=Image.get_image_by_id(self.cat_img.id)
    self.cat_img.update_image(image_name='KICC TOWER')

    self.assertEquals(Image.get_image_by_id(self.cat_img.id).image_name,'KICC TOWER')