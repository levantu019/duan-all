from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('duongbo', views.DBViewSet)
router.register('conggiaothong', views.CGTViewSet)
router.register('duongbang', views.DBANGViewSet)
router.register('baidaptructhang', views.BDTTViewSet)
router.register('baohieuhanghaiais', views.BHHHAISViewSet)
router.register('bencang', views.BCViewSet)
router.register('cautau', views.CTViewSet)
router.register('baohieudanluonghanghaiduongthuy', views.BHDLHHDTViewSet)
router.register('cacdoituonghanghaihaivan', views.CDTHHHVViewSet)
router.register('nhomautau', views.NATViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
