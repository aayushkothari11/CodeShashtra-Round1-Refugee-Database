from . import views
from django.conf.urls import url

app_name = 'app'
urlpatterns = [
    url(r'^ngo_register/$', views.ngo_register, name='ngo_register'),
]
