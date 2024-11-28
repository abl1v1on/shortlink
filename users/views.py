from typing import Any
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import logout

from .forms import LoginUserForm, RegisterUserForm
from .models import Profile


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form: RegisterUserForm):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        Profile.objects.create(user=user)
        return super().form_valid(form)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('users:login')
