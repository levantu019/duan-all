from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('don-vi', views.DonViViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
