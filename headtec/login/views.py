# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login1(request):
    return render(request, 'login.html', {'title':'Login'})