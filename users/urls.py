from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('register/profile/', views.CreateUserProfileView.as_view(), name='register_profile'),
]
