from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Emo Revival",
        default_version='v0.0 - Closed Beta',
        description="A maior balada Emo de São Paulo",
        terms_of_service="Termos de servicço",
        contact=openapi.Contact(email="contato@emorvvl.com.br"),
        license=openapi.License(name="No License"),
        ),
    public=True,
    permission_classes=[permissions.BasePermission, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('apps.event.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
