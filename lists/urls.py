from django.conf.urls import url

from lists.views import view_list, new_list, my_lists

urlpatterns = [
    url(r'^new$', new_list, name='new-list'),
    url(r'^(\d+)$', view_list, name='view-list'),
    url(r'^users/(.+)$', my_lists, name='my-lists'),
]
