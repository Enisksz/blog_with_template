from django.contrib import admin
from .models import CustomUserModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username','email')
    fieldsets = UserAdmin.fieldsets + (('Image değiştirme alanı',{
        'fields':['image']
    }),)

admin.site.register(CustomUserModel,CustomAdmin)