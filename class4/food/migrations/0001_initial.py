# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('portion_in_grams', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('food_type', models.CharField(max_length=255, choices=[('carbohydrate', 'Carbohydrate'), ('dairy', 'Dairy'), ('fruit', 'Fruit'), ('protein', 'Protein'), ('vegetable', 'Vegetable')])),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('items', models.ManyToManyField(to='food.Item')),
            ],
        ),
    ]
