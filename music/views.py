from django.urls import reverse

from .forms import *
from .models import *
from django.shortcuts import render, redirect


# Create your views here.

def base(request):
    return render(request,'music/main.html',{'title': "MuFoS"})

def category_phonk(request):
    songs = Music.objects.all()
    return render(request,'music/Phonk.html',{'title': "Phonk", 'songs': songs})

def learn(request):
    return render(request,"music/learning.html")

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST, request.FILES)  # Добавлен аргумент request.FILES
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Music.objects.create(**form.cleaned_data)
                return redirect(reverse('home'))
            except:
                form.add_error(None, "Ошибка добавления музыки")

    else:
        form = NameForm()
    return render(request, 'music/name.html', {'form': form})