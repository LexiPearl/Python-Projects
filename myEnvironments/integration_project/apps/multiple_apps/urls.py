from django.conf.urls import url
from views import index, create
app_name= 'multiple_apps'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create')
]
