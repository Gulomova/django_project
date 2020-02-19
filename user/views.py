from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from django.views.generic import View

from django.http import HttpResponse

import user
from user.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


# class UserLoginAPIView(View):
#     def user_login(self, request):
#         args = {}
#         args.update(csrf(request))
#         if request.POST:
#             user_name = request.POST.get('username', '')
#             password = request.POST.get('password', '')
#             user1 = auth.authenticate(username='username', password='password')
#             if user1 is not None:
#                 auth.login(request, user1)
#                 return redirect('/')
#             else:
#                 args['login_error'] = "User is not defined"
#                 return redirect('login.html', args)
#
#
# class UserLogoutAPIView(View):
#     def user_logout(self, request):
#         auth.logout(request)
#         return redirect("/")


class UserRetrieveAPIView(View):
    # def get(self, request):
    #     return render(request, 'user/base.html', {'user': request.user})
    def get(self, request):
        view = 'get_user_info'
        return render(request, 'user/view_profile.html', {'user': view})


class UserUpdateAPIView(View):
    def get(self, request):
        return render(request, 'user/edit_profile.html', {'user': request.user})


class UserRegisterAPIView(View):
    def get(self, request):
        return render(request, 'user/register.html', {'user': request.user})




