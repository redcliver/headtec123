# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import caixa_geral, movimentacao

# Create your views here.

def entradas(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            mov = movimentacao(tipo='E', desc=desc, total=valor)
            mov.save()
            saldo_atualizado = caixa_geral.objects.latest('id')
            saldo_atualizado = saldo_atualizado.saldo + int(valor)
            add_caixa = caixa_geral(movimentacao_caixa=mov, saldo=saldo_atualizado)
            add_caixa.save()
            msg = 'Entrada'
            return render(request, 'sucesso.html', {'title':'Sucesso', 'valor':valor, 'desc':desc, 'msg':msg})
        return render(request, 'entradas.html', {'title':'Entradas'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def saidas(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            mov = movimentacao(tipo='S', desc=desc, total=valor)
            mov.save()
            saldo_atualizado = caixa_geral.objects.latest('id')
            saldo_atualizado = saldo_atualizado.saldo - int(valor)
            add_caixa = caixa_geral(movimentacao_caixa=mov, saldo=saldo_atualizado)
            add_caixa.save()
            msg = 'Saida'
            return render(request, 'sucesso.html', {'title':'Sucesso', 'valor':valor, 'desc':desc, 'msg':msg})
        return render(request, 'saidas.html', {'title':'Saidas'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})

def contas(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            data = request.POST.get('data')
            mov = movimentacao(tipo='S', desc=desc, total=valor, data=data)
            mov.save()
            msg = 'Conta'
            return render(request, 'sucesso.html', {'title':'Sucesso', 'valor':valor, 'desc':desc, 'msg':msg})
        return render(request, 'contas.html', {'title':'Contas a pagar'})
    else:
        return render(request, 'erro.html', {'title':'Erro'})
