<<<<<<< HEAD
from . import views
from django.conf.urls import url

app_name = 'app'
urlpatterns = [
    url(r'^ngo_register/$', views.ngo_register, name='ngo_register'),
=======
from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
>>>>>>> a163af2da24ff6acf2ba491ca4aa14f5390a9663
]
