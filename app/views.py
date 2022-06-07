from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def register_user(request):
    return render(request,'auth/register.html')