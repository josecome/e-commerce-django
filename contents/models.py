from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProdCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=16)
    description = models.CharField(max_length=60)   
    image = models.ImageField(upload_to = 'images/', null=True)
    date_created = models.DateField(null=True)
    date_updated = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "prod_category"    


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=16)
    description = models.CharField(max_length=60)   
    category = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=200.00)
    image = models.ImageField(upload_to = 'images/', null=True)
    date_created = models.DateField(null=True)
    date_updated = models.DateField(null=True)
    category = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "product"    
        