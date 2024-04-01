from django.db import models

# Create your models here.
class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    brand_logo = models.CharField(max_length=100)
    brand_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Motorcycles(models.Model):
    motorcycle_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    motorcycle_name = models.CharField(max_length=100)
    motorcycle_type = models.CharField(max_length=100)
    motorcycle_price = models.DecimalField(max_digits=10, decimal_places=2)
    motorcycle_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)