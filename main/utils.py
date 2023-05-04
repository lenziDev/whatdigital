from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

def get_or_create_user_auth_with_email(email):
    try:
        user = get_user_model().objects.get(username=email)
    except get_user_model().DoesNotExist:
        user = get_user_model().objects.create(
            username = email
        )
    try:
        token = Token.objects.get(user=user)
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)
    return user, token