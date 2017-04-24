from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import EmailField


class ListUserManager(BaseUserManager):
    def create_user(self, email):
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)


class ListUser(AbstractBaseUser, PermissionsMixin):
    email = EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'example@example.com'

    @property
    def is_active(self):
        return True
