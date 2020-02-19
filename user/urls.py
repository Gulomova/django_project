from django.conf.urls import url
# from . import views
from user.views import UserRetrieveAPIView, UserUpdateAPIView, UserRegisterAPIView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', UserRetrieveAPIView.as_view(), name='get_user_info'),
    url(r'^user/edit/$', UserUpdateAPIView.as_view(), name='update_user_info'),
    url(r'^register/$', UserRegisterAPIView.as_view(), name='create_user_info'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^user/login/$', UserLoginAPIView.as_view(), name='login_user'),
]
