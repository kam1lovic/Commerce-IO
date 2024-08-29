from django.urls import path

from shops.views.categories import CategoryListAPIView
from shops.views.others import CountryListAPIView, CurrencyListAPIView
from shops.views.shops import (
    ShopListCreateAPIView,
    ShopRetrieveUpdateDestroyAPIView,
)

app_name = 'shops'

urlpatterns = [
    # Shop
    path('shop', ShopListCreateAPIView.as_view(), name='create-list'),
    path('shop/<int:pk>/detail', ShopRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy'),

    # Category
    path('shop-category', CategoryListAPIView.as_view(), name='shop_category'),

    # Others
    path('country', CountryListAPIView.as_view(), name='country'),
    path('currency', CurrencyListAPIView.as_view(), name='currency'),

]
