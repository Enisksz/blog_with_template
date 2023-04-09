from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=('user','post','comment')
    list_filter = ('user','post')

admin.site.register(Comment,CommentAdmin)