from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('nhiem-vu-dieu-hanh', views.NVDHViewSet)
router.register('diem-nvdh', views.DiemNVDHViewSet)
router.register('tuyen-nvdh', views.TuyenNVDHViewSet)
router.register('vung-nvdh', views.VungNVDHViewSet)
router.register('don-vi', views.DonViViewSet)
router.register('nhiem-vu-bo-phan', views.NVBPViewSet)
router.register('phuong-an-vi-tri', views.PAViTriViewSet)
router.register('phuong-an-tuyen', views.PATuyenViewSet)
router.register('phuong-an-vung', views.PAVungViewSet)
router.register('phe-duyet-phuong-an-vi-tri', views.PDPAViTriViewSet)
router.register('phe-duyet-phuong-an-tuyen', views.PDPATuyenViewSet)
router.register('phe-duyet-phuong-an-vung', views.PDPAVungViewSet)
router.register('phe-duyet-chung-nvbp', views.PDChungNVBPViewSet)
router.register('gan-luc-luong', views.GanLLViewSet)
router.register('phe-duyet-phuong-an-gan-luc-luong', views.PDPAGanLLViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
