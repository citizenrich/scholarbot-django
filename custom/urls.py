from django.conf.urls import url

from custom import views

urlpatterns = [
    url(r'^custom/get/$', views.CustomGet.as_view()),
]
