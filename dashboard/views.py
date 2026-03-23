from django.shortcuts import render
from django.db.models import Sum
from orders.models import Order, OrderItem
from expenses.models import Expense
from inventory.models import Item
from repairs.models import RepairRequest

def dashboard_view(request):
    try:
        total_sales = OrderItem.objects.aggregate(Sum('price'))['price__sum'] or 0
    except:
        total_sales = 0

    try:
        total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    except:
        total_expenses = 0

    profit = total_sales - total_expenses

    total_items = Item.objects.count()
    total_orders = Order.objects.count()
    total_repairs = RepairRequest.objects.count()

    return render(request, 'dashboard.html', {
        'sales': total_sales,
        'expenses': total_expenses,
        'profit': profit,
        'total_items': total_items,
        'total_orders': total_orders,
        'total_repairs': total_repairs,
    })