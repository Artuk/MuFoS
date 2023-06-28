from django import forms
from .models import *


class NameForm(forms.Form):
    song_name = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)
    song = forms.FileField()
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(),empty_label="Категория не выбрана")

class NameCategory(forms.Form):
    category_name = forms.CharField(max_length=100)