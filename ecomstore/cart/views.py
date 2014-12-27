from django.shortcuts import render_to_response
from django.template import RequestContext
import shoppingcart 

def show_cart(request, template_name = "cart/cart.html"):
    #cart_item_count = shoppingcart.cart_item_count(request)
    cart_item_count = shoppingcart.cart_distinct_item_count(request)
    page_title = "Shopping Cart"
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))
