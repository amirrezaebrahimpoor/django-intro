from django.shortcuts import render
from django.http import *
import random
import string,requests


def generate_password(request):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return HttpResponse(password)

def random_number(request):
    num=random.randint(1,1000)
    req=requests.get('http://numbersapi.com/NUMBER',{num})
    show=req.text
    
    return HttpResponse(show)
