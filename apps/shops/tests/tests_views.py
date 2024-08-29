import pytest
from django.core.management import call_command
from django.urls import reverse_lazy
from rest_framework import status

from shops.models import Shop, Country, Currency, ShopCategory, Category


@pytest.mark.django_db
class TestViews:
    @pytest.fixture(autouse=True)
    def common_fixtures(self):
        call_command("loaddata", "shop_category", "country", "currency")
        self.shop_category_url = reverse_lazy('shops:shop_category')
        self.shop_url = reverse_lazy('shops:shop_list')
        self.currency_url = reverse_lazy('shops:shop_category')
        self.country_url = reverse_lazy('shops:country')

    @pytest.mark.parametrize("url_name, keys, count, allowed_methods", [
        ('shop_category_url', {'id', 'name'}, 21, {'get', 'options', 'head'}),
        ('currency_url', {'id', 'name', 'order'}, 87, {'get', 'options', 'head'}),
        ('country_url', {'count', 'next', 'previous', 'results', 'sort_fields'}, 5, {'get', 'options', 'head'}),
        ('shop_url', {'count', 'results'}, 2, {'get', 'post', 'options', 'head'}),
    ])
    def test_url_data_with_http_methods(self, api_client, api_user1_client, url_name, keys, count, allowed_methods):
        url = getattr(self, url_name)
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        response = api_user1_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()

        assert keys == set(response[0])
        assert len(response) == count

        response = api_user1_client.options(url)
        _allowed_methods = response.headers.get('Allow').split(', ')
        _allowed_methods = set(map(lambda i: i.lower(), _allowed_methods))
        assert _allowed_methods == allowed_methods

    def test_country_list_with_pagination(self, api_client, api_user1_client):
        query = {
            'size': 100000
        }
        response = api_user1_client.get(self.country_url, query)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()

        assert len(response['results']) == 249 == response['count']
        assert set(response['results']) == {'id', 'name'}

    def test_shop_list_data(self, api_client, api_user1_client, api_user2_client, shop11):
        """
        api_user1_client - login qilingan user (user1)
        shop1 - user1 ning default shopi
        """
        shop_count = Shop.objects.filter(owner=shop11.owner).count()
        response = api_user1_client.get(self.shop_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response['results']) == shop_count

    def test_shop_create(self, api_client, api_user1_client, api_user2_client, shop11):
        _country = Country.objects.order_by('?').first()
        _currency = Currency.objects.order_by('?').first()
        _shop_category = ShopCategory.objects.order_by('?').first()

        owner = shop11.owner
        data = {
            "languages": ["ru"],
            "shop_category_id": _shop_category.id,
            "phone_number": "+998977736531",
            "shop_currency_id": _currency.id,
            "name": "Yangi Shop",
            "country_id": _country.id
        }
        response = api_user1_client.post(self.shop_url, data)
        assert response.status == status.HTTP_201_CREATED
        _shop = Shop.objects.filter(owner=owner).order_by('-id').first()
        owner.refresh_from_db()
        assert owner.default_shop == _shop
        assert _shop.name == data['name']

    def test_category_list_search_by_name(self, api_user1_client, shop11):
        key = 'computer'
        search_count = Category.objects.filter(name__icontains=key, shop=shop11).count()
        query = {
            'search': key
        }
        response = api_user1_client.get(self.shop_category_url, query)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert len(response) == search_count
