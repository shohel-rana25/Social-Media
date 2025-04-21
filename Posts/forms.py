from django import forms
from .models import PostModel
from .models import CommentModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['profile','caption', 'image', 'likes']




class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a comment...'
            }),
        }