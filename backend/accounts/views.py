from django.views.generic import ListView
from .models import Tutor
from jobs.models import Category
#from django.shortcuts import get_object_or_404


class SearchResultsView(ListView):
    template_name = "search.html"
    context_object_name = "tutors"

    def get_queryset(self):
        if self.request.GET.get('category'):
            return Tutor.objects.filter(jobs__category=self.request.GET.get('category'))
        return Tutor.objects.all()
