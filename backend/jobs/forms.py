from django import forms
from jobs.models import Job


class JobCreateForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'price', 'price_per', 'category', 'tutor']
