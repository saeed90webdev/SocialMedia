from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "phone" ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ('date_of_birth', 'bio', 'photo', 'job', 'phone')}),
    )

