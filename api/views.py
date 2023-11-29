from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count

from .serializer import (
    ProdCategorySerializer,
    ProductSerializer,
    )
from contents.models import (
    ProdCategory,
    Product,
    )


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = ProdCategorySerializer
    queryset = ProdCategory.objects.all()[:12]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:1]
    
    def get_queryset(self):
        link = self.kwargs['link']
        if link:
            self.queryset = Product.objects.filter(link=link)
            return self.queryset
        else:
            return self.queryset

