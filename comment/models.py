from django.db import models
from post.models import Post
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey('user.CustomUserModel',on_delete=models.CASCADE,related_name='comment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ])

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    
    def __str__(self):
        return self.comment[:9]