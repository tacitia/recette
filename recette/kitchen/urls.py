from django.conf.urls import patterns, url
from kitchen import views

urlpatterns = patterns('',
    url(r'^(?P<user_name>[a-z]+)/$', views.userKitchen, name = 'userKitchen'),
)
