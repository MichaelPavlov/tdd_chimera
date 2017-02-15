from django.db.models import ForeignKey
from django.db.models import Model, TextField


class List(Model):
    pass


class Item(Model):
    text = TextField(default='')
    list = ForeignKey(List, default=None)
