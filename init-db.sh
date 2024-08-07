#! /bin/bash

python manage.py makemigrations
python manage.py migrate

echo "from users.models import User; User.objects.create_superuser('ccpy2024@gmail.com', '1')" | python manage.py shell

python manage.py loaddata service.json country.json currency.json languages.json shop_category.json plans.json plan_pricing.json quotas.json
plan_quotas.json


