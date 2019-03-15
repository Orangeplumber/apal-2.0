from django.db import models
from shop.models import Product
from django.conf import settings


# HOSTEL_CHOICES= [
#     ('bhabha', 'Bhabha Bhavan'),
#     ('swami', 'Swami Vivekanand Bhavan'),
#     ('gajjar', 'Gajjar Bhavan'),
#     ('mtb', 'Mother Teresa Bhavan'),
#     ('nehru', 'Nehru Bhavan'),
#     ('tagore', 'Tagore Bhavan'),
#     ('sarabhai', 'Sarabhai Bhavan')
#     ]

# class Order(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60)
#     # last_name = models.CharField(max_length=60)
#     email = models.EmailField()
#     phone_no=models.CharField()
#     hostel = models.CharField(max_length=20)
#     wing = models.CharField(max_length=5)
#     room_no=models.PositiveIntegerField(default=1)
#     # postal_code = models.CharField(max_length=30)
#     # city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)

#     class Meta:
#         ordering = ('-created', )

#     def __str__(self):
#         return 'Order {}'.format(self.id)

#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_order', on_delete=models.CASCADE)
    order_id=models.CharField(max_length=7)
    phone_no=models.CharField(max_length=14)
    hostel = models.CharField(max_length=20)
    wing = models.CharField(max_length=5)
    room_no=models.PositiveIntegerField(default=1)
    delivery_time=models.CharField(max_length=10) #time duration of a day
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=60)
    # last_name = models.CharField(max_length=60)
    # email = models.EmailField()
    # address = models.CharField(max_length=150)
    # postal_code = models.CharField(max_length=30)
    # city = models.CharField(max_length=100)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

