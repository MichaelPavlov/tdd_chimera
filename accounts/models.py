import uuid

from django.db.models import Model, EmailField, CharField


class Token(Model):
    email = EmailField()
    uid = CharField(default=uuid.uuid4, max_length=40)


class User(Model):
    email = EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    is_anonymous = False
    is_authenticated = True
