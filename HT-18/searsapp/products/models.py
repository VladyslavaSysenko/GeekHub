from django.db import models


class Product(models.Model):
    site_id = models.CharField(max_length=50)
    name = models.TextField()
    link = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    store = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
