from django.contrib import admin
from django.urls import path
import api1.views

urlpatterns = [
    path('generate-password/',api1.views.generate_password),
    path('random-number/',api1.views.random_number)
]