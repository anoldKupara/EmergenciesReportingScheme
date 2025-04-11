from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this for the root URL
    path('report/', views.report_scheme, name='report_scheme'),
    path('report/<str:tracking_id>/', views.report_status, name='report_status'),
    path('counseling/', views.request_counseling, name='counseling'),
    path('escalate/<str:tracking_id>/', views.escalate_report, name='escalate_report'),
]