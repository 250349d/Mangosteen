from . import views
from django.urls import path

app_name = 'task_app'
urlpatterns = [
    path('', views.list_view, name='list'),
#    path('client/<int:client_id>', views.list_client_view, name='client'),
#    path('client/<int:worker_id>', views.list_worker_view, name='worker'),
    path('detail/<int:task_id>', views.detail_view, name='detail'),
    path('delete/<int:task_id>', views.delete_view, name='delete')
]
