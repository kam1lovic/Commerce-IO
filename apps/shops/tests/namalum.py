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


# import pytest
# from django.urls import reverse_lazy
#
#
# class TestCategoryUrl:
#     def test_category_create_list(self):
#         url = reverse_lazy('shops:category-create-list')
#         assert url == '/api/v1/shop/category'
#
#     def test_category_retrieve_destroy(self):
#         url = reverse_lazy('shops:category-update-destroy', kwargs={'pk': 1})
#         assert url == '/api/v1/shop/shop/1/category'
#
#
# @pytest.mark.django_db
# class TestCategoryView:
#
#     def test_category_list(self, category):
#         print(category)
#         # assert ShopCategory.objects.count()
#
#     # @pytest.mark.django_db
#     # def test_create_category(self, auth_user, shop, anonim_user, login_auth_user):
#     #     url = reverse_lazy('shops:category-create-list')
#     #     data = {
#     #         "name": "Category test",
#     #         "emoji": "📚",
#     #         "description": "Bu test kategoriya",
#     #         "position": 1,
#     #         "shop": shop.id,
#     #     }
#     #     response_401 = anonim_user.post(url, data)
#     #     assert response_401.status_code == status.HTTP_401_UNAUTHORIZED
#     #
#     #     response_201 = login_auth_user.post(url, data)
#     #     res_data = response_201.data
#     #     assert response_201.data == status.HTTP_201_CREATED
#     #
#     #     assert res_data['name'] == data['name']
#     #     assert res_data['status'] == data['status']
#     #     assert res_data['description'] == data['description']
#     #     assert res_data['emoji'] == data['emoji']
#     #
#     # @pytest.mark.django_db
#     # def test_get_categories(self, auth_user, anonim_user, category, login_auth_user):
#     #     url = reverse_lazy('shops:category-create-list')
#     #     response_401 = anonim_user.get(url)
#     #     assert response_401.status_code == status.HTTP_401_UNAUTHORIZED
#     #
#     #     response_200 = login_auth_user.get(url)
#     #     res_data = response_200.data
#     #     assert response_200.status_code == status.HTTP_200_OK
#     #
#     #     assert res_data[0]['name'] == category.name
#     #     assert res_data[0]['status'] == category.status
#     #     assert res_data[0]['show_in_commerce'] == category.show_in_commerce
#     #
#     # @pytest.mark.django_db
#     # def test_category_detail(self, category, login_auth_user):
#     #     """Test the category detail view (retrieve, update, delete)."""
#     #     url = reverse_lazy('shops:category-update-destroy', kwargs={'pk': category.pk})
#     #     data = {
#     #         "name": "Category updated",
#     #         "emoji": "📖",
#     #         "description": "Bu test kategoriya update qilindi",
#     #         "position": 2,
#     #         "image": None,
#     #         "status": "inactive",
#     #         "show_in_commerce": False,
#     #     }
#     #
#     #     response = login_auth_user.put(url, data)
#     #     assert response.status_code == status.HTTP_200_OK
#     #
#     #     assert response.data['name'] == data['name']
#     #     assert response.data['status'] == data['status']
#     #     assert response.data['show_in_commerce'] == data['show_in_commerce']
#     #
#     #     response_delete = login_auth_user.delete(url)
#     #     assert response_delete.status_code == status.HTTP_204_NO_CONTENT
#     #
#     #     response_get_after_delete = login_auth_user.get(url)
#     #     assert response_get_after_delete.status_code == status.HTTP_404_NOT_FOUND
