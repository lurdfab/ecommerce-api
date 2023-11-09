from rest_framework import routers
from user.api import *
from products.api import *
from orders.api import *
from cart.api import *
from payments.api import *

router = routers.DefaultRouter(trailing_slash=True)
#user
router.register(r"register", RegisterViewSet),
router.register(r"login", LoginViewSet),
router.register(r"userprofile", UserProfileViewSet),
#products
router.register(r"category", CategoryViewSet),
router.register(r"brand", BrandViewSet),
router.register(r"product", ProductViewSet),
#review
router.register(r'reviews', ReviewViewSet)
#orders
router.register(r"order", OrderViewSet)
#cart
router.register(r"cart", CartItemViewSet)
#payment
router.register(r"order/(?P<id>\d+)/payment", PaymentViewSet)
#wishlist
router.register(r"wishlist", WishListViewSet)
#search
router.register(r"search", ProductSearchViewSet)


