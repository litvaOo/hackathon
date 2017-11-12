from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(
        r'^api/v1/api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'^', include('core.urls', namespace="core")),
    url(r'^', include('jobs.urls', namespace="jobs"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
