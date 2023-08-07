from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('',MuFoS_Home.as_view(),name='home'),
    path('phonk/', cache_page(60)(MuFoS_Phonk.as_view()), name='phonk'),
    path('music_add', MuFoS_AddMusic.as_view(), name='Music'),
    path('category_add', MuFoS_AddCategory.as_view(), name='Category'),
    path('403', MuFoS_error_403.as_view(), name='403_error'),
    path('login', MuFoS_LoginUser.as_view(), name='login'),
    path('register',MuFoS_RegisterUser.as_view(),name='register'),
    path('logout',logout_view, name='logout')
]
