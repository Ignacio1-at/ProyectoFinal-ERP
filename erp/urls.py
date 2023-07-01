from django.urls import path
from .views import home, login_view, menu_view, procesar_formulario

app_name = 'erp'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('menu/', menu_view, name='menu'),
    path('procesar/', procesar_formulario, name='procesar'),    # Ruta para la vista de inicio de sesión
    # Otras rutas de la aplicación
]
