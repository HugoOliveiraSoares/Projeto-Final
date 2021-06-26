from django.urls import path
from .views import certificados

urlpatterns = [
    path('certificados/', certificados, name='certificados')
]