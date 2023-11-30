from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse as Response
from rest_framework import status
from django.db.models import Q, Count

from .serializer import (
    ProdCategorySerializer,
    ProductSerializer,
    CartSerializer,
    )
from contents.models import (
    ProdCategory,
    Product,
    )
from datetime import date, datetime


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = ProdCategorySerializer
    queryset = ProdCategory.objects.all()[:12]

# Product by category
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


class AddNewCategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProdCategorySerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        server_data = {'user': request.user.id, 'date_created': date.today(), 'date_updated': date.today()}
        category_data = request.data

        serializer = self.serializer_class(data = { **server_data, **category_data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddNewProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        server_data = {'user': request.user.id, 'date_created': date.today(), 'date_updated': date.today()}
        product_data = request.data

        serializer = self.serializer_class(data = { **server_data, **product_data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddNewProductInCartModelViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        server_data = {'user': request.user.id, 'date_created': date.today(), 'date_updated': date.today()}
        product_in_cart_data = request.data

        serializer = self.serializer_class(data = { **server_data, **product_in_cart_data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)