from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['hostel', 'wing', 'room_no', 'phone_no', 'delivery_time']
        # fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
