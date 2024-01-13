from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from contents.models import (
    ProdCategory,
    Product,
    Cart,
)


@receiver(post_save, sender=ProdCategory)
def category_created(sender, instance, created, **kwargs):
   if created:
      print('New Category of Products added:', instance.category)


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
   if created:
      print('New Product created:', instance.product)


@receiver(post_save, sender=Cart)
def cart_created(sender, instance, created, **kwargs):
   if created:
      print('New Product in Cart added:', instance.article)