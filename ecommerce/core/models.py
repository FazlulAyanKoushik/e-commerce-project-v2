from autoslug import AutoSlugField

from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUID

from core.choices import UserGender
from core.utils import get_user_media_path_prefix


# Create your models here.
class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(self, full_name, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("User must have a phone number")

        user = self.model(
            full_name=full_name, phone_number=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, phone_number, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(
            full_name=full_name, phone_number=phone_number, password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModelWithUID, PermissionsMixin):
    """Users in the System"""

    phone_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from="full_name",
        unique=True,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
    )
    image = VersatileImageField(
        "Profile_image",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ("full_name",)

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"
