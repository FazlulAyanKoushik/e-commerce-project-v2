import pytest


@pytest.fixture
def create_admin_user(django_user_model):
    """
    This fixture creates an admin user.
        :param django_user_model:
        :return: User object of the admin user.
    """

    return django_user_model.objects.create_superuser(
        phone_number="01515620300",
        full_name="Admin User",
        password="admin"
    )
