from django.urls import path
from .views import *


urlpatterns = [
    path('',MuFoS_Home.as_view(),name='home'),
    path('phonk/', MuFoS_Phonk.as_view(), name='phonk'),
    path('music_add', MuFoS_AddMusic.as_view(), name='Music'),
    path('category_add', MuFoS_AddCategory.as_view(), name='Category'),
    path('403', MuFoS_error_403.as_view(), name='403_error')
]
