from django.conf.urls import patterns, include, url
from ecomstore import settings

urlpatterns = patterns('checkout.views',
        url(r'^$', 'show_checkout', { 'template_name': 'checkout/checkout.html', 'SSL' : settings.ENABLE_SSL }, 'checkout'),
        url(r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html', 'SSL' : settings.ENABLE_SSL }, 'checkout_receipt'),
        )
