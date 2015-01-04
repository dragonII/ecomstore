from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from catalog.models import Category, Product, ProductReview
from cart import shoppingcart
from catalog.forms import ProductAddToCartForm, ProductReviewForm
from stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW


def index(request, template_name="catalog/index.html"):
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug = category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def get_json_products(request):
    from django.core import serializers
    products = Product.active.all()
    json_products = serializers.serialize("json", products)
    return HttpResponse(json_products, content_type='application/javascript; charset=utf-8')
    

def show_product(request, product_slug, template_name = "catalog/product.html"):
    p = get_object_or_404(Product, slug = product_slug)
    from stats import stats
    stats.log_product_view(request, p) # add to product view
    categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart ... create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            shoppingcart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        # it's a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request = request, label_suffix = ':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()

    product_reviews = ProductReview.approved.filter(product = p).order_by('-date')
    review_form = ProductReviewForm()
    return render_to_response("catalog/product.html", locals(), context_instance = RequestContext(request))

@login_required
def test_review(request):
    print("In test_review function")

@login_required
@csrf_exempt
def add_review(request):
    print("In add_review")
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        print("Valid input");
        review = form.save(commit = False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug = slug)
        review.user = request.user
        review.product = product
        review.save()

        template = "catalog/product_review.html"
        html = render_to_string(template, {'review': review})
        response = simplejson.dumps({'success':'True', 'html':html})
    else:
        print("Invalid input")
        html = form.errors.as_ul()


        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')


#def show_product(request, product_slug, template_name="catalog/product.html"):
#    p = get_object_or_404(Product, slug=product_slug)
#    categories = p.categories.filter(is_active=True)
#    page_title = p.name
#    meta_keywords = p.meta_keywords
#    meta_description = p.meta_description
#    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

