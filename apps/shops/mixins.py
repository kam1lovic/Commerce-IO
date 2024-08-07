from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404

from shops.models import Shop


class ShopMixin:
    def get_shop(self):
        user = self.request.user
        self.shop = get_object_or_404(Shop, pk=self.kwargs.get("shop_pk"), owner=user)
        if not self.shop:
            raise NotFound("Shop not found.")
        return self.shop
