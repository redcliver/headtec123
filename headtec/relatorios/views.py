# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import render
from datetime import datetime, timedelta
from movimentacoes.models import movimentacao, caixa_geral

# Create your views here.
def relatorios(request):
    if request.user.is_authenticated():
        return render(request, 'relatorios.html', {'title':'Relatorios'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def semanal(request):
    if request.user.is_authenticated():
        hoje = datetime.today()
        one_week_ago = hoje - timedelta(days=7)
        mov = caixa_geral.objects.filter(movimentacao_caixa__data__lte=hoje, movimentacao_caixa__data__gt=one_week_ago)
        saldo_atualizado = caixa_geral.objects.latest('id')
        return render(request, 'semanal.html', {'title':'Semanal', 'mov':mov, 'hoje':hoje, 'one_week_ago':one_week_ago, 'saldo_atualizado':saldo_atualizado})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def mensal(request):
    if request.user.is_authenticated():
        hoje = datetime.today()
        one_month_ago = hoje - timedelta(days=30)
        mov = caixa_geral.objects.filter(movimentacao_caixa__data__lte=hoje, movimentacao_caixa__data__gt=one_month_ago)
        saldo_atualizado = caixa_geral.objects.latest('id')
        return render(request, 'mensal.html', {'title':'Mensal', 'mov':mov, 'hoje':hoje, 'one_month_ago':one_month_ago, 'saldo_atualizado':saldo_atualizado})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def anual(request):
    if request.user.is_authenticated():
        hoje = datetime.today()
        one_year_ago = hoje - timedelta(days=365)
        mov = caixa_geral.objects.filter(movimentacao_caixa__data__lte=hoje, movimentacao_caixa__data__gt=one_year_ago)
        saldo_atualizado = caixa_geral.objects.latest('id')
        return render(request, 'anual.html', {'title':'Anual', 'mov':mov, 'hoje':hoje, 'one_year_ago':one_year_ago, 'saldo_atualizado':saldo_atualizado})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def conta(request):
    if request.user.is_authenticated():
        return render(request, 'conta.html', {'title':'Contas'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})