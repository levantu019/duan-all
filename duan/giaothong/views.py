from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    DuongBo,
    CongGiaoThong,
    DuongBang,
    BaiDapTrucThang,
    BaoHieuHangHaiAIS,
    BenCang,
    CauTau,
    BaoHieuDanLuongHangHaiDuongThuy,
    CacDoiTuongHangHaiHaiVan,
    NhomAuTau
)
from .serializers import (
    DBSerializer,
    CGTSerializer,
    DBANGSerializer,
    BDTTSerializer,
    BHHHAISSerializer,
    BCSerializer,
    CTSerializer,
    BHDLHHDTSerializer,
    CDTHHHVSerializer,
    NATSerializer
)
from nendialy.decorators import http_methods_disable



# 1. Đường bộ
@http_methods_disable('post', 'put', 'patch', 'delete')
class DBViewSet(viewsets.ModelViewSet):
    queryset = DuongBo.objects.all()
    serializer_class = DBSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongBo.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaiduongbo')
    def choices_loaiDuongBo(self, request):
        try:
            choices = DuongBo.loaiDuongBo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='capkythuat')
    def choices_capKyThuat(self, request):
        try:
            choices = DuongBo.capKyThuat.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaicltm')
    def choices_loaiChatLieuTraiMat(self, request):
        try:
            choices = DuongBo.loaiChatLieuTraiMat.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaihtsd')
    def choices_loaiHienTrangSuDung(self, request):
        try:
            choices = DuongBo.loaiHienTrangSuDung.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='chieuxechay')
    def choices_chieuXeChay(self, request):
        try:
            choices = DuongBo.chieuXeChay.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='vitri')
    def choices_viTri(self, request):
        try:
            choices = DuongBo.viTri.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='lienketgt')
    def choices_lienKetGiaoThong(self, request):
        try:
            choices = DuongBo.lienKetGiaoThong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Cống giao thông
@http_methods_disable('post', 'put', 'patch', 'delete')
class CGTViewSet(viewsets.ModelViewSet):
    queryset = CongGiaoThong.objects.all()
    serializer_class = CGTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongGiaoThong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Đường băng
@http_methods_disable('post', 'put', 'patch', 'delete')
class DBANGViewSet(viewsets.ModelViewSet):
    queryset = DuongBang.objects.all()
    serializer_class = DBANGSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongBang.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 4. Bãi đáp trực thăng
@http_methods_disable('post', 'put', 'patch', 'delete')
class BDTTViewSet(viewsets.ModelViewSet):
    queryset = BaiDapTrucThang.objects.all()
    serializer_class = BDTTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BaiDapTrucThang.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='vitribaidap')
    def choices_viTriBaiDap(self, request):
        try:
            choices = BaiDapTrucThang.viTriBaiDap.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 5. Báo hiệu hàng hải AIS
@http_methods_disable('post', 'put', 'patch', 'delete')
class BHHHAISViewSet(viewsets.ModelViewSet):
    queryset = BaoHieuHangHaiAIS.objects.all()
    serializer_class = BHHHAISSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BaoHieuHangHaiAIS.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 6. Bến cảng
@http_methods_disable('post', 'put', 'patch', 'delete')
class BCViewSet(viewsets.ModelViewSet):
    queryset = BenCang.objects.all()
    serializer_class = BCSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BenCang.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 7. Cầu tàu
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTViewSet(viewsets.ModelViewSet):
    queryset = CauTau.objects.all()
    serializer_class = CTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CauTau.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaicautau')
    def choices_loaiCauTau(self, request):
        try:
            choices = CauTau.loaiCauTau.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
@http_methods_disable('post', 'put', 'patch', 'delete')
class BHDLHHDTViewSet(viewsets.ModelViewSet):
    queryset = BaoHieuDanLuongHangHaiDuongThuy.objects.all()
    serializer_class = BHDLHHDTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BaoHieuDanLuongHangHaiDuongThuy.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='huongbaohieu')
    def choices_huongBaoHieu(self, request):
        try:
            choices = BaoHieuDanLuongHangHaiDuongThuy.huongBaoHieu.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='hinhdang')
    def choices_hinhDang(self, request):
        try:
            choices = BaoHieuDanLuongHangHaiDuongThuy.hinhDang.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='mausac')
    def choices_mauSac(self, request):
        try:
            choices = BaoHieuDanLuongHangHaiDuongThuy.mauSac.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='phoihopmausac')
    def choices_phoiHopMauSac(self, request):
        try:
            choices = BaoHieuDanLuongHangHaiDuongThuy.phoiHopMauSac.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 9. Các đối tượng hàng hải hải văn
@http_methods_disable('post', 'put', 'patch', 'delete')
class CDTHHHVViewSet(viewsets.ModelViewSet):
    queryset = CacDoiTuongHangHaiHaiVan.objects.all()
    serializer_class = CDTHHHVSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CacDoiTuongHangHaiHaiVan.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 10. Nhóm Âu tàu
@http_methods_disable('post', 'put', 'patch', 'delete')
class NATViewSet(viewsets.ModelViewSet):
    queryset = NhomAuTau.objects.all()
    serializer_class = NATSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = NhomAuTau.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

