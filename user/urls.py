from django.conf.urls import url
# from . import views
from user.views import user_login, UserRetrieveAPIView, UserUpdateAPIView, UserRegisterAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', UserRetrieveAPIView.as_view(), name='get_user_info'),
    url(r'^edit/$', UserUpdateAPIView.as_view(), name='update_user_info'),
    url(r'^register/$', UserRegisterAPIView.as_view(), name='create_user_info'),
    url(r'^login/$', user_login, name='login'),
]
