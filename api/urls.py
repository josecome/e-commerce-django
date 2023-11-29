from rest_framework import routers
from . import views as api_views
from django.urls import path, re_path

router = routers.SimpleRouter()
router.register(r'', api_views.HomeViewSet, basename="home")

urlpatterns = router.urls