import uuid

from django.contrib import auth
from django.db.models import Model, EmailField, CharField

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class Token(Model):
    email = EmailField()
    uid = CharField(default=uuid.uuid4, max_length=40)


class User(Model):
    email = EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    is_anonymous = False
    is_authenticated = True
