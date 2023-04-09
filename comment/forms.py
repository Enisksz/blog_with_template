from django import forms
from .models import Comment

class CommentAddModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','stars')