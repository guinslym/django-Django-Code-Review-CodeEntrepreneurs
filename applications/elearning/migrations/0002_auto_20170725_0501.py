# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 09:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_minutes',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(60)]),
        ),
    ]