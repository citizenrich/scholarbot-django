from django.conf.urls import url
# see stackoverflow answer on this. error using tutorial is:
# module 'api.views' has no attribute 'obtain_auth_token'
# use authviews or some other rename on import instead to avoid contention
from rest_framework.authtoken import views as authviews
# slight mod from recipe, added -jwt to end of url to avoid contention
# refresh and other features not implemented
from rest_framework_jwt.views import obtain_jwt_token

from api import views

urlpatterns = [
    url(r'^get/$', views.CustomGet.as_view()),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^api-token-auth-jwt/', obtain_jwt_token),
]
