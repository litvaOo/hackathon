from django.views.generic import ListView, DetailView
from .models import Tutor
from django.http import Http404
from django.shortcuts import get_object_or_404
from jobs.forms import JobCreateForm


class SearchResultsView(ListView):
    template_name = "search.html"
    context_object_name = "tutors"

    def get_queryset(self):
        if self.request.GET.get('category'):
            return Tutor.objects.filter(
                jobs__category=self.request.GET.get('category'))
        return Tutor.objects.all()


class ProfileTutorPageView(DetailView):
    template_name = 'profile.html'
    model = Tutor

    def get_object(self, **kwargs):
        if 'pk' not in kwargs and not self.request.user.is_authenticated():
            raise Http404('Tutor profile not found')
        if 'pk' not in kwargs:
            return get_object_or_404(self.model, user=self.request.user)
        return get_object_or_404(self.model, user=kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(
            ProfileTutorPageView, self).get_context_data(*args, **kwargs)
        context['job_create_form'] = JobCreateForm
        return context
