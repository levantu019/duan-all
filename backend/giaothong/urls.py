from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('duong-bo', views.DuongBoViewSet)
router.register('cong-giao-thong-curve', views.Curve_CGTViewSet)
router.register('cong-giao-thong-point', views.Point_CGTViewSet)
router.register('duong-bang', views.DBANGViewSet)
router.register('bai-dap-truc-thang', views.BDTTViewSet)
router.register('bao-hieu-hang-hai-ais', views.BHHHAISViewSet)
router.register('ben-cang', views.BenCangViewSet)
router.register('cau-tau-surface', views.Surface_CTViewSet)
router.register('cau-tau-curve', views.Curve_CTViewSet)
router.register('bao-hieu-dan-luong-hang-hai-duong-thuy', views.BHDLHHDTViewSet)
router.register('cac-doi-tuong-hang-hai-hai-van-surface', views.Surface_CDTHHHVViewSet)
router.register('cac-doi-tuong-hang-hai-hai-van-point', views.Point_CDTHHHVViewSet)
router.register('nhom-au-tau-surface', views.Surface_NATViewSet)
router.register('nhom-au-tau-curve', views.Curve_NATViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
