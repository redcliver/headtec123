# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class caixa_geral(models.Model):
    TIPO = (
        ('E', 'Entrada'),
        ('S', 'Saida'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    data = models.DateTimeField(default=timezone.now())
    desc = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.id)
