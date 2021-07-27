from django import forms
from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=commit)
        password = self.cleaned_data["password"]
        user.set_password(password)
        user.save()
        return user
