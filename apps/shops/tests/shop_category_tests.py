# TODO checked +

import pytest
from django.urls import reverse_lazy
from rest_framework import status


class TestShopCategoryUrl:
    def test_shop_category_list(self):
        url = reverse_lazy('shops:shop_category')
        assert url == '/api/v1/shop/shop-category'


class TestCurrencyUrl:
    def test_currency_list(self):
        url = reverse_lazy('shops:currency')
        assert url == '/api/v1/shop/currency'


class TestCountryUrl:
    def test_shop_category_list(self):
        url = reverse_lazy('shops:country')
        assert url == '/api/v1/shop/country'


@pytest.mark.django_db
class TestShopCategoryView:
    def test_shop_category_list_no_pagination(self, commerce_fixture, api_client, api_user1_client):
        allowed_http_methods = {'get', 'options', 'head'}
        url = reverse_lazy('shops:shop_category')

        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        response = api_user1_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()

        assert len(response) == 21
        keys = {'id', 'name'}
        assert keys == set(response[0].keys())

        response = api_user1_client.options(url)
        allowed_methods = response.headers.get('Allow').split(', ')
        allowed_methods = set(map(lambda i: i.lower(), allowed_methods))
        assert allowed_methods == allowed_http_methods
