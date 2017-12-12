from django.contrib import admin
from movimentacoes.models import movimentacao, caixa_geral


admin.site.register(movimentacao)
admin.site.register(caixa_geral)