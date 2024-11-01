from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
UserAdmin.fieldsets[2][1]['fields']=(
    'is_active',
    'is_staff',
    'groups',
    'user_permissions',
    'is_author',
    'is_seller',
)
UserAdmin.list_display+=('is_author','is_seller')
admin.site.register(User,UserAdmin)
