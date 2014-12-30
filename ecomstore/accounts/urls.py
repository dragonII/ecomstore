from django.conf.urls import patterns, include, url
from ecomstore import settings

urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'register', 
        { 'template_name': 'registration/register.html', 'SSL' : settings.ENABLE_SSL }, 'register'),
    url(r'^my_account/$', 'my_account', 
        {'template_name': 'registration/my_account.html'}, 'my_account'),
    #url(r'^order_info/$', 'order_info', 
    #    {'template_name': 'registration/order_info.html'}, 'order_info'),
    url(r'^order_details/(?P<order_id>[-\w]+)$', 'order_details', 
        {'template_name': 'registration/order_dtails.html'}, 'order_dtails'),
    )

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', 
        {'template_name': 'registration/login.html', 'SSL' : settings.ENABLE_SSL }, 'login'),
    )
