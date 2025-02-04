from . import views
from django.urls import path

app_name = 'user_app'
urlpatterns = [
    path('', views.list_view, name='list'),
    path('detail/<int:user_id>', views.detail_view, name='detail'),
    path('delete/<int:user_id>', views.delete_view, name='delete')
]
