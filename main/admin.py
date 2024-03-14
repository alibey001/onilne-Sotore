from django.contrib import admin
from .models import  *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

admin.site.register(Product)
