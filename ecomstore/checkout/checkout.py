import google_checkout

def get_checkout_url(request):
    print("In get_checkout_url")
    return google_checkout.get_checkout_url(request)
