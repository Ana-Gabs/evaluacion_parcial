# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns for this app here, e.g.,
    path('appointment/', views.appointment_view, name='appointment'),
]
