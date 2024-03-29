from django.shortcuts import render
from django.http import HttpResponse as httpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .models import ProdCategory, Product, Cart
from .forms import ProdCategoryForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from .utils import (
    send_activation_email, 
    send_reset_password_email, 
    send_forgotten_username_email, 
    send_activation_change_email,
)
from .decorators import admin_required
from django.conf import settings

# Create your views here.
def Home(request):     
    form = ProdCategoryForm()  
    prodcat = ProdCategory.objects.all()
    return render(request, 'home.html', {'form': form, 'prodcat': prodcat})  


def Create_Category(request):
    if request.method == "POST":
        form = ProdCategoryForm(request.POST, request.FILES)  
        print(form.errors)
        if form.is_valid(): 
            ctgry = form.save(commit=False)
            ctgry.user_id = 1
            ctgry.save() 
            messages.success(request, _(settings.SUCCESS_INSERT))
            form_instance= form.instance  
            return render(request, 'result_page.html', {'form': form_instance}) 
        else:
            messages.info(request, _(settings.ERROR_INSERT_CATEGORY))
            return render(request, 'result_page.html') 
                        
    else:
        messages.info(request, _(settings.REQUEST_NOT_VALID)) 
        return redirect("/")
    

def Products_for_Sale(request, category):
    return render(request, 'products_for_sale.html', {'product' : category})


@cache_page(60 * 15)
def ProductsForSaleList(request, category):
    print('Start...')
    print(category)
    category_id = int(ProdCategory.objects.get(category=category).pk)        
    print(category_id)
    data = Product.objects.filter(category_id=category_id)
    print(str(data))
    json_data = serializers.serialize('json', data)

    return httpResponse(json_data, content_type="application/json")


def Products(request, category):
    category_id = int(ProdCategory.objects.get(category=category).pk)    
    data = Paginator(Product.objects.filter(category_id=category_id).prefetch_related('category').all(), 8)
    # page_number = request.GET.get("page")
    data_obj = data.get_page(1)

    return render(request, 'product.html', {'category': category, 'products': data_obj})  


def ProductForm(request):    
    category = request.GET['pg']
    t = None
    try:
        t = request.GET['t']
    except:
        t = '_'    

    if t is not None and t == "edit":
        id = int(request.GET['id'])
        data = Product.objects.get(id=id)
        print(data)
        return render(request, 'product_form.html', {'category': category, 'product': data})  
    
    return render(request, 'product_form.html', {'category': category})  


def ProductInCart(request, user_id):
    data = Cart.objects.filter(user_id=user_id)
    json_data = serializers.serialize('json', data)

    return httpResponse(json_data, content_type="application/json")


def ListOfCategories(request):
    data = ProdCategory.objects.all()
    json_data = serializers.serialize('json', data)

    return httpResponse(json_data, content_type="application/json")


# @login_required(login_url='login.html')    
def Dashboard(request):
    return render(request, 'dashboard.html') 


def Dashboard_data(request):
    json_data = {'key': 'value'}
    return httpResponse(json_data, content_type="application/json")


@admin_required
def disable_project_by_admin():
    # Require admin
    pass


    

    

