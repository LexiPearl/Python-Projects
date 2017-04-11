from django.conf.urls import url
# from . import views
from views import index, add, course, delete, logout

app_name = 'course'
urlpatterns = [
    url(r'^$', index, name='index_course'),
    url(r'^add$', add, name='add'),
    url(r'^courses/destroy/(?P<id>\d+)$',course, name='course'),
    url(r'^delete/(?P<id>\d+)$',delete, name='delete'),
    url(r'^logout$', logout, name='logout'),
]