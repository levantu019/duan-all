from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('bien-dao-surface', views.Surface_BienDaoViewSet)
router.register('bien-dao-point', views.Point_BienDaoViewSet)
router.register('dao-surface', views.Surface_DaoViewSet)
router.register('dao-point', views.Point_DaoViewSet)
router.register('bai-boi-surface', views.Surface_BaiBoiViewSet)
router.register('bai-boi-point', views.Point_BaiBoiViewSet)
router.register('bai-da-duoi-nuoc-surface', views.Surface_BDDNViewSet)
router.register('bai-da-duoi-nuoc-point', views.Point_BDDNViewSet)
router.register('nguon-nuoc-surface', views.Surface_NguonNuocViewSet)
router.register('nguon-nuoc-point', views.Point_NguonNuocViewSet)
router.register('diem-do-cao-muc-nuoc', views.DDCMNViewSet)
router.register('duong-bo-nuoc', views.DBNViewSet)
router.register('duong-mep-nuoc', views.DMNViewSet)
router.register('ranh-gioi-nuoc-mat-quy-uoc', views.RGNMQUViewSet)
router.register('bo-ke-bo-cap', views.BKBCViewSet)
router.register('kenh-muong-surface', views.Surface_KenhMuongViewSet)
router.register('kenh-muong-curve', views.Curve_KenhMuongViewSet)
router.register('tram-thu-thap-tttv', views.TTTTTTVViewSet)
router.register('tham-so-kttv', views.TSKTTVViewSet)
router.register('song-gio-dong-chay', views.SGDCViewSet)
router.register('tham-so-nuoc', views.TSNViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
