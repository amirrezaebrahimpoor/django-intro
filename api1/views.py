from django.shortcuts import render
from django.http import *
import random
import string

def generate_password(request):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return HttpResponse(password)

    