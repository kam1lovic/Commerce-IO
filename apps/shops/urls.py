from django.urls import path

from shops.views.shops import ShopListCreateAPIView, ShopRetrieveDestroyAPIView

app_name = 'shops'

urlpatterns = [
    path('shop', ShopListCreateAPIView.as_view(), name='create-list'),
    path('shop/<int:pk>/detail', ShopRetrieveDestroyAPIView.as_view(), name='retrieve-destroy'),

]
