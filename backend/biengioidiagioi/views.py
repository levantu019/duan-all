from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    VungBien,
    DiaPhanHanhChinhTrenBien,
    DuongRanhGioiHanhChinhTrenBien
)
from .serializers import (
    VBSerializer,
    DPHCTBSerializer,
    DRGHCTBSerializer
)

from nendialy.decorators import http_methods_disable


# 1. Vùng biển
@http_methods_disable('put', 'patch', 'delete')
class VBViewSet(viewsets.ModelViewSet):
    queryset = VungBien.objects.all()
    serializer_class = VBSerializer

    @action(methods=['get'], detail=False)
    def choices_maDoiTuong(self, request):
        try:
            choices = VungBien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Địa phận hành chính trên biển
@http_methods_disable('post', 'put', 'patch', 'delete')
class DPHCTBViewSet(viewsets.ModelViewSet):
    queryset = DiaPhanHanhChinhTrenBien.objects.all()
    serializer_class = DPHCTBSerializer

    @action(methods=['get'], detail=False)
    def choices_maDoiTuong(self, request):
        try:
            choices = DiaPhanHanhChinhTrenBien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Đường ranh giới hành chính trên biển
@http_methods_disable('post', 'put', 'patch', 'delete')
class DRGHCTBViewSet(viewsets.ModelViewSet):
    queryset = DuongRanhGioiHanhChinhTrenBien.objects.all()
    serializer_class = DRGHCTBSerializer

    @action(methods=['get'], detail=False)
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongRanhGioiHanhChinhTrenBien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def choices_loaiHTPL(self, request):
        try:
            choices = DuongRanhGioiHanhChinhTrenBien.loaiHienTrangPhapLy.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
