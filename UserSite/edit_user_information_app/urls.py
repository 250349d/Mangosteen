from django.urls import path
from . import views

app_name = 'edit_user_information_app'
urlpatterns = [
    path('', views.edit_view, name='edit'),
]
