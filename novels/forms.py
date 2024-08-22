from django import forms
from .models import Novel

class NovelForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'author', 'genre', 'published_date', 'synopsis']
