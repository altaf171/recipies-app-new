
"""
Database Models

"""
from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """ Manager for user. """

    def create_user(self, email, password=None, **extra_fields):
        """ create, save and return new user """
        if not email:
            raise ValueError('User must have email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ creates and returns new superuser."""

        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the System.

    """
    email = models.EmailField(_("email"), max_length=254, unique=True)
    name = models.CharField(_("name"), max_length=50)
    is_active = models.BooleanField(_("is_active"), default=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
