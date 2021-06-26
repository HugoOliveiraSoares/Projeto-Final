from django.urls import path
from .views import objetivo

urlpatterns = [
    path('objetivo/', objetivo, name='objetivo')
]