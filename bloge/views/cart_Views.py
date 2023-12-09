# from math import ceil
from django.shortcuts import render, redirect
# from realestate.cart_operation_session import CartSession  # noqa: F401
from ..models import Contact, Product  # noqa: F401
from django.core.exceptions import ValidationError  # noqa: F401


# HttpResponse
# from django.http import HttpResponse



# delete from cart
def delete_from_cart(request):
    return redirect("Home")


def update_cart(request):
    return render(request, "store/cart_summary.html")



# cart summary
def cart_summary(request):
    return render(request, "store/cart_summary.html")
