from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('diem-goc-do-dac-quoc-gia', views.DGDDQGViewSet)
router.register('diem-do-dac-quoc-gia', views.DDDQGViewSet)
router.register('tram-dinh-vi-ve-tinh-quoc-gia', views.TDVVTQGViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
