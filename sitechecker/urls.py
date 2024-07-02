from django.urls import path
from .views import sitechecker

urlpatterns = [
    path('', sitechecker, name='checker')
]
