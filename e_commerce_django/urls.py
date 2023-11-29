"""e_commerce_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from contents import views

urlpatterns = [
    path('', views.Home, name="home"), 
    path('admin/', admin.site.urls),
    path('add_category/', views.Create_Category, name="add_category"),
    path('products_for_sale/<str:category>', views.Products_for_Sale, name="products_for_sale"),
    path('products_for_sale_list/<str:category>', views.ProductsForSaleList, name="products_for_sale_list"),
    path('products/<str:category>', views.Products, name="products"),
    path('product_form/', views.ProductForm, name="product_form"),
    path('productincart/<int:user_id>', views.ProductInCart, name="productincart/"),
    path('listofcategories/', views.ListOfCategories, name="listofcategories"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('dashboard_data/', views.Dashboard_data, name="dashboard_data"),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

