# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='aums_id', primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.FloatField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.FloatField(null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.FloatField(max_length=5, null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.FloatField(max_length=5, null=True, verbose_name='12th Mark', blank=True),
        ),
    ]
