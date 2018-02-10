from . import views
from django.conf.urls import url

app_name = 'app'
urlpatterns = [
    url(r'^ngo_register/$', views.ngo_register, name='ngo_register'),
    url(r'^user_register/$', views.register, name='register'),
    url(r'^user_login/$', views.login, name='login'),
    url(r'^user_logout/$', views.logout, name='logout'),
    url(r'^ngo_login/$', views.ngo_login, name='ngo_login'),
    url(r'^ngo_profile/(?P<pk>[0-9]+)/$', views.ngo_profile, name='ngo_profile'),
    url(r'^ngo_logout/$', views.ngo_logout, name='ngo_logout'),
]
