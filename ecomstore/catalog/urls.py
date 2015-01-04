from django.conf.urls import patterns, url

urlpatterns = patterns('catalog.views',
        url(r'^$', 'index', { 'template_name' :'catalog/index.html' }, 'catalog_home'),
        url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', { 'template_name' :'catalog/category.html' }, 'catalog_category'),
        url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', { 'template_name' : 'catalog/product.html'}, 'catalog_product'),
        url(r'^get_json_products/$', 'get_json_products'),
        url(r'^review/product/add/$', 'add_review'),
        url(r'^review/product/test/$', 'test_review'),
        )

