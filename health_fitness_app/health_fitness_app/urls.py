"""
URL configuration for health_fitness_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from fitness.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Fitness app URLs
    path('fitness/', include('fitness.urls')),

    # Home view for the root URL
    path('', home, name='home'),

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  # Password change URL
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # Password change done URL
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Password reset URL
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Password reset done URL
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Password reset confirm URL
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Password reset complete URL
]