from django.conf.urls import url
from views import dashboard, addBookReview, addReview, bookInfo, userInfo, delete, logout
app_name= "beltReviewerApp"
urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^addBookReview$', addBookReview, name='addBookReview'),
    url(r'^addReview/(?P<book_id>\d+)$', addReview, name='addReview'),
    url(r'^bookInfo/(?P<book_id>\d+)$', bookInfo, name='bookInfo'),
    url(r'^userInfo/(?P<id>\d+)$', userInfo, name='userInfo'),
    url(r'^delete/(?P<id>\d+)$', delete, name='delete'),
    url(r'^logout$', logout, name='logout')
]
