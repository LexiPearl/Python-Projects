from django.conf.urls import url
from views import index, process, delete, login, logout
app_name="loginAndRegistration"
urlpatterns = [
    url(r'^$', index, name="loginAndRegistration_index"),
    url(r'^process$', process, name="loginAndRegistration_process"),
    # url(r'^dashboard$', dashboard, name="loginAndRegistration_success"),
    url(r'^delete/(?P<id>\d+)$', delete, name="loginAndRegistration_delete"),
    url(r'^login$', login, name="loginAndRegistration_login"),
    url(r'^logout$',logout, name="loginAndRegistration_logout")
]
