import pytest
from dotenv import load_dotenv
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from shops.models import Category, Country, Currency, Shop, ShopCategory
from users.models import Plan, User

load_dotenv()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_user():
    data = {
        'email': 'ccpy2024@gmail.com',
        'password': '1',
        'is_active': True,
        'is_superuser': False,
        'is_staff': True,
        'type': 'email'
    }

    return User.objects.create_user(**data)


@pytest.fixture
def another_user():
    data = {
        'email': 'asqar@gmail.com',
        'password': '2',
        'is_active': True,
        'is_superuser': False,
        'is_staff': True,
        'type': 'email'
    }
    return User.objects.create_user(**data)


@pytest.fixture
def anonim_user(client):
    return client


@pytest.fixture
def login_auth_user(api_client, auth_user):
    token, _ = Token.objects.get_or_create(user=auth_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client


@pytest.fixture
def login_another_user(api_client, another_user):
    token, _ = Token.objects.get_or_create(user=another_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client


@pytest.fixture
def country():
    return Country.objects.create(name='Uzbekistan', code='Uzb')


@pytest.fixture
def shop_category():
    return ShopCategory.objects.create(name='Texnika')


@pytest.fixture
def currency():
    return Currency.objects.create(name="so'm", order=1)


@pytest.fixture
def plan():
    return Plan.objects.create(name="Free", code='free', description='Tekin')


@pytest.fixture
def shop(auth_user, country, shop_category, currency, plan):
    return Shop.objects.create(
        name="Shop test",
        phone="+998997711310",
        phone_number=None,
        status="active",
        lat=7878700.12,
        lon=7878700.12,
        starts_at=None,
        ends_at=None,
        has_terminal=True,
        about_us="Biz haqimizda malumot",
        facebook="https://facebook.com",
        instagram="https://instagram.com",
        telegram="https://telegram.com",
        email="ccpy2024@gmail.com",
        address="Toshkent",
        is_new_products_show=True,
        is_popular_products_show=True,
        country=country,
        category=shop_category,
        currency=currency,
        owner=auth_user,
        plan=plan,
    )


@pytest.fixture
def shop2(another_user, country, shop_category, currency, plan):
    return Shop.objects.create(
        name="Shop2 test",
        phone="+998997711310",
        phone_number=None,
        status="active",
        lat=7878700.12,
        lon=7878700.12,
        starts_at=None,
        ends_at=None,
        has_terminal=True,
        about_us="Biz haqimizda malumot",
        facebook="https://facebook.com",
        instagram="https://instagram.com",
        telegram="https://telegram.com",
        email="ccpy2024@gmail.com",
        address="Toshkent",
        is_new_products_show=True,
        is_popular_products_show=True,
        country=country,
        category=shop_category,
        currency=currency,
        owner=another_user,
        plan=plan,
    )


@pytest.fixture
def category(shop):
    return Category.objects.create(
        name='Texnika',
        x='🤑',
        position=2,
        status='active',
        shop=shop
    )
