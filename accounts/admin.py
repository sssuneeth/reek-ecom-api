from django.contrib import admin

from .models import User


#User model
class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['email', 'name']
admin.site.register(User, AdminUser)