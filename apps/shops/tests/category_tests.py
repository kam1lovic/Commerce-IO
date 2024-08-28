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
