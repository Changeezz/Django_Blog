
from django.conf.urls import include, url
from django.contrib import admin
from Blog import views
urlpatterns = [
        url(r'^blogs/$', views.get_blogs),
        url(r'^detail/(\d+)/$', views.get_details, name='blog_get_detail'),
]
