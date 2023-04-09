from django import forms
from .models import Post

class PostCreateModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user','slug')

class PostUpdateModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Title"
    }))
    class Meta:
        model = Post
        exclude = ('yazar','slug')