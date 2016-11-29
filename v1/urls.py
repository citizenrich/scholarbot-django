from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^search/(?P<uuid>[^/]+)/$', views.Search.as_view(), name='search')
    url(r'^search/$', views.Search.as_view(), name='search'),
    # url(r'^subscribe/$', views.Subscribe.as_view(), name='subscribe')
]
