from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

def is_admin(user):
    return User.objects.filter(is_superuser=1).exists()


admin_required = user_passes_test(is_admin)