from django.shortcuts import render

from django.urls import reverse
from django.views import generic
import re
from django.http import HttpResponseRedirect

from .models import Pack

class OfferView(generic.ListView):
	template_name='home/index.html'
	context_object_name='pack_list'

	def get_queryset(self):
		"""Return the last five pubished question."""
		return Pack.objects.order_by('stock')[:]

# def add_to_cart(request, product_id, quantity):
#     product = Pack.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.add(product, product.unit_price, quantity)

# def remove_from_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.remove(product)

# def get_cart(request):
#     return render_to_response('cart.html', dict(cart=Cart(request)))
