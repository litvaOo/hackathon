from django import forms
from dal import autocomplete
from jobs.models import Category


class LandingSearchForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='core:category-autocomplete')
    )
    some_field = forms.CharField()