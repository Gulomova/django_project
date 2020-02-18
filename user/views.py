from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic import View

from django.http import HttpResponse
from user.models import User


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class UserRetrieveAPIView(View):
    def get(self, request):
        return render(request, 'user/base.html', {'user': request.user})


class UserUpdateAPIView(View):
    pass
