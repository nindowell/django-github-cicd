from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeDoneView
from .views import HomeView, ProfileView, CustomSignupView, SignupSuccessView, CustomLoginView, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordChangeView
from .forms import CustomLoginForm


app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('signup/success', SignupSuccessView.as_view(), name='signup_success'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('account/password-reset', CustomPasswordResetView.as_view(), name='password_reset'),
    path('account/password-reset/done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('account/password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account/password-reset/complete', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('account/password-change', CustomPasswordChangeView.as_view(), name='password_change'),
    path('account/password-change/done', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
