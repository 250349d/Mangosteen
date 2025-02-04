from . import views
from django.urls import path

app_name = 'manager_app'
urlpatterns = [
    path('', views.list_view, name='list'),
    path('create', views.create_view, name='create'),
    path('detail/<int:manager_id>', views.detail_view, name='detail'),
    path('delete/<int:manager_id>', views.delete_view, name='delete')
]
