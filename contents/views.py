from django.shortcuts import render
from .models import ProdCategory

# Create your views here.
def Home(request):     
    prodcat = ProdCategory.objects.all()
    return render(request, 'home.html', {'prodcat': prodcat})     