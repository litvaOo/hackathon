from dal import autocomplete
from jobs.models import Category, Job
from jobs.forms import JobCreateForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()
        return qs


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    # todo: изменить на правильную урлу
    success_url = reverse_lazy('accounts:self-profile')
