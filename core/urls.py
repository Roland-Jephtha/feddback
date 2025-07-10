# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='submit_feedback'),
    path('success/', views.feedback_success, name='feedback_success'),
]
