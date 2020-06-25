from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField( max_length=50)
    dis = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    img = models.ImageField( upload_to='image', height_field=None, width_field=None, max_length=None)