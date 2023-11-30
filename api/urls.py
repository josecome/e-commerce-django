from rest_framework import routers
from . import views as api_views
from django.urls import path, re_path

router = routers.SimpleRouter()
router.register(r'', api_views.HomeViewSet, basename="home")
router.register('category/(?P<link>[^/.]+)', api_views.CategoryViewSet, basename="category-details")
router.register('add_new_category', api_views.AddNewCategoryModelViewSet, basename="add_new_category")
router.register('add_new_product', api_views.AddNewProductModelViewSet, basename="add_new_product")
router.register('add_new_product_in_cart', api_views.AddNewProductInCartModelViewSet, basename="add_new_product_in_cart")

urlpatterns = router.urls