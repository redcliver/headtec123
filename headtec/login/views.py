# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.
def login1(request):
    return render(request, 'login.html', {'title':'Login'})

def logout(request):
    logout()
    return render(request, 'logout.html', {'title':'Logout'})

def erro(request):
    return render(request, 'erro.html', {'title':'Erro'})