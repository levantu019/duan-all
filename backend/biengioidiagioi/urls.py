from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('vungbien', views.VBViewSet)
router.register('diaphanhanhchinhtrenbien', views.DPHCTBViewSet)
router.register('duongranhgioihanhchinhtrenbien', views.DRGHCTBViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
