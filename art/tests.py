from django.test import TestCase
from .models import Category, Location,Image

# Create your tests here.
class CategoryTestCase(TestCase):
    '''
    class that will test the functions under class Category
    '''
    def setUp(self):
        self.cg1 = Category(name = 'oil painting')
        self.cg2 = Category(name = 'watercolor painitng')

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.cg1,Category))
        self.assertTrue(isinstance(self.cg2, Category))

    def test_save_method(self):
        self.cg1.save_category()
        self.cg2.save_category()
        categories = Category.objects.all()
        self.assertEquals(len(categories),2)

    def test_delete(self):
        self.cg1.save_category()
        self.cg2.save_category()
        self.cg1.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)<2)

class LocationTestCase(TestCase):
    '''
    class that test the functions under class Location
    '''
    def setUp(self):
        self.lc1 = Location(name = 'Nairobi')
        self.lc2 = Location(name = 'Nakuru')

    def test_instance(self):
        self.assertTrue(isinstance(self.lc1,Location))
        self.assertTrue(isinstance(self.lc2,Location))

    def test_save_method(self):
        self.lc1.save_location()
        self.lc2.save_location()
        locations = Location.objects.all()
        self.assertEquals(len(locations),2)

    


    
