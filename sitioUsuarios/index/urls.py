from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^user/(?P<param_pk>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^uploadfile$', views.uploadFile, name='uploadfile'),
]
