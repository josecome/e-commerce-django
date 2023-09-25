from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SharedFields(models.Model):
    description = models.CharField(max_length=60)   
    date_created = models.DateField(null=True)
    date_updated = models.DateField(null=True)

    class Meta:
        abstract = True


class ProdCategory(SharedFields):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=16)
    image = models.ImageField(upload_to = 'images/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "prod_category"    


class Product(SharedFields):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=16) 
    category = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=200.00)
    image = models.ImageField(upload_to = 'images/', null=True)
    category = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "product"


class Cart(SharedFields):
    id = models.AutoField(primary_key=True)
    article = models.CharField(max_length=16, default='No Product')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=200.00)
    qnty = models.IntegerField(default=1)
    totalprice = models.DecimalField(max_digits=5, decimal_places=2, default=200.00)
    purchased = models.BooleanField()
    category = models.CharField(max_length=16)
    category = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "cart"