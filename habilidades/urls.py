from django.urls import path
from .views import habilidades

urlpatterns = [
    path('habilidades/', habilidades, name='habilidades')
]