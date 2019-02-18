from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_delivered', 'hostel', 'room_no', 'wing', 'phone_no', 'delivery_time', 'customer','paid', 'updated']
    list_filter = ['is_delivered', 'paid', 'created', 'updated']
    list_editable = ['paid', 'is_delivered']
    inlines = [OrderItemInline]
    # list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    # 'updated']
    # list_filter = ['paid', 'created', 'updated']
    # inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)
