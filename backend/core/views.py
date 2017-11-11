from django.views.generic import TemplateView
from .forms import LandingSearchForm


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['search_form'] = LandingSearchForm
        return context


class LoginPageView(TemplateView):
    template_name = 'login.html'


class SignUpPageView(TemplateView):
    template_name = 'signup.html'


class ProfilePageView(TemplateView):
    template_name = 'profile.html'
