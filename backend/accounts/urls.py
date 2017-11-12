from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(
        r'^results$', views.SearchResultsView.as_view(), name='search_results'
    ),
    url(
        r'^profile/(?P<pk>\d+)/$',
        views.ProfileTutorPageView.as_view(), name='profile'
    ),
    url(
        r'^profile/$',
        views.ProfileTutorPageView.as_view(), name='self-profile'
    ),
]
