from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('diem-do-cao', views.DDCViewSet)
router.register('duong-binh-do', views.DBDViewSet)
router.register('chat-day', views.ChatDayViewSet)
router.register('diem-do-sau', views.DDSViewSet)
router.register('duong-binh-do-sau', views.DBDSViewSet)
router.register('dia-hinh-dac-biet-day-bien-surface', views.Surface_DHDBDBViewSet)
router.register('dia-hinh-dac-biet-day-bien-curve', views.Curve_DHDBDBViewSet)
router.register('dia-mao', views.DiaMaoViewSet)
router.register('mo-hinh-so-do-cao-goc-lop-diem', views.DEMGLPViewSet)
router.register('mo-hinh-so-do-cao-goc-lop-duong', views.DEMGLLViewSet)
router.register('mo-hinh-so-do-cao-goc-lop-vung', views.DEMGLAViewSet)
router.register('mo-hinh-so-do-cao-goc-lop-vung-bien-tap', views.DEMDLVBTViewSet)
# router.register('lopluoitamgiacbatquytac', views.LTGBQTViewSet)
# router.register('lopraster', views.RSTViewSet)
router.register('ho-khoan-dia-chat', views.HKDCViewSet)
router.register('so-lieu-hkdc', views.SLHKDCViewSet)
router.register('mat-cat-dia-hinh-dia-chat', views.MCDHViewSet)
router.register('loai-dia-chat', views.LDCSerializer)


urlpatterns = [
    path('', include(router.urls)),
]
