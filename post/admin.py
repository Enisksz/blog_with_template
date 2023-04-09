from django.contrib import admin
from .models import Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author')
    list_filter = ('title','categories')

admin.site.register(Post,CategoryAdmin)