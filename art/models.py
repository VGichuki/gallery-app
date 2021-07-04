from django.db import models
import datetime as dt
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    '''
    class that categorises the images
    '''
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_category(cls, category):
        category = cls.objects.filter(name = category)
        return category

class Location(models.Model):
    '''
    class that defines the location of an image
    '''
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls,location):
        location = cls.objects.filter(name = location)
        return location

class Image(models.Model):
    '''
    class that contains the image details in the database
    '''
    image_url = models.ImageField(upload_to='images/',blank=True)
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    posted_on = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        found = cls.objects.filter(id=image_id)
        return found

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(category__name__icontains=category).all()
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        images = Image.objects.filter(location=location).all()
        return images.url

    class Meta:
        ordering = ['image_name']


   




