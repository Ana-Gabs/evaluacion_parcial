# ./authentication/urls.py
from django.urls import path
from .views import CustomTokenObtainPairView  # Asegúrate de importar la nueva vista
from rest_framework_simplejwt.views import TokenRefreshView  

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

