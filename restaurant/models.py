from django.db import models
from django.test import TestCase

class Booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingdate=models.DateTimeField()

class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
