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

    def test_get_category(self):
        self.cg1.save_category()
        self.cg2.save_category()

        found_category = Category.search_category('oil painting')
        self.assertEquals(len(found_category),1)

class LocationTestCase(TestCase):
    '''
    class that test the functions under class Location
    '''
    def setUp(self):
        self.lc1 = Location(name = 'Nairobi')
        self.lc2 = Location(name = 'Nakuru')

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lc1,Location))
        self.assertTrue(isinstance(self.lc2,Location))

    def test_save_method(self):
        self.lc1.save_location()
        self.lc2.save_location()
        locations = Location.objects.all()
        self.assertEquals(len(locations),2)

    def test_delete(self):
        self.lc1.save_location()
        self.lc2.save_location()
        self.lc1.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<2)

    def test_get_location(self):
        self.lc1.save_location()
        self.lc2.save_location()

        found_location = Location.get_location('Nairobi')
        self.assertEquals(len(found_location),1)

class ImageTestCase(TestCase):
    '''
    testcase for the functions under class image
    '''
    def setUp(self):
        #Categories
        self.cg1 = Category(name = 'oil painting')
        self.cg2 = Category(name = 'watercolor painiting')
        self.cg1.save_category()
        self.cg2.save_category()

        #Locations
        self.lc1 = Location(name = 'Nairobi')
        self.lc2 = Location(name = 'Nakuru')
        self.lc1.save_location()
        self.lc2.save_location()

        #Image
        self.img1 = Image(image_url = "images/op1.jpeg",image_name="op1",description="It is a beautiful sunset", posted_on="2021-07-04",category= self.cg1, location= self.lc1)
        self.img2 = Image(image_url="images/wc1.jpg",image_name="wc1",description="It is a lake type of day", posted_on="2021-07-04",category= self.cg2, location = self.lc2)
        self.img1.save_image()
        self.img2.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.img1, Image))
        self.assertTrue(isinstance(self.img2, Image))

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_method(self):
        self.img1.save_image()
        self.img2.save_image()

        savedimages = Image.objects.all()
        self.assertEquals(len(savedimages),2)
    def test_delete(self):
        self.img1.save_image()
        self.img2.save_image()

        self.img1.delete_image()
        savedimages = Image.objects.all()
        self.assertEquals(len(savedimages),1)

    def test_get_image_by_id(self):
        self.img1.save_image()
        self.img2.save_image()
        try:
            found=Image.get_image_by_id(self.img1.id)
        except ValueError:
            raise AttributeError
        self.assertEquals(len(found),1)

    # def test_search(self):
    #     self.img1.save_image()
    #     self.img2.save_image()

    #     search_term='Oil painting'
    #     found_


    
