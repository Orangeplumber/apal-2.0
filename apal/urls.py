"""apal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', OfferView.as_view(), name='display_offers'),
    # path('home', OfferView.as_view(), name='display_offers'),
    path('en-us/paytm/', include('paytm.urls')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    url('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# the following will be the site map:
# 	|__www.apal.co.in
# 			|__ /home
# 			|__ /view_cart
# 			|__ /checkout
# 			|__ /contact_us
# 			|__ /about_us
# 			|__ /track_order
# 			|__ /signup
# 			|__ /login