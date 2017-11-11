from django import forms
from dal import autocomplete
from dal_select2 import widgets
from jobs.models import Category


class LandingSearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=widgets.ModelSelect2(url='jobs:category-autocomplete')
    )
