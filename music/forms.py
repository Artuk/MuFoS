from django import forms
from .models import *
from django.core.exceptions import ValidationError

class NameForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"


    def clean_song_name(self):
        song_name = self.cleaned_data["song_name"]
        if len(song_name) > 25:
            raise ValidationError("Длина песни больше 25 символов")

        return song_name




class NameCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

