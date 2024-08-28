from django.urls import path

from shops.views.categories import CategoryListCreateAPIView, CategoryUpdateDestroyAPIView
from shops.views.others import CountryListAPIView
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
    path('category', CategoryListCreateAPIView.as_view(), name='category-create-list'),
    path('shop/<int:pk>/category', CategoryUpdateDestroyAPIView.as_view(), name='category-update-destroy'),

    # Others
    path('countries', CountryListAPIView.as_view(), name='country-list'),

]
