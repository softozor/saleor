from django.conf import settings

import graphene
from graphene_django.debug import DjangoDebug

from .account.schema import AccountMutations, AccountQueries
from .checkout.schema import CheckoutMutations, CheckoutQueries
from .core.schema import CoreMutations
from .discount.schema import DiscountMutations, DiscountQueries
from .menu.schema import MenuMutations, MenuQueries
from .order.schema import OrderMutations, OrderQueries
from .page.schema import PageMutations, PageQueries
from .payment.schema import PaymentMutations, PaymentQueries
from .product.schema import ProductMutations, ProductQueries
from .shipping.schema import ShippingMutations, ShippingQueries
from .shop.schema import ShopMutations, ShopQueries


class Query(AccountQueries, CheckoutQueries, DiscountQueries, MenuQueries,
            OrderQueries, PageQueries, PaymentQueries, ProductQueries,
            ShippingQueries, ShopQueries):
    node = graphene.Node.Field()
    # Only add the __debug field to root query if GRAPHENE_DEBUG is True
    if settings.GRAPHENE_DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')



class Mutations(AccountMutations, CheckoutMutations, CoreMutations,
                DiscountMutations, MenuMutations, OrderMutations,
                PageMutations, PaymentMutations, ProductMutations,
                ShippingMutations, ShopMutations):
    pass


schema = graphene.Schema(Query, Mutations)
