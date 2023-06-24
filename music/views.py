from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def base(request):
    return render(request,'music/main.html',{'title': "MuFoS"})

def category_phonk(request):
    songs = Music.objects.all()
    return render(request,'music/Phonk.html',{'title': "Phonk", 'songs': songs,})

def learn(request):
    return render(request,"music/learning.html")

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('phonk/')
    else:
        form = NameForm()
    return render(request,'music/name.html', {'form': form})