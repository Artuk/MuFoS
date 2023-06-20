from django.urls import path
from .views import *


urlpatterns = [
    path('',base,name='home'),
    path('phonk/<int:category_id>', category_phonk, name='phonk')
]
