from django.db import models

class Tracking(models.Model):
    name = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 100)
    tracking = models.CharField(max_length = 100,null = True, blank = True)
    other = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.tracking)
    
class Product(models.Model):
    item_name = models.CharField(max_length = 100)
    price = models.DecimalField(decimal_places = 2, max_digits = 100)
    description = models.TextField(null = True, blank = True)
    other = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return '{} - {} ({})'.format(self.item_name, self.price, self.description)
