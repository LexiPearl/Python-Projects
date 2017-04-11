from django.conf.urls import url
from views import dashboard, addPoke, logout
app_name= "beltTwoApp"
urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^addPoke/(?P<pokee_id>\d+)$', addPoke, name='addPoke'),
    url(r'^logout$', logout, name='logout')
]
