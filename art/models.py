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

class Image(models.Model):
    '''
    class that contains the image details in the database
    '''
    # image_url = models.ImageField(upload_to='images/', blank = True)
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    posted_on = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
