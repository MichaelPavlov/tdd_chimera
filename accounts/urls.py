from django.conf.urls import url

from accounts.views import send_login_email, login

urlpatterns = [
    url(r'send_login_email$', send_login_email, name='send-login-email'),
    url(r'login', login, name='login')
]
