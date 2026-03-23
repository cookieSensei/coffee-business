from django.shortcuts import render, redirect
from .forms import OrderForm, OrderItemForm

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        item_form = OrderItemForm(request.POST)

        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save()

            order_item = item_form.save(commit=False)
            order_item.order = order
            order_item.save()

            return redirect('/')
    else:
        order_form = OrderForm()
        item_form = OrderItemForm()

    return render(request, 'orders/create_order.html', {
        'order_form': order_form,
        'item_form': item_form
    })