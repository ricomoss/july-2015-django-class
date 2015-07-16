from django import forms
from django.forms.models import modelformset_factory

from food import models


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = "__all__"


ItemFormSet = modelformset_factory(
    models.Item, fields=('name', 'calories', 'portion_in_grams', 'food_type'),
    can_delete=True)