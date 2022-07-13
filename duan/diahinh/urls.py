from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('diemdocao', views.DDCViewSet)
router.register('duongbinhdo', views.DBDViewSet)
router.register('chatday', views.CDViewSet)
router.register('diemdosau', views.DDSViewSet)
router.register('duongbinhdosau', views.DBDSViewSet)
router.register('diahinhdacbietdaybien', views.DHDBDBViewSet)
router.register('diamao', views.DMViewSet)
router.register('mohinhsodocaogoclopdiem', views.DEMGLPViewSet)
router.register('mohinhsodocaogoclopduong', views.DEMGLLViewSet)
router.register('mohinhsodocaogoclopvung', views.DEMGLAViewSet)
router.register('mohinhsodocaogoclopvungbientap', views.DEMDLVBTViewSet)
router.register('lopluoitamgiacbatquytac', views.LTGBQTViewSet)
router.register('lopraster', views.RSTViewSet)
router.register('hokhoandiachat', views.HKDCViewSet)
router.register('solieuhkdc', views.SLHKDCViewSet)
router.register('matcatdiahinhdiachat', views.MCDHViewSet)
router.register('loaidiachat', views.LDCSerializer)


urlpatterns = [
    path('', include(router.urls)),
]
