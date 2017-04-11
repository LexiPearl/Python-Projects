from django.conf.urls import url
from views import index, add_user_to_course

app_name = 'course_user'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_user_to_course$', add_user_to_course, name='add_user_to_course'),
]