from accounts.views import register_client, register_employee, register_individual, user_logout, user_type_page, CustomLoginView, profile
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', user_type_page, name='user-type'),
    path('register_client', register_client, name='reg-client' ),
    path('register_individual', register_individual, name='reg-individual' ),
    path('register_employee', register_employee, name='reg-employee' ),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
]
