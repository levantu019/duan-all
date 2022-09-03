from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('cay-doc-lap', views.CayDocLapViewSet)
router.register('ranh-gioi-phu-be-mat', views.RGPBMViewSet)
router.register('be-mat-cong-trinh', views.BMCTViewSet)
router.register('be-mat-khu-dan-cu', views.BMKDCViewSet)
router.register('dat-trong', views.DatTrongViewSet)
router.register('nuoc-mat', views.NuocMatViewSet)
router.register('thuc-vat-day-bien', views.TVDBViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
