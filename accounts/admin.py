

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
 
 
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('game_status',)}),)
    list_display = ['username', 'email', 'game_status']
 
 
admin.site.register(CustomUser, CustomUserAdmin)