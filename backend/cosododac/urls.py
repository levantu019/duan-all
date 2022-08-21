from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('diemgocdodacquocgia', views.DGDDQGViewSet)
router.register('diemdodacquocgia', views.DDDQGViewSet)
router.register('tramdinhvivetinhquocgia', views.TDVVTQGViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
