from django.contrib.auth.models import User
from django_dynamic_fixture import G


def login_user(test_case, user, password):
    test_case.client.logout()
    test_case.client.login(username=user.username, password=password)


def create_logged_in_user(test_case, username='mary', password='marypassword'):
    user = G(User)
    user.username = username
    user.set_password(password)
    user.save()
    login_user(test_case, user, password)
    return user