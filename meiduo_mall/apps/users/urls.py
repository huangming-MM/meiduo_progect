from django.conf.urls import  url

from  . import  views

urlpatterns = [
    url(r'^register/$',views.RegisterView.as_view()),

    #判断用户重复
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$',views.RegisterView.as_view()),

    url(r'^/mobiles/(?P<mobile>1[3-9]\d{9})/count/$',views.MobileCountView.as_view()),
]