from django.views.generic import ListView, DetailView

from common import models as common_models
from food import models


class MealListView(ListView):
    model = models.Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = list()
        for meal in context['object_list']:
            context['data'].append({
                'meal': meal,
                'rating': common_models.Review.average_rating(meal),
                'reviews_count': meal.review_set.all().count(),
            })
        return context


class MealDetailView(DetailView):
    model = models.Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal = context['object']
        context['rating'] = common_models.Review.average_rating(meal)
        return context
