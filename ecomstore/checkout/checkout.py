import google_checkout
from cart import shoppingcart
from models import Order, OrderItem
from forms import CheckoutForm
import authnet
from ecomstore import settings
from django.core import urlresolvers
import urllib

# returns the URL from the checkout module for cart
def get_checkout_url(request):
    #return google_checkout.get_checkout_url(request)
    return urlresolvers.reverse('checkout')


def process(request):
    # Transaction results
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'
    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number', '')
    exp_month = postdata.get('credit_card_expire_month', '')
    exp_year = postdata.get('credit_card_expire_year', '')
    exp_date = exp_month + exp_year
    cvv = postdata.get('credit_card_cvv', '')
    amount = shoppingcart.cart_subtotal(request)
    results = {}
    response = authnet.do_auth_capture(amount = amount,
                                       card_num = card_num,
                                       exp_date = exp_date,
                                       card_cvv = cvv)
    if response[0] == APPROVED:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        result = {'order_number' : order.id, 'message':'' }
    if response[0] == DECLINED:
        results = {'order_number':0, 'message':'There is a problem with you credit card'}
    if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
        results = {'order_number':0, 'message':'Error processing your order.'}
    #create_order(request, transaction_id = 1024)
    return results

def create_order(request, transaction_id):
    order = Order()
    checkout_form = CheckoutForm(request.POST, instance = order)
    order = checkout_form.save(commit = False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()
    # if the order save succeeded
    if order.pk:
        cart_items = shoppingcart.get_cart_items(request)
        for ci in cart_items:
            # create order item for each cart item
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()
        # all set, empty card
        shoppingcart.empty_cart(request)
    # return the new order object
    return order
