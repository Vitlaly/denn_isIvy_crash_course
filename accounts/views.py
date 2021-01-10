from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending
               }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products_all = Product.objects.all()
    return render(request, 'accounts/products.html', {'products_all': products_all})


def customer(request, id_customer):
    customer = Customer.objects.get(id=id_customer)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer,
               'orders': orders,
               'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)
