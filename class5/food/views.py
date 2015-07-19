from datetime import datetime

from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from common import models as common_models
from food import models, forms


class MealListView(ListView):
    model = models.Meal

    def get_context_data(self, **kwargs):
        start = datetime.now()
        context = super().get_context_data(**kwargs)
        context['data'] = list()
        for meal in context['object_list']:
            context['data'].append({
                'meal': meal,
                'rating': common_models.Review.average_rating(meal),
                'reviews_count': meal.review_set.all().count(),
            })
        print('{} sec to return view'.format(datetime.now() - start))
        return context


class MealDetailView(DetailView):
    model = models.Meal

    def get_context_data(self, **kwargs):
        start = datetime.now()
        context = super().get_context_data(**kwargs)
        meal = context['object']
        context['rating'] = common_models.Review.average_rating(meal)
        print('{} sec to return view'.format(datetime.now() - start))
        return context


class MealEditView(DetailView, FormView):
    model = models.Meal
    template_name = "food/meal_edit.html"
    form_class = forms.ItemFormSet
    formset_model_class = models.Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal = context['object']
        context['meal'] = meal
        context['formset'] = self.form_class(
            queryset=models.Item.objects.filter(meal=meal))
        return context

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        meal = self.model.objects.get(pk=kwargs.get('pk'))
        if formset.is_valid():
            formset.save()
            for obj in formset.new_objects:
                obj.meal_set.add(meal)
        return redirect(reverse('food:detail', kwargs=kwargs))
