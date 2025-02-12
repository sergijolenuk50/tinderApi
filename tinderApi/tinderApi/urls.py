"""
URL configuration for tinderApi project.

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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
    #django_auth/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import UserCreateView

urlpatterns = [
path('admin/', admin.site.urls),
path('accounts/', include('django.contrib.auth.urls')),
path('register/', UserCreateView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# ]

#Add Django site authentication urls (for login, logout, password management)

