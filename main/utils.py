from django.contrib.auth import get_user_model
from django.conf import settings

def get_or_create_user_auth_with_email(email):
    try:
        user = get_user_model().objects.get(username=email)
    except get_user_model().DoesNotExist:
        user = get_user_model().objects.create(
            username = email
        )
    
    return user