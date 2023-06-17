from django.shortcuts import render
from django.http import HttpResponse as httpResponse
from django.shortcuts import render, redirect 
from django.core import serializers
from .models import ProdCategory
from .models import Product
from .forms import ProdCategoryForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


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
            messages.success(request, _('Category successfull created'))
            form_instance= form.instance  
            return render(request, 'result_page.html', {'form': form_instance}) 
        else:
            messages.info(request, _('Error creating Category'))
            return render(request, 'result_page.html') 
                        
    else:
        messages.info(request, _('Request not valid')) 
        return redirect("/")
    

def Products_for_Sale(request, category):
    return render(request, 'products_for_sale.html', {'product' : category})


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
    data = Product.objects.filter(category_id=category_id).prefetch_related('category').all()

    return render(request, 'product.html', {'category': category, 'products': data})  


