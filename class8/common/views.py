from django.views.generic import ListView, DetailView

from common import models
from food import models as food_models


class ReviewListView(ListView):
    model = models.Review

    def get_queryset(self):
        qs = super().get_queryset()
        meal = food_models.Meal.objects.get(pk=self.kwargs['meal_id'])
        return qs.filter(meal=meal)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal = food_models.Meal.objects.get(pk=self.kwargs['meal_id'])
        context['meal'] = meal
        return context
