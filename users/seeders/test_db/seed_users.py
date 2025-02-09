from django.contrib.auth import get_user_model

User = get_user_model()


def seed_test_users():
    """
    Seeds a test user and a test superuser for authentication tests.
    Ensures they are created only if they don't exist.
    Returns a dictionary containing the user instances.
    """

    users = {}

    # Create standard test user
    user, created = User.objects.get_or_create(
        email="test@productselection.com",
        defaults={"username": "testuser", "is_superuser": False, "is_staff": False}
    )
    if created:
        user.set_password("123test123")
        user.save()
    users["test_user"] = user

    return users
