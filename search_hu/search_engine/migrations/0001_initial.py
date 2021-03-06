# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityEstablishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='availabilityestablishment',
            name='establishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='establishment_available', to='search_engine.Establishment'),
        ),
    ]
