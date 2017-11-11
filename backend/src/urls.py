from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(
        r'^api/v1/api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^', include('accounts.urls')),
    url(r'^', include('core.urls')),
    url(r'^', include('jobs.urls'))
]
