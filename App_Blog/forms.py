from django import forms
from django.db import models
from django.forms import fields
from App_Blog.models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Comment',)
