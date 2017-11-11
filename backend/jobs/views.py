from django.shortcuts import render
from dal import autocomplete
from jobs.models import Category 

class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()

        return qs
# Create your views here.
