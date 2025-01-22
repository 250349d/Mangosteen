from . import views
from django.urls import path

app_name = 'passreset_app'
urlpatterns = [
    path('', views.passreset_view, name='passreset'),
    path('done/', views.passreset_done_view, name='done'),
]
