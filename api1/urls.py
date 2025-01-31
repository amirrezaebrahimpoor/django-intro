from django.contrib import admin
from django.urls import path
import api1.views

urlpatterns = [
    path('generate-password/',api1.views.generate_password)
]