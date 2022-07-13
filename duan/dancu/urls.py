from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('khudancu', views.KDCViewSet)
router.register('nha', views.NViewSet)
router.register('congtrinhphutro', views.CTPTViewSet)
router.register('khoinha', views.KNViewSet)
router.register('diadanhdancu', views.DDDCViewSet)
router.register('hatangkythuatkhac', views.HTKTKViewSet)
router.register('tramkhituongthuyvanquocgia', views.TKTTVQGiewSet)
router.register('tramquantracmoitruong', views.TQTMTViewSet)
router.register('tramquantractainguyennuoc', views.TQTTNNViewSet)
router.register('duongdaytaidien', views.DDTDViewSet)
router.register('cotdien', views.CDViewSet)
router.register('duongongdan', views.DODViewSet)
router.register('ranhgioi', views.RGViewSet)
router.register('congtrinhyte', views.CTYTViewSet)
router.register('congtrinhgiaoduc', views.CTGDViewSet)
router.register('congtrinhthethao', views.CTTTViewSet)
router.register('congtrinhvanhoa', views.CTVHViewSet)
router.register('congtrinhthuongmaidichvu', views.CTTMDVViewSet)
router.register('congtrinhtongiaotinnguong', views.CTTGTNViewSet)
router.register('trusocoquannhanuoc', views.TSCQNNViewSet)
router.register('congtrinhcongnghiep', views.CTCNViewSet)
router.register('cososanxuatnonglamnghiep', views.CSSXNLNViewSet)
router.register('khuchucnangdacthu', views.KCNDTViewSet)
router.register('congtrinhxulychatthai', views.CTXLCTViewSet)
router.register('congtrinhanninh', views.CTANViewSet)
router.register('congtrinhquocphong', views.CTQPViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
