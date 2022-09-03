from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('vung-bien', views.VBViewSet)
router.register('dia-phan-hanh-chinh-tren-bien', views.DPHCTBViewSet)
router.register('duong-ranh-gioi-hanh-chinh-tren-bien', views.DRGHCTBViewSet)
router.register('dia-phan-hanh-chinh-tren-dat-lien', views.DPHCTDLViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
