from django.views.generic import ListView, DetailView
from .models import User, Tutor
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


class ProfilePageView(DetailView):
    template_name = 'accounts/profile.html'
    model = User
    context_object_name = 'user'

    def get_object(self, **kwargs):
        if 'pk' not in kwargs and not self.request.user.is_authenticated():
            raise Http404('User profile not found')
        if 'pk' not in kwargs:
            return get_object_or_404(self.model, email=self.request.user.email)
        return get_object_or_404(self.model, pk=kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(
            ProfilePageView, self).get_context_data(*args, **kwargs)
        context['job_create_form'] = JobCreateForm()
        return context
