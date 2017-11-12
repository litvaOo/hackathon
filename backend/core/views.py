from django.views.generic import TemplateView
from jobs.models import Category


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:6]
        return context


class LoginPageView(TemplateView):
    template_name = 'login.html'


class SignUpPageView(TemplateView):
    template_name = 'signup.html'
