from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Category   
# Register your models here.

class CategoryAdmin(ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('name',)

admin.site.register(Category,CategoryAdmin)