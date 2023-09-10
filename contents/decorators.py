from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import Project_Form_Meta, Project_Form

def is_admin(user):
    return User.objects.filter(is_superuser=1).exists()

admin_required = user_passes_test(is_admin)