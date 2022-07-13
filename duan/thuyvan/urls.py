from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('biendao', views.BDViewSet)
router.register('dao', views.DViewSet)
router.register('baiboi', views.BBViewSet)
router.register('baidaduoinuoc', views.BDDNViewSet)
router.register('nguonnuoc', views.NNViewSet)
router.register('diemdocaomucnuoc', views.DDCMNViewSet)
router.register('duongbonuoc', views.DBNViewSet)
router.register('duongmepnuoc', views.DMNViewSet)
router.register('ranhgioinuocmatquyuoc', views.RGNMQUViewSet)
router.register('bokebocap', views.BKBCViewSet)
router.register('kenhmuong', views.KMViewSet)
router.register('tramthuthaptttv', views.TTTTTTVViewSet)
router.register('thamsokttv', views.TSKTTVViewSet)
router.register('songgiodongchay', views.SGDCViewSet)
router.register('thamsonuoc', views.TSNViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
