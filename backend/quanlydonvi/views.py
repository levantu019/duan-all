from django.db.models import Sum, Count, F
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, permission_classes, api_view, authentication_classes
from drf_yasg.utils import swagger_auto_schema

from jwtauth.permissions import (
    IsSuperUser,
    IsAdminData,
)
from . import models, serializers


# 1. Loại đơn vị

# 2. Cấp đơn vị

# 3. Đơn vị
class DonViViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DonVi.objects.all()
    serializer_class = serializers.DonViSerializer
    