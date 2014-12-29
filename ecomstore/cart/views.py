from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from checkout import checkout
from ecomstore import settings
import shoppingcart 

#def show_cart(request, template_name = "cart/cart.html"):
#    #cart_item_count = shoppingcart.cart_item_count(request)
#    cart_item_count = shoppingcart.cart_distinct_item_count(request)
#    page_title = "Shopping Cart"
#    return render_to_response(template_name, locals(), context_instance = RequestContext(request))

def show_cart(request, template_name = "cart/cart.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        print("postdata['submit'] = %s" % postdata['submit'])
        if postdata['submit'] == 'Remove':
            shoppingcart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            shoppingcart.update_cart(request)
        if postdata['submit'] == 'Checkout':
            print("Before get_checkout_url")
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    cart_items = shoppingcart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = shoppingcart.cart_subtotal(request)
    # for Google Checkout button
    merchant_id = settings.GOOGLE_CHECKOUT_MERCHANT_ID
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))
