from django.contrib.auth import get_user_model
from main.utils import get_or_create_user_auth_with_email
import pytest

@pytest.mark.django_db
def test_get_or_create_user_auth_with_email():
    email = "test@test.com"
    User = get_user_model()
    user = get_or_create_user_auth_with_email(email)
    assert isinstance(user, User)
    assert user.email == email

    # Verify the user was saved to the database
    db_user = User.objects.get(email=email)
    assert db_user == user