from django.conf import settings
from django.db.models import ForeignKey
from django.db.models import Model, TextField
from django.urls import reverse


class List(Model):
    owner = ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('lists:view-list', args=[self.id])


class Item(Model):
    text = TextField(default='')
    list = ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
