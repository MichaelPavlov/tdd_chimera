from django.db.models import ForeignKey
from django.db.models import Model, TextField
from django.urls import reverse


class List(Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(Model):
    text = TextField(default='')
    list = ForeignKey(List, default=None)


