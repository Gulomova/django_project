from django.conf.urls import url
from . import views
from django.shortcuts import render
from .models import Post

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]


def post_list(request):
    return render(request, 'blog/post_list.html', {})
