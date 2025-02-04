from . import views
from django.urls import path

app_name = 'contact_app'
urlpatterns = [
    path('', views.list_view, name='list'),
    path('detail/<int:contact_id>', views.detail_view, name='detail'),
    path('delete/<int:contact_id>', views.delete_view, name='delete')
]
