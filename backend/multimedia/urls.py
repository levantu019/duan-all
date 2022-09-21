from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('nhom-du-lieu', views.NhomDuLieuViewSet)
router.register('loai-style', views.LoaiStyleViewSet)
router.register('lop-du-lieu', views.LopDuLieuViewSet)
router.register('style', views.StyleViewSet)
router.register('other/choice-models', views.GetModelName, basename='other')

urlpatterns = [
    path('other/value-fields/<str:app_label>/<str:model_name>/<str:field_name>', views.getValueFields, name='value_fields'),
    path('other/app-model/<str:id_model>', views.getApp_Model, name='app_model'),

    path('', include(router.urls)),
]
