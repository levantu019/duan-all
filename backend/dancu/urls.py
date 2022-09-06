from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('khu-dan-cu', views.KDCViewSet)
router.register('nha-surface', views.Surface_NViewSet)
router.register('nha-point', views.Point_NViewSet)
router.register('cong-trinh-phu-tro-surface', views.Surface_CTPTViewSet)
router.register('cong-trinh-phu-tro-curve', views.Curve_CTPTViewSet)
router.register('khoi-nha', views.KNViewSet)
router.register('dia-danh-dan-cu', views.DDDCViewSet)
router.register('ha-tang-ky-thuat-khac-surface', views.Surface_HTKTKViewSet)
router.register('ha-tang-ky-thuat-khac-point', views.Point_HTKTKViewSet)
router.register('tram-khi-tuong-thuy-van-quoc-gia', views.TKTTVQGiewSet)
router.register('tram-quan-trac-moi-truong', views.TQTMTViewSet)
router.register('tram-quan-trac-tai-nguyen-nuoc', views.TQTTNNViewSet)
router.register('duong-day-tai-dien', views.DDTDViewSet)
router.register('cot-dien', views.CotDienViewSet)
router.register('duong-ong-dan', views.DODViewSet)
router.register('ranh-gioi', views.RanhGioiViewSet)
router.register('cong-trinh-y-te-surface', views.Surface_CTYTViewSet)
router.register('cong-trinh-y-te-point', views.Point_CTYTViewSet)
router.register('cong-trinh-giao-duc-surface', views.Surface_CTGDViewSet)
router.register('cong-trinh-giao-duc-point', views.Point_CTGDViewSet)
router.register('cong-trinh-the-thao-surface', views.Surface_CTTTViewSet)
router.register('cong-trinh-the-thao-point', views.Point_CTTTViewSet)
router.register('cong-trinh-van-hoa-surface', views.Surface_CTVHViewSet)
router.register('cong-trinh-van-hoa-point', views.Point_CTVHViewSet)
router.register('cong-trinh-thuong-mai-dich-vu-surface', views.Surface_CTTMDVViewSet)
router.register('cong-trinh-thuong-mai-dich-vu-point', views.Point_CTTMDVViewSet)
router.register('cong-trinh-ton-giao-tin-nguong-surface', views.Surface_CTTGTNViewSet)
router.register('cong-trinh-ton-giao-tin-nguong-point', views.Point_CTTGTNViewSet)
router.register('tru-so-co-quan-nha-nuoc-surface', views.Surface_TSCQNNViewSet)
router.register('tru-so-co-quan-nha-nuoc-point', views.Point_TSCQNNViewSet)
router.register('cong-trinh-cong-nghiep-surface', views.Surface_CTCNViewSet)
router.register('cong-trinh-cong-nghiep-curve', views.Curve_CTCNViewSet)
router.register('cong-trinh-cong-nghiep-point', views.Point_CTCNViewSet)
router.register('co-so-san-xuat-nong-lam-nghiep-surface', views.Surface_CSSXNLNViewSet)
router.register('co-so-san-xuat-nong-lam-nghiep-point', views.Point_CSSXNLNViewSet)
router.register('khu-chuc-nang-dac-thu', views.KCNDTViewSet)
router.register('cong-trinh-xu-ly-chat-thai-surface', views.Surface_CTXLCTViewSet)
router.register('cong-trinh-xu-ly-chat-thai-point', views.Point_CTXLCTViewSet)
router.register('cong-trinh-an-ninh-surface', views.Surface_CTANViewSet)
router.register('cong-trinh-an-ninh-point', views.Point_CTANViewSet)
router.register('cong-trinh-quoc-phong-surface', views.Surface_CTQPViewSet)
router.register('cong-trinh-quoc-phong-point', views.Point_CTQPViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
