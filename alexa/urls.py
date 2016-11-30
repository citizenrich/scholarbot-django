from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^test/$', csrf_exempt(views.AlexaTest.as_view()), name='test'),
    url(r'^prod/$', csrf_exempt(views.AlexaProd.as_view()), name='prod'),
]
