from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from paytm import Checksum
from paytm.views import payment
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.conf import settings
from django.forms import formset_factory


@login_required
def order_create(request):
    cart = Cart(request)
    data_dict={}
    if request.method == 'POST':
        data_dict={}
        for key in request.POST:
                data_dict[key] = request.POST[key]
        OrderFormSet = formset_factory(OrderCreateForm, extra=data_dict['form-TOTAL_FORMS'])
        formset=OrderFormSet(request.POST)
        # form = OrderCreateForm(request.POST)
        if formset.is_valid():
            # order=Order.objects.create(customer=request.user, hostel=data_dict['hostel'], wing=data_dict['wing'], room_no=data_dict['room_no'], phone_no=data_dict['phone_no'], delivery_time=data_dict['delivery_time'])
            # orders = formset.save(commit=False)
            orders_id=[]
            for order in formset:
                order_ID = Checksum.__id_generator__()
                order.instance.order_id=order_ID
                order.instance.customer = request.user
                order.instance.save()

                # order.customer=request.user
                # order.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order.instance,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                orders_id.append(order.instance.id)
            cart.clear()
        order=Order.objects.get(order_id=order_ID)
        bill_amount=order.get_total_cost()
        return payment(request, order_ID, bill_amount)
        # return render(request, 'orders/order/created.html', {'orders': orders_id})
    else:
        OrderFormSet = formset_factory(OrderCreateForm, extra=1)
        formset = OrderFormSet()
    return render(request, 'orders/order/create.html', {'formset': formset})



# def create(request):
#     AddressInlineFormSet = inlineformset_factory(Address, Store, form=AddressForm)

#      if request.method == 'POST':
#          storeForm = StoreForm(request.POST)

#          if storeForm.is_valid():
#              new_store = storeForm.save()
#              addressInlineFormSet = AddressInlineFormSet(request.POST, request.FILES, instance=new_store)

#              if addressInlineFormSet.is_valid():
#                 addressInlineFormSet.save()
#                 return HttpResponseRedirect(reverse('some_happy_customer_url'))

#              else:
#                 classificationformset = ClassificationInlineFormSet(request.POST, request.FILES, instance=new_store)
#      else:
#           addressInlineFormSet = AddressInlineFormSet()
#           storeForm = StoreForm()
#      return render(request, 'create.html', locals())