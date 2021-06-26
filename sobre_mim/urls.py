from django.urls import path
from .views import sobre_mim

urlpatterns = [
    path('sobre_mim/', sobre_mim, name='sobre_mim')
]