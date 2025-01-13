from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'worker_app'
urlpatterns = [
    path('mypage/', TemplateView.as_view(template_name='worker_app/mypage.html'), name='mypage'),

    path('receive/', views.receive_request_view, name='receive_request'),
    path('conpleted-request/', views.completed_requests_view, name='completed_requests'),
    path('confirm_request/<int:pk>/', views.confirm_request_view, name='confirm_request'),
    path('cancel_request/<int:pk>/', views.cancel_request_view, name='cancel_request'),
    path('accepted/', views.accepted_requests_view, name='accepted_requests'),
    path('rewards/', views.reward_check_view, name='reward_check'),
    path('submit_cost/<int:pk>/', views.submit_cost_view, name='submit_cost'),
    path('approve_cost/<int:pk>/', views.approve_cost_view, name='approve_cost'),
#    path('requester/', views.requester_home_view, name='requester_home'),
]
