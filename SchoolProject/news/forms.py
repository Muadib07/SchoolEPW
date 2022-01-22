from django import forms

from .models import SchoolNews


class SchoolNewsForm(forms.ModelForm):
    class Meta:
        model = SchoolNews
        fields = ('title', 'news_content',)
