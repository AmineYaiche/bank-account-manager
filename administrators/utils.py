from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Administrator


def login_administrator(request, id_info):
    administrator = Administrator.objects.first()
    login(request, administrator.user)


def login_or_create_administrator(request, id_info):
    administrator = Administrator.objects.filter(google_id=id_info.get('sub'))
    if not administrator.exists():
        user = User(
            username=id_info.get('email'),
            email=id_info.get('email'),
            first_name=id_info.get('given_name'),
            last_name=id_info.get('family_name'),
            is_staff=True,
            is_superuser=True
        )
        user.set_unusable_password()
        user.save()
        Administrator.objects.create(google_id=id_info.get('sub'), user=user)

    login_administrator(request, id_info)

