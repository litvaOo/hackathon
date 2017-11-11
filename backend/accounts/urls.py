from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(
        r'^results$', views.SearchResultsView.as_view(), name='search_results'
    ),
]
