# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
def relatorios(request):
    if request.user.is_authenticated():
        return render(request, 'relatorios.html', {'title':'Relatorios'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})