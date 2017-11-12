from django.contrib.auth import get_user_model
from django import forms


class SignupForm(forms.Form):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'city',
            'country',
            'avatar'
        ]

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']
        user.country = self.cleaned_data['country']
        user.avatar = self.cleaned_data['avatar']
        user.save()
