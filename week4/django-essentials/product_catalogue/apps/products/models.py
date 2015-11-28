from django.db import models
from datetime import datetime

class Product(models.Model):
    brand_name = models.TextField(max_length=100)
    product_name = models.TextField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(datetime.now())
    class Meta:
        db_table = 'products'
