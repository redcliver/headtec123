# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def controle(request):
    return render(request, 'controle.html', {'title':'Controle'})