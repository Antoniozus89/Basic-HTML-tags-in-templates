from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import title


def main_page(request):
    return render(request,'third_task/main_page.html')


def price_page(request):
    return render(request,'third_task/price.html')


def cart_page(request):
    return render(request,'third_task/cart_boilerplate.html')


