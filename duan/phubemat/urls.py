from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('caydoclap', views.CDLViewSet)
router.register('ranhgioiphubemat', views.CDLViewSet)
router.register('bematcongtrinh', views.CDLViewSet)
router.register('bematkhudancu', views.CDLViewSet)
router.register('dattrong', views.CDLViewSet)
router.register('nuocmat', views.CDLViewSet)
router.register('thucvatdaybien', views.CDLViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
