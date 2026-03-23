from django import forms
from .models import Order, OrderItem
from inventory.models import Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity', 'price']