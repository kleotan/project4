from attr import field
from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
