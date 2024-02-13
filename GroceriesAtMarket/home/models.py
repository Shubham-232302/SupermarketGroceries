from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100, unique=True)

class SubCategory(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
