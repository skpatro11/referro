#!/bin/sh
echo "Welcome to referro!!"
python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='admin@example.com', name='admin', password='12345')" | python3 manage.py shell
echo "Super user created"