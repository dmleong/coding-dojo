from django.db import models

# define our custom QuerySet function that inherits from the default QuerySet class
class ProductQueryset(models.query.QuerySet):
    def active(self):
 # have each function return a QuerySet
        return self.filter(is_active=True)
    def featured(self):
 # have each function return a QuerySet
        return self.filter(is_featured=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)
    def active(self):
        return self.get_queryset().active()
    def featured(self):
        return self.get_queryset().featured()

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    objects = ProductManager() # set the objects attribute to our custom model Manager
    def __str__(self):
        return self.name

