# import pytest
# from django.urls import reverse_lazy
# from rest_framework import status
#
# pytestmark = pytest.mark.django_db
#
#
# class TestShopUrl:
#
#     def test_list_create_shop(self):
#         url = reverse_lazy('shops:list-create')
#         assert url == '/api/v1/shop/shop'
#
#     def test_detail_shop(self):
#         url = reverse_lazy('shops:shop-detail', kwargs={'pk': 1})
#         assert url == '/api/v1/shop/shop/1/detail'
#
#
# class TestShopView:
#
#     def test_create_shop(self, shop, user1, country, currency, shop_category, client, login_user1):
#         url = reverse_lazy('shops:create-list')
#         data = {
#             "name": "Shop test",
#             "phone": "+998997711310",
#             "phone_number": "8989898",
#             "status": "active",
#             "lat": 7878700.12,
#             "lon": 7878700.12,
#             "has_terminal": True,
#             "about_us": "Biz haqimizda malumot",
#             "facebook": "https://facebook.com",
#             "instagram": "https://instagram.com",
#             "telegram": "https://telegram.com",
#             "email": "tohir@gmail.com",
#             "address": "Toshkent",
#             "is_new_products_show": True,
#             "is_popular_products_show": True,
#             "country": country.id,
#             "category": shop_category.id,
#             "currency": currency.id,
#             "owner": user1.id,
#         }
#         response = client.post(url, data)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#
#         response = login_user1.post(url, data)
#         res_data = response.data
#         assert response.status_code == status.HTTP_201_CREATED
#
#         assert res_data['name'] == shop.name
#         assert res_data['phone'] == shop.phone
#         assert shop.owner_id == user1.id
#         assert shop.owner.email == user1.email
#         assert shop.owner.type == user1.type
#         assert res_data['category'] == shop_category.id
#         assert res_data['currency'] == shop.currency.id
#
#     def test_get_shops(self, user1, client, shop, shop2, login_user1):
#         url = reverse_lazy('shops:create-list')
#         response = client.get(url)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         response = login_user1.get(url)
#         res_data = response.data
#         assert response.status_code == status.HTTP_200_OK
#         assert len(res_data) == 1
#
#     def test_shop_detail(self, user1, client, country, currency, shop, login_user1, login_user2):
#         url = reverse_lazy('shops:retrieve-update-destroy', kwargs={'pk': shop.pk})
#         data = {
#             "name": "Shop update put",
#             "phone": "+998997711310",
#             "phone_number": "8989898",
#             "status": "active",
#             "lat": 7878700.12,
#             "lon": 7878700.12,
#             "has_terminal": True,
#             "about_us": "Biz haqimizda malumot",
#             "facebook": "https://facebook.com",
#             "instagram": "https://instagram.com",
#             "telegram": "https://telegram.com",
#             "email": "tohir@gmail.com",
#             "address": "Toshkent",
#             "is_new_products_show": True,
#             "is_popular_products_show": True,
#             "country": country.id,
#             "currency": currency.id,
#         }
#         response = client.get(url)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#
#         response = login_user1.get(url)
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['name'] == shop.name
#
#         response = login_user2.get(url)
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#
#         response = login_user1.put(url, data)
#         assert response.status_code == status.HTTP_200_OK
#         shop.refresh_from_db()
#         assert response.data['name'] == shop.name
#         assert user1 == shop.owner
#
#         response = login_user1.patch(url, {"name": "Patch"})
#         assert response.status_code == status.HTTP_200_OK
#         shop.refresh_from_db()
#         assert shop.name == response.data['name']
#         response = login_user1.delete(url)
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#
#         response = login_user1.get(url)
#         assert response.status_code == status.HTTP_404_NOT_FOUND
