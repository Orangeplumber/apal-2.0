from django.conf.urls import url
from . import views

app_name = 'offers'

urlpatterns = [
    url(r'^$', views.offer_list, name='offer_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.offer_detail, name='offer_detail'),
]