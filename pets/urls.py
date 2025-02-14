from django.urls import path
from pets.views import PetListView, PetCreateView, PetUpdateView, PetDeleteView

urlpatterns = [
    path('list/', PetListView.as_view(), name='pet-list'),
    path('create/', PetCreateView.as_view(), name='pet-create'),
    path('update/<int:pk>/', PetUpdateView.as_view(), name='pet-update'),
    path('delete/<int:pk>/', PetDeleteView.as_view(), name='pet-delete'),
]
