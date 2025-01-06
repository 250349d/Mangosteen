from . import views
from django.urls import path

app_name = 'group_app'
urlpatterns = [
    path('', views.list_view, name='list'),
    path('choice/<int:manager_id>', views.choice_view, name='choice'),
]
