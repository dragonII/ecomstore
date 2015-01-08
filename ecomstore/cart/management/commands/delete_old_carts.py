from django.core.management.base import NoArgsCommand
from cart import shoppingcart

class Command(NoArgsCommand):
    help = "Delete shopping cart items more than SESSION_AGE_DAYS days old"
    def handle_noargs(self, **options):
        shoppingcart.remove_old_cart_items()
