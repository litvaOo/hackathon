from django.conf.urls import include, url
from django.contrib import admin
from jobs.views import CategoryAutocomplete

urlpatterns = [
    url(r'category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name="category-autocomplete"
    ),
]