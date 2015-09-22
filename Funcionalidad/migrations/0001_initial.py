# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_diag', models.DateField(verbose_name='Fecha de diagnostico')),
                ('city', models.CharField(verbose_name='ciudad', max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('mail', models.EmailField(verbose_name='e-mail', blank=True, max_length=254)),
            ],
        ),
    ]
