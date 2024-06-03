from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import CustomUserCreationForm, CustomLoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomSetPasswordForm

# Create your views here.


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = CustomLoginForm


class HomeView(TemplateView):
    template_name = 'users/home.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class CustomSignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:signup_success')
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)


class SignupSuccessView(TemplateView):
    template_name = 'users/signup_success.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    email_template_name = 'users/password_reset_email.html'
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')
