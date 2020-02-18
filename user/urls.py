from django.conf.urls import url
# from . import views
from user.views import UserRetrieveAPIView, UserUpdateAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', UserRetrieveAPIView.as_view(), name='get_user_info'),
    url(r'^edit/$', UserUpdateAPIView.as_view(), name='update_user_info'),
]
