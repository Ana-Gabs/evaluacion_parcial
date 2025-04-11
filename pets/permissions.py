# pets/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class SoloEmpleadosOAdminsModifican(BasePermission):
    """
    Permite acceso de solo lectura a cualquiera,
    pero solo empleados o admins pueden modificar.
    """
    def has_permission(self, request, view):
        # Verifica si la acción es de solo lectura (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        
        # Verifica si el usuario está autenticado y si su rol es 'Empleado' o 'Admin'
        return request.user.is_authenticated and (
            request.user.role in ['Employee', 'Admin']  # Verifica el nombre exacto del rol
        )
