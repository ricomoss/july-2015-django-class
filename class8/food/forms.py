from django import forms
from django.forms.models import modelformset_factory

from food import models, vendors


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = "__all__"


ItemFormSet = modelformset_factory(
    models.Item, fields=('name', 'calories', 'portion_in_grams', 'food_type'),
    can_delete=True)


class VendorsForm(forms.Form):
    ACTION_CHOICES = (
        ('order', 'Make Order'),
        ('cancel_order', 'Cancel Order'),
        ('payment', 'Make Payment')
    )
    vendor = forms.ChoiceField(choices=vendors.VENDOR_OPTIONS)
    action = forms.ChoiceField(choices=ACTION_CHOICES)
