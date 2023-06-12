from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProdCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=16)
    description = models.CharField(max_length=60)   
    image_link = models.CharField(max_length=40)  
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  
        db_table = "prod_category"      