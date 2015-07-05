from django.views.generic import ListView, DetailView

from food import models


class MealListView(ListView):
    model = models.Meal


class MealDetailView(DetailView):
    model = models.Meal
