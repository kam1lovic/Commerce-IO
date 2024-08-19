#! /bin/bash

python manage.py makemigrations
python manage.py migrate


python manage.py loaddata service.json
python manage.py loaddata country.json
python manage.py loaddata currency.json
python manage.py loaddata languages.json
python manage.py loaddata shop_category.json
python manage.py loaddata plans.json plan_pricing.json
python manage.py loaddata quotas.json
python manage.py loaddata plan_quotas.json


