from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(
        r'^results$', views.SearchResultsView.as_view(), name='search_results'
    ),
    url(
        r'^profile/(?P<pk>\d+)/$',
        views.ProfilePageView.as_view(), name='profile'
    ),
    url(
        r'^profile/$',
        views.ProfilePageView.as_view(), name='self-profile'
    ),
]
