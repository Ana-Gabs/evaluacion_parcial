from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from users.models import CustomUser  # Tu modelo de usuario personalizado

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'users':  # Se ejecuta solo cuando se migra la app 'users'
        # Definir los grupos
        admin_group, created = Group.objects.get_or_create(name='Administrador')
        empleado_group, created = Group.objects.get_or_create(name='Empleado')
        viewer_group, created = Group.objects.get_or_create(name='Viewer')

        # Obtener permisos
        user_content_type = ContentType.objects.get_for_model(CustomUser)
        
        # Definir permisos específicos para cada grupo
        permisos_admin = Permission.objects.filter(content_type=user_content_type)  # Todos los permisos
        permisos_empleado = Permission.objects.filter(content_type=user_content_type, codename__in=['change_customuser'])
        permisos_viewer = Permission.objects.filter(content_type=user_content_type, codename__in=['view_customuser'])

        # Asignar permisos a los grupos
        admin_group.permissions.set(permisos_admin)
        empleado_group.permissions.set(permisos_empleado)
        viewer_group.permissions.set(permisos_viewer)

        print("Grupos creados o actualizados correctamente.")
