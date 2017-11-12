from django.conf.urls import url
from jobs.views import CategoryAutocomplete, JobCreateView

urlpatterns = [
    url(
        r'category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name="category-autocomplete"
    ),
    url(
        r'job-create/$',
        JobCreateView.as_view(),
        name="job-create"
    )
]
