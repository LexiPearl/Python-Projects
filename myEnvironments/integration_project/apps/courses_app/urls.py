from django.conf.urls import url
from views import index, process, remove, delete, logout
app_name="courses_app"
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^process$', process, name="process"),
    url(r'^remove(?P<id>\d+)$', remove, name="remove"),
    url(r'^delete/(?P<id>\d+)$', delete, name="delete"),
    url(r'^logout$', logout, name="logout"),
    # url(r'^dashboard$', dashboard, name="dashbaord")
]
