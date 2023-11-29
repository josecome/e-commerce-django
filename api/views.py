from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
from contents.models import (
    ProdCategory,
    Product,
)

from .serializer import (
    ProdCategorySerializer,
    )
from contents.models import (
    ProdCategory,
    Product,
    )


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = ProdCategorySerializer
    queryset = ProdCategory.objects.all()[:12]


