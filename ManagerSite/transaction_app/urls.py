from . import views
from django.urls import path

app_name = 'transaction_app'
urlpatterns = [
    path('detail/<int:task_id>', views.detail_view, name='detail'),
]
