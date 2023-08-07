from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, CreateView
from .forms import *
from .models import *
from django.shortcuts import render, redirect


# Create your views here.

def error_403(request, exception):
    return redirect(reverse_lazy('403_error'))

def login(request):
    return redirect(reverse_lazy('home'))

def logout_view(request):
    logout(request)
    return redirect('login')
class MuFoS_Home(ListView):
    model = Music
    template_name = 'music/base.html'
    extra_context = {'title': 'MuFoS'}

class MuFoS_Phonk(ListView):
    model = Music
    template_name = 'music/Phonk.html'
    extra_context = {'title': 'Phonk'}
    context_object_name = 'songs'
    paginate_by = 4
    ordering = 'song_name'



class MuFoS_error_403(ListView):
    model = Music
    template_name = 'music/403_error.html'
    extra_context = {'title': 'Доступ запрещен'}

class MuFoS_AddMusic(LoginRequiredMixin,FormView):
    form_class = NameForm
    template_name = 'music/Addmusic.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    raise_exception = True


    def form_valid(self, form):
        form.save()  # Сохранение данных формы
        return super().form_valid(form)



class MuFoS_AddCategory(LoginRequiredMixin,FormView):
    form_class = NameCategory
    success_url = reverse_lazy('home')
    context_object_name = 'form'
    login_url = reverse_lazy('home')
    template_name = 'music/AddCategory.html'
    raise_exception = True

class MuFoS_RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'music/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

class MuFoS_LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'music/login.html'

    def get_success_url(self):
        return reverse_lazy('home')