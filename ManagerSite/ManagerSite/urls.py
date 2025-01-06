"""
URL configuration for ManagerSite project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login-app/', include("login_app.urls")),
    path('manager-info/', include("manager_app.urls")),
    path('user-info/', include("user_app.urls")),
    path('task-info/', include("task_app.urls")),
    path('contact-info/', include("contact_app.urls")),
    path('notification-info/', include("notification_app.urls")),
    path('homepage/', include("home_app.urls")),
    path('mypage/', include("mypage_app.urls")),
    path('group-info/', include("group_app.urls")),
]
