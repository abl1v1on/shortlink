from typing import Any
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import logout, get_user_model

from .forms import LoginUserForm, RegisterUserForm, CreateProfileForm
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
        profile = Profile.objects.create(user=user)
        self.request.session['profile_id'] = profile.pk
        return redirect('users:register_profile')


class CreateUserProfileView(CreateView):
    template_name = 'users/create-profile.html'
    form_class = CreateProfileForm

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.session.get('profile_id'):
            return redirect('users:register')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать профиль'
        return context
    
    def form_valid(self, form: CreateProfileForm) -> HttpResponse:
        cd = form.cleaned_data
        profile = get_object_or_404(Profile, pk=self.request.session['profile_id'])
        profile.picture = cd['picture']
        profile.description = cd['description']
        profile.save()
        return redirect('users:login')


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('users:login')
