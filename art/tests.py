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
    def test_instance(self):
        self.assertTrue(isinstance(self.cg1,Category))
        self.assertTrue(isinstance(self.cg2, Category))
    def test_save_method(self):
        self.cg1.save_category()
        self.cg2.save_category()
        categories = Category.objects.all()
        self.assertEquals(len(categories),2)
