from django import forms
from .models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields  = ['title','category','content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 30}),
        }

