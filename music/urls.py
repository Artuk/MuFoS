from django.urls import path
from .views import *


urlpatterns = [
    path('',base,name='home'),
    path('phonk/', category_phonk, name='phonk'),
    path('learn/',learn),
    path('music_add', AddMusic, name='Music'),
    path('category_add', AddCategory, name='Category')
]
