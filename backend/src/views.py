from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class SignUpPageView(TemplateView):
    template_name = 'signup.html'


class ProfilePageView(TemplateView):
    template_name = 'profile.html'
