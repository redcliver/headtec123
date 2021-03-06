# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movimentacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], max_length=1)),
                ('data', models.DateTimeField(default=datetime.datetime(2017, 12, 6, 19, 8, 21, 766570, tzinfo=utc))),
                ('desc', models.CharField(max_length=200)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AddField(
            model_name='caixa_geral',
            name='movimentacao_caixa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.movimentacao'),
            preserve_default=False,
        ),
    ]
