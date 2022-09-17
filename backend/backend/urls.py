"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns_swagger = [
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns_admin = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('test/', include('test.urls')),
    path('eav/', include('eav.urls')),
    path('nen-dia-ly/', include('nendialy.urls')),
    path('bien-gioi-dia-gioi/', include('biengioidiagioi.urls')),
    path('co-so-do-dac/', include('cosododac.urls')),
    path('dan-cu/', include('dancu.urls')),
    path('dia-hinh/', include('diahinh.urls')),
    path('giao-thong/', include('giaothong.urls')),
    path('phu-be-mat/', include('phubemat.urls')),
    path('thuy-van/', include('thuyvan.urls')),
    path('soan-thao-ke-hoach/', include('soanthaokehoach.urls')),
    path('multi-media/', include('multimedia.urls')),
    path('du-lieu-quan-tri/', include('dulieuquantri.urls')),
]


# 
if settings.SWAGGER_ENABLED:
    urlpatterns += urlpatterns_swagger

# 
if settings.ADMIN_ENABLED:
    urlpatterns += urlpatterns_admin

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)