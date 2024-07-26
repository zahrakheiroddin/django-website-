from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
class Order(models.Model):
    user_order =models.ForeignKey(User,related_name='order', on_delete=models.CASCADE,default= '1')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, default= '0')
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity

class wh_Order(models.Model):
    user_order =models.ForeignKey(User,related_name='wh_order', on_delete=models.CASCADE,default= '1')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, default= '0')
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    class Meta:
        ordering = ('-created',)
        verbose_name = 'سفارش همکاران'
        verbose_name_plural = 'سفارش های همکاران '
    def __str__(self):
        return f'wh_Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class wh_OrderItem(models.Model):
    order = models.ForeignKey(wh_Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='wh_order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity