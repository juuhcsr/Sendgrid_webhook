from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('sendgrid_webhook/', views.sendgrid_webhookx, name='sendgrid_webhook'),
    path('sendgrid-logs/', views.sendgrid_logs, name='sendgrid_logs'),
    path('snippets/', views.SnippetList.as_view()),
]
