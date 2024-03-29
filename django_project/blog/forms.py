
from django.forms import ModelForm
from .models import Post, Comment

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']