from django.conf.urls import include, url
from django.contrib import admin
from src.views import (HomePageView, LoginPageView, ProfilePageView,
                       SignUpPageView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(
        r'^api/v1/api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^login/$', LoginPageView.as_view(), name='login'),
    url(r'^signup/$', SignUpPageView.as_view(), name='signup'),
    url(r'^profile/$', ProfilePageView.as_view(), name='profile'),
    url(r'^$', HomePageView.as_view(), name='home')
]
