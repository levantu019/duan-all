from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('attr-api', views.AttributeViewSet)

app_name = 'eav'

urlpatterns = [
    path('attr/new-attr', views.AttributeView.as_view(), name='new-attr'),
    path('attr-api', include(router.urls)),
]
