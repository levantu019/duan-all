from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    DiemGocDoDacQuocGia,
    DiemDoDacQuocGia,
    TramDinhViVeTinhQuocGia
)
from .serializers import (
    DGDDQGSerializer,
    DDDQGSerializer,
    TDVVTQGSerializer
)
from nendialy.decorators import http_methods_enable


# 1. Điểm gốc đo đạc quốc gia
@http_methods_enable('get')
class DGDDQGViewSet(viewsets.ModelViewSet):
    queryset = DiemGocDoDacQuocGia.objects.all()
    serializer_class = DGDDQGSerializer
    # swagger_schema = None

    # Phải đăng nhập mới dùng được API này
    # permission_classes = [permissions.IsAuthenticated]

    # Bất kỳ người dùng nào cũng thực hiện được phương thức GET (list)
    # Các phương thức còn lại bắt buộc phải đăng nhập mới dùng được
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny]

    #     return [permissions.IsAuthenticated]

    # Tạo 1 action mới
    # @action(methods=['post'], detail=True)
    # /DGDDQG/{pk}/new_action
    @action(methods=['get'], detail=False)
    def choices_maDoiTuong(self, request):
        try:
            choices = DiemGocDoDacQuocGia.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # example
        # except DiemGocDoDacQuocGia.DoesNotExist:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Điểm đo đạc quốc gia
@http_methods_enable('get')
class DDDQGViewSet(viewsets.ModelViewSet):
    queryset = DiemDoDacQuocGia.objects.all()
    serializer_class = DDDQGSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiemDoDacQuocGia.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['get'], detail=False, url_path='loaimoc')
    def choices_loaiMoc(self, request):
        try:
            choices = DiemDoDacQuocGia.loaiMoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaicaphang')
    def choices_loaiCapHang(self, request):
        try:
            choices = DiemDoDacQuocGia.loaiCapHang.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Trạm định vị vệ tinh quốc gia
@http_methods_enable('get')
class TDVVTQGViewSet(viewsets.ModelViewSet):
    queryset = TramDinhViVeTinhQuocGia.objects.all()
    serializer_class = TDVVTQGSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = TramDinhViVeTinhQuocGia.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaitramdinhvivetinh')
    def choices_loaiTramDinhViVeTinh(self, request):
        try:
            choices = TramDinhViVeTinhQuocGia.loaiTramDinhViVeTinh.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)