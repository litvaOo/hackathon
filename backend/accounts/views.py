from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView
from jobs.forms import JobCreateForm

from .forms import TutorProfileForm, UserForm
from .models import Tutor, User


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
        if (
            'pk' not in self.kwargs and
            not self.request.user.is_authenticated()
        ):
            raise Http404('User profile not found')
        if 'pk' not in self.kwargs:
            return get_object_or_404(self.model, email=self.request.user.email)
        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(
            ProfilePageView, self).get_context_data(*args, **kwargs)
        context['job_create_form'] = JobCreateForm()
        return context


class ProfileUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('accounts:self-profile')
    template_name = 'accounts/profile-edit.html'
    form_class = UserForm

    def get_object(self, **kwargs):
        if self.request.user.is_authenticated():
            return self.request.user
        raise Http404()

    def get_context_data(self, **kwargs):
        context = super(
            ProfileUpdateView, self).get_context_data(**kwargs)
        if hasattr(self.get_object(), 'tutors'):
            context['tutor_form'] = TutorProfileForm(
                instance=self.object.tutors.first()
            )
        return context

    def form_valid(self, form):
        if self.object.tutors.exists():
            tutor_form = TutorProfileForm({
                'about': self.request.POST.get('about')
            }, instance=self.object.tutors.first())
            if not tutor_form.is_valid():
                return self.render_to_response(
                    self.get_context_data(form=tutor_form)
                )
            tutor_form.save()

        if self.request.POST.get('teacher') == 'yes':
            Tutor.objects.create(
                user=self.request.user,
                about=self.request.POST.get('about')
            )

        return super(ProfileUpdateView, self).form_valid(form)
