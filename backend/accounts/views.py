from django.shortcuts import render
from django.views.generic import ListView
from .models import Tutor

# Create your views here.

class SearchResultsView(ListView):
    template_name = "search.html"

    def get_queryset(self):
        queryset = Tutor.objects.all()
        return queryset

