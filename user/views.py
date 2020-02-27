from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect

import user
from user.models import User
from user.forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return render(request, 'user/view_profile.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                print("You enter invalid date")
                return render(request, 'user/login.html', {'form': form})
                # return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


from django.contrib import messages
from user.forms import RegistrationForm
def signup(request):
    print("WWWWWWWWWWWWww")
    print(request.method )
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        print(form.is_valid())
        print(form.is_bound)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password')
            print(password)
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            if password == raw_password:
                form.save()
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('user:get_user_info')
            else:
                messages.error(request, "Incorrect password.")
        else:
            messages.error(request, form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'user/user_register.html', {'form': form})

# class MyRegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = "/login/"
#     template_name = "register.html"
#
#     def form_valid(self, form):
#         form.save()
#         return super(MyRegisterFormView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return super(MyRegisterFormView, self).form_invalid(form)


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
    def get(self, request):
        return render(request, 'user/view_profile.html', {'user': request.user})


class UserUpdateAPIView(View):
    def get(self, request):
        return render(request, 'user/edit_profile.html', {'user': request.user})

    def post(self, request):
        user = request.user
        form = User(request.POST or None)
        if request.method == 'POST':
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            # user.email = request.POST['email']
            # user.birth_data = request.POST['birth_data']
            user.educations = request.POST['educations']
            user.about_me = request.POST['about_me']
            if request.method == 'POST':
                user.save()
            context = {
                "form": form
            }
            return render(request, 'user/edit_profile.html', context)
        return render(request, 'user/edit_profile.html', {'user': request.user})



# from django.views.generic.edit import CreateView
#
# from user.forms import RegistrationForm
# class UserRegisterAPIView(CreateView):
#     """
#     Add new collector
#     """
#     model = User
#     success_url = '/'
#     form_class = RegistrationForm
#     template_name_suffix = '_register'
#
#     # def get_context_data(self, **kwargs):
#     #     """
#     #     Extends context data
#     #     :param kwargs:
#     #     :return: context
#     #     """
#     #     context = super(UserRegisterAPIView, self).get_context_data(**kwargs)
#     #     context['page_title'] = u'Создание нового коллекционера'
#     #     return context
#
#     def form_valid(self, form):
#         """
#         The successful addition of new collector
#         :param form:
#         :return: message
#         """
#         message = super(UserRegisterAPIView, self).form_valid(form)
#         mes = 'Register success.'
#         messages.success(self.request, mes)
#         return message
#
#     def post(self, request, *args, **kwargs):
#         print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
#         self.object = None
#         form = self.get_form()
#         print(form)
#         print(form.is_valid())
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

# class UserRegisterAPIView(View):
#     def get(self, request):
#         return render(request, 'user/register.html')
#
#     # def post(self, request):
#     #     return render(request, 'user/register.html', {'user': request.user})
#     # template_name = "user/register.html"
#     #
#     # def post(self, request, *args, **kwargs):
#     #     if request.method == 'POST':
#     #         username = request.POST.get('username')
#     #         first_name = request.POST.get('first_name')
#     #         last_name = request.POST.get('last_name')
#     #         email = request.POST.get('email')
#     #         password = request.POST.get('password')
#     #         password2 = request.POST.get('password2')
#     #
#     #         if password == password2:
#     #             User.objects.create_user(username, email, password)
#     #             return redirect(request, 'user/view_profile.html', {'user': request.user})
#     #
#     #     return render(request, self.template_name)
#
#     def post(self, request):
#         form = User(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             user.profile.email = form.cleaned_data.get('email')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = User()
#         return render(request, 'signup.html', {'form': form})

