from django.urls import path
from shops.views.category import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
)
from shops.views.others import CountryListAPIView
from shops.views.shops import ShopListCreateAPIView, ShopRetrieveDestroyAPIView

app_name = 'shops'

urlpatterns = [
    # Shop
    path('shop', ShopListCreateAPIView.as_view(), name='create-list'),
    path('shop/<int:pk>/detail', ShopRetrieveDestroyAPIView.as_view(), name='retrieve-destroy'),

    # Category
    path('categories', CategoryListCreateAPIView.as_view(), name='category-create-list'),
    path('categories/<int:pk>/detail', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-destroy'),

    # Others
    path('countries', CountryListAPIView.as_view(), name='country-list'),

]
