from django.urls import path
from .views import formacao

urlpatterns = [
    path('formacao/', formacao, name='formacao')
]