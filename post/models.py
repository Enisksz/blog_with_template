from django.db import models
from autoslug import AutoSlugField
from category.models import Category
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post_image',blank=True,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey('user.CustomUserModel',on_delete=models.CASCADE,related_name='posts')
    categories = models.ManyToManyField(Category,related_name='post')

    def __str__(self):
        return self.title