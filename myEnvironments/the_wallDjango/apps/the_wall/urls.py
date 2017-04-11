from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.thewall),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^newmessage$', views.newmessage),
    url(r'^newcomment/(?P<message_id>\w+)$', views.newcomment),
    url(r'^logout$', views.logout),

]
