from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('don-vi', views.DonViViewSet)
router.register('loai-trang-bi-khi-tai', views.LoaiTrangBiKhiTaiViewSet)


urlpatterns = [
    path('statistic-type/<str:type>', views.statistic_type, name='statistic_type'),
    path('statistic-value/<str:type>/<str:value>', views.statistic_value, name='statistic_value'),
    path('', include(router.urls)),
]
