from django.urls import path
from adoptions.views import (
    AdoptionRequestListView, AdoptionRequestCreateView, 
    AdoptionRequestUpdateView, AdoptionRequestDeleteView
)

urlpatterns = [
    path('list/', AdoptionRequestListView.as_view(), name='adoption-list'),
    path('create/', AdoptionRequestCreateView.as_view(), name='adoption-create'),
    path('update/<int:pk>/', AdoptionRequestUpdateView.as_view(), name='adoption-update'),
    path('delete/<int:pk>/', AdoptionRequestDeleteView.as_view(), name='adoption-delete'),
]
