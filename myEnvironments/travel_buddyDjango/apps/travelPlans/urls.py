from django.conf.urls import url
from views import index, register, login, dashboard, addTrip, destination, join, delete, logout
app_name= "travelPlans"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login, name='login'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^addTrip$', addTrip, name='addTrip'),
    url(r'^destination/(?P<id>\d+)$', destination, name='destination'),
    url(r'^join/(?P<user_id>\d+)/(?P<destination_id>\d+)$', join, name="join" ),
    url(r'^delete/(?P<id>\d+)$', delete, name='delete'),
    url(r'^logout$', logout, name='logout'),
]
