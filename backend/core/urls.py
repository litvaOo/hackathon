from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
    url(r'^signup/$', views.SignUpPageView.as_view(), name='signup'),
    url(r'^profile/$', views.ProfilePageView.as_view(), name='profile'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
]
