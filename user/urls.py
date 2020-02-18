from django.conf.urls import url
from . import views
from user.views import UserRetrieveAPIView, UserUpdateAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.UserRetrieveAPIView, name='get_user_info'),
    url(r'edit/^$', views.UserUpdateAPIView, name='update_user_info'),
]
