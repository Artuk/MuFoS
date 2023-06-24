from django.urls import path
from .views import *


urlpatterns = [
    path('',base,name='home'),
    path('phonk/', category_phonk, name='phonk'),
    path('learn/',learn),
    path('your_name', get_name, name='name')
]
