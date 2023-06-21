from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request,'music/main.html',{'title': "MuFoS"})

def category_phonk(request):
    songs = Music.objects.all()
    return render(request,'music/Phonk.html',{'title': "Phonk", 'songs': songs,})

def learn(request):
    return render(request,"music/learning.html")