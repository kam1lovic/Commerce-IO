import pytest
from django.urls import reverse_lazy
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestShopUrl:
    def test_shop_create_list(self):
        url = reverse_lazy('shops:create-list')
        assert url == '/api/v1/shops/shop'

    def test_shop_retrieve_destroy(self):
        url = reverse_lazy('shops:retrieve-destroy', kwargs={'pk': 1})
        assert url == '/api/v1/shops/shop/1/detail'


class TestShopView:
    @pytest.mark.django_db
    def test_create_shop(self, shop, auth_user, country, currency, shop_category, anonim_user, login_auth_user):
        url = reverse_lazy('shops:create-list')
        data = {
            "name": "Shop test",
            "phone": "+998997711310",
            "phone_number": "8989898",
            "status": "active",
            "lat": 7878700.12,
            "lon": 7878700.12,
            "has_terminal": True,
            "about_us": "Biz haqimizda malumot",
            "facebook": "https://facebook.com",
            "instagram": "https://instagram.com",
            "telegram": "https://telegram.com",
            "email": "tohir@gmail.com",
            "address": "Toshkent",
            "is_new_products_show": True,
            "is_popular_products_show": True,
            "country": country.id,
            "category": shop_category.id,
            "currency": currency.id,
            "owner": auth_user.id,
        }
        response_401 = anonim_user.post(url, data)
        assert response_401.status_code == status.HTTP_401_UNAUTHORIZED

        response_201 = login_auth_user.post(url, data)
        res_data = response_201.data
        assert response_201.status_code == status.HTTP_201_CREATED

        assert res_data['name'] == shop.name
        assert res_data['phone'] == shop.phone
        assert shop.owner_id == auth_user.id
        assert shop.owner.email == auth_user.email
        assert shop.owner.type == auth_user.type
        assert res_data['category'] == shop_category.id
        assert res_data['currency'] == shop.currency.id

    @pytest.mark.django_db
    def test_get_shops(self, auth_user, anonim_user, shop, login_auth_user):
        url = reverse_lazy('shops:create-list')
        response_401 = anonim_user.get(url)
        assert response_401.status_code == status.HTTP_401_UNAUTHORIZED
        response_200 = login_auth_user.get(url)
        res_data = response_200.data
        assert response_200.status_code == status.HTTP_200_OK
        assert auth_user == shop.owner
        assert res_data[0]['name'] == shop.name
        assert res_data[0]['status'] == shop.status

    @pytest.mark.django_db
    def test_shop_detail(self, country, currency, shop, auth_user, shop_category, login_auth_user):
        """Test the shop detail view (retrieve, update, delete)."""
        url = reverse_lazy('shops:retrieve-destroy', kwargs={'pk': shop.pk})
        data = {
            "name": "Shop update",
            "phone": "+998997711310",
            "phone_number": "8989898",
            "status": "active",
            "lat": 7878700.12,
            "lon": 7878700.12,
            "has_terminal": True,
            "about_us": "Biz haqimizda malumot",
            "facebook": "https://facebook.com",
            "instagram": "https://instagram.com",
            "telegram": "https://telegram.com",
            "email": "ccpy2024@gmail.com",
            "address": "Toshkent",
            "is_new_products_show": True,
            "is_popular_products_show": True,
            "country": country.id,
            "currency": currency.id,
            "category": shop_category.id
        }

        # Update the shop
        response = login_auth_user.put(url, data)
        assert response.status_code == status.HTTP_200_OK

        # Verify that all fields are updated correctly
        assert response.data['name'] == data['name']
        assert response.data['phone'] == data['phone']
        assert response.data['phone_number'] == data['phone_number']
        assert response.data['status'] == data['status']
        assert response.data['lat'] == data['lat']
        assert response.data['lon'] == data['lon']
        assert response.data['has_terminal'] == data['has_terminal']
        assert response.data['about_us'] == data['about_us']
        assert response.data['facebook'] == data['facebook']
        assert response.data['instagram'] == data['instagram']
        assert response.data['telegram'] == data['telegram']
        assert response.data['email'] == data['email']
        assert response.data['address'] == data['address']
        assert response.data['is_new_products_show'] == data['is_new_products_show']
        assert response.data['is_popular_products_show'] == data['is_popular_products_show']
        assert response.data['country']['id'] == data['country']
        assert response.data['currency'] == data['currency']
        assert response.data['category'] == data['category']
        response_get = login_auth_user.get(url)
        assert response_get.status_code == status.HTTP_200_OK
        assert response_get.data == response.data

        response_delete = login_auth_user.delete(url)
        assert response_delete.status_code == status.HTTP_204_NO_CONTENT

        # Ensure the shop no longer exists
        response_get_after_delete = login_auth_user.get(url)
        assert response_get_after_delete.status_code == status.HTTP_404_NOT_FOUND
