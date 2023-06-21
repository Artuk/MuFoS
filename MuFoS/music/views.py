from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request,'music/main.html',{'title': "Главная страница"})

def category_phonk(request,category_id):
    songs = Music.objects.filter(id = category_id)
    path_phonk = Music.objects.get(id=category_id)
    return render(request,'music/Phonk.html',{'title': "Музыка", 'songs': songs,'path_phonk': path_phonk})

def learn(request):
    return render(request,"music/learning.html")