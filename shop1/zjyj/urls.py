from django.conf.urls import url
from . import views

app_name = 'shop1'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop1list/$', views.list, name='list'),
    url(r'^shop1detail/(\d+)/$', views.detail, name='detail'),
]

