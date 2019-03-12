from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', home, name='home'),
    # url(r'^payment/', payment, name='payment'),
    url(r'^response/', response, name='response'),
]
