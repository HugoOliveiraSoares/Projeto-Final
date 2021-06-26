from django.urls import path
from .views import experiencias

urlpatterns = [
    path('experiencias/', experiencias, name='exeriencias')
]