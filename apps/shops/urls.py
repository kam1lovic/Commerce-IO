from django.urls import path

from shops.views import ShopListCreateAPIView, ShopRetrieveDestroyAPIView

urlpatterns = [
    path('shop', ShopListCreateAPIView.as_view(), name='create-list-create'),
    path('shop/<int:pk>/detail', ShopRetrieveDestroyAPIView.as_view(), name='destroy-shop'),

]
