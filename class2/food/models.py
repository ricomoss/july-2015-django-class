from django.db import models

from food import constants


class Item(models.Model):
    name = models.CharField(max_length=255)
    portion_in_grams = models.IntegerField()
    calories = models.IntegerField()
    food_type = models.CharField(
        max_length=255, choices=constants.FOOD_TYPE_CHOICES)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
