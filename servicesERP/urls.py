from django.contrib import admin
from django.urls import path, include
from erp.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('erp/', include('erp.urls')),
    # Agrega otras rutas si las tienes
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


