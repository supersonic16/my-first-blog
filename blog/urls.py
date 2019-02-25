from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^hello', views.first_entry, name='1'),
    url(r'^get_name/$', views.get_name, name='get_name')
]
