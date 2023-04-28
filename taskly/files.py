from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Create your forms here.
# It creates a form that allows users to create a new account.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class MyUserCreationForm(UserCreationForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        field = ['title', 'content', ]
        exclude = ['user', ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Task'))

