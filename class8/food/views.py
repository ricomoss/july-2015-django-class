from django.views.generic import ListView, DetailView, FormView, View
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from common import models as common_models
from common import wrappers
from food import models, forms, vendors


class MealListView(ListView):
    model = models.Meal

    @wrappers.retry
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


class MealEditView(DetailView, FormView):
    model = models.Meal
    template_name = 'food/meal_edit.html'
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


class VendorsView(View):
    template_name = 'food/vendor_list.html'
    close_template_name = 'food/vendor_close.html'
    form = forms.VendorsForm

    def get(self, request):
        return render(
            request, self.template_name, context={'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            vendor_handler = getattr(vendors, form.cleaned_data['vendor'])()
            resp = vendor_handler.handler(form.cleaned_data['action'])
            return render(
                request, self.close_template_name, context=resp)
        return render(request, self.template_name, context={'form': form})
