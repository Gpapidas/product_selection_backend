from django.contrib.auth import get_user_model

User = get_user_model()


def seed_test_users():
    """
    Seeds a test users for authentication tests.
    Ensures they are created only if they don't exist.
    Returns a list of dictionaries containing user instances.
    """

    users_data = [
        {"email": "test@productselection.com", "username": "testuser", "is_superuser": False, "is_staff": False}
    ]

    created_users = []

    for user_data in users_data:
        user, created = User.objects.get_or_create(
            email=user_data["email"],
            defaults={"username": user_data["username"], "is_superuser": user_data["is_superuser"],
                      "is_staff": user_data["is_staff"]}
        )
        if created:
            user.set_password("123test123")
            user.save()
        created_users.append({"object": user, "created": created})

    return created_users
