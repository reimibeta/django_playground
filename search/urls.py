from django.urls import path
from rest_framework.routers import DefaultRouter
from phone_verify.api import VerificationViewSet

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
