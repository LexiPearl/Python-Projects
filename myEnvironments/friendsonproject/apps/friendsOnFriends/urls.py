from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_friend$', views.add_friend),
    url(r'^add_friendship$', views.add_friendship),
]
