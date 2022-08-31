from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    BienDao,
    Dao,
    BaiBoi,
    BaiDaDuoiNuoc,
    NguonNuoc,
    DiemDoCaoMucNuoc,
    DuongBoNuoc,
    DuongMepNuoc,
    RanhGioiNuocMatQuyUoc,
    BoKeBoCap,
    KenhMuong,
    TramThuThapKTTV,
    ThamSoKTTV,
    SongGioDongChay,
    ThamSoNuoc
)
from .serializers import (
    BDSerializer,
    DSerializer,
    BBSerializer,
    BDDNSerializer,
    NNSerializer,
    DDCMNSerializer,
    DBNSerializer,
    DMNSerializer,
    RGNMQUSerializer,
    BKBCSerializer,
    KMSerializer,
    TTTTTTVSerializer,
    TSKTTVSerializer,
    SGDCSerializer,
    TSNSerializer
)
from nendialy.decorators import http_methods_enable


# 1. Biển đảo
@http_methods_enable('get')
class BDViewSet(viewsets.ModelViewSet):
    queryset = BienDao.objects.all()
    serializer_class = BDSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BienDao.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 2. Đảo
@http_methods_enable('get')
class DViewSet(viewsets.ModelViewSet):
    queryset = Dao.objects.all()
    serializer_class = DSerializer

    @action(methods=['get'], detail=False, url_path='loaittxl')
    def choices_loaiTrangThaiXuatLo(self, request):
        try:
            choices = Dao.loaiTrangThaiXuatLo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Bãi bồi
@http_methods_enable('get')
class BBViewSet(viewsets.ModelViewSet):
    queryset = BaiBoi.objects.all()
    serializer_class = BBSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BaiBoi.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaibaiboi')
    def choices_loaiBaiBoi(self, request):
        try:
            choices = BaiBoi.loaiBaiBoi.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='ttxl')
    def choices_trangThaiXuatLo(self, request):
        try:
            choices = BaiBoi.trangThaiXuatLo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 4. Bãi đá dưới nước
@http_methods_enable('get')
class BDDNViewSet(viewsets.ModelViewSet):
    queryset = BaiDaDuoiNuoc.objects.all()
    serializer_class = BDDNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BaiDaDuoiNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='ttxl')
    def choices_trangThaiXuatLo(self, request):
        try:
            choices = BaiDaDuoiNuoc.trangThaiXuatLo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 5. Nguồn nước
@http_methods_enable('get')
class NNViewSet(viewsets.ModelViewSet):
    queryset = NguonNuoc.objects.all()
    serializer_class = NNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = NguonNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loainguonnuoc')
    def choices_loaiNguonNuoc(self, request):
        try:
            choices = NguonNuoc.loaiNguonNuoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 6. Điểm độ cao mực nước
@http_methods_enable('get')
class DDCMNViewSet(viewsets.ModelViewSet):
    queryset = DiemDoCaoMucNuoc.objects.all()
    serializer_class = DDCMNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiemDoCaoMucNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 7. Đường bờ nước
@http_methods_enable('get')
class DBNViewSet(viewsets.ModelViewSet):
    queryset = DuongBoNuoc.objects.all()
    serializer_class = DBNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongBoNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaittdbn')
    def choices_loaiTrangThaiDuongBoNuoc(self, request):
        try:
            choices = DuongBoNuoc.loaiTrangThaiDuongBoNuoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaidbn')
    def choices_loaiDuongBoNuoc(self, request):
        try:
            choices = DuongBoNuoc.loaiDuongBoNuoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 8. Đường mép nước
@http_methods_enable('get')
class DMNViewSet(viewsets.ModelViewSet):
    queryset = DuongMepNuoc.objects.all()
    serializer_class = DMNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongMepNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaidmn')
    def choices_loaiDuongMepNuoc(self, request):
        try:
            choices = DuongMepNuoc.loaiDuongMepNuoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 9. Ranh giới nước mặt quy ước
@http_methods_enable('get')
class RGNMQUViewSet(viewsets.ModelViewSet):
    queryset = RanhGioiNuocMatQuyUoc.objects.all()
    serializer_class = RGNMQUSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = RanhGioiNuocMatQuyUoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loairgnmqu')
    def choices_loaiRanhGioiNuocMatQuyUoc(self, request):
        try:
            choices = RanhGioiNuocMatQuyUoc.loaiRanhGioiNuocMatQuyUoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 10. Bờ kè bờ cạp
@http_methods_enable('get')
class BKBCViewSet(viewsets.ModelViewSet):
    queryset = BoKeBoCap.objects.all()
    serializer_class = BKBCSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BoKeBoCap.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaichatlieu')
    def choices_loaiChatLieu(self, request):
        try:
            choices = BoKeBoCap.loaiChatLieu.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaithanhphan')
    def choices_loaiThanhPhan(self, request):
        try:
            choices = BoKeBoCap.loaiThanhPhan.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 11. Kênh mương
@http_methods_enable('get')
class KMViewSet(viewsets.ModelViewSet):
    queryset = KenhMuong.objects.all()
    serializer_class = KMSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = KenhMuong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaihtsd')
    def choices_loaiHienTrangSuDung(self, request):
        try:
            choices = KenhMuong.loaiHienTrangSuDung.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 12. Trạm thu thập TTTV
@http_methods_enable('get')
class TTTTTTVViewSet(viewsets.ModelViewSet):
    queryset = TramThuThapKTTV.objects.all()
    serializer_class = TTTTTTVSerializer

    @action(methods=['get'], detail=False, url_path='matkttv')
    def choices_maTramKTTV(self, request):
        try:
            choices = TramThuThapKTTV.maTramKTTV.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaitttkttv')
    def choices_loaiTramThuThapKTTV(self, request):
        try:
            choices = TramThuThapKTTV.loaiTramThuThapKTTV.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='kieuthuthapkttv')
    def choices_kieuThuThapKTTV(self, request):
        try:
            choices = TramThuThapKTTV.kieuThuThapKTTV.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 13. Tham số KTTV
@http_methods_enable('get')
class TSKTTVViewSet(viewsets.ModelViewSet):
    queryset = ThamSoKTTV.objects.all()
    serializer_class = TSKTTVSerializer

    @action(methods=['get'], detail=False, url_path='matskttv')
    def choices_maThamSoKTTV(self, request):
        try:
            choices = ThamSoKTTV.maThamSoKTTV.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='thamso')
    def choices_thamSo(self, request):
        try:
            choices = ThamSoKTTV.thamSo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 14. Số liệu sóng, gió, dòng chảy
@http_methods_enable('get')
class SGDCViewSet(viewsets.ModelViewSet):
    queryset = SongGioDongChay.objects.all()
    serializer_class = SGDCSerializer

    @action(methods=['get'], detail=False, url_path='masgdc')
    def choices_maSongGioDongChay(self, request):
        try:
            choices = SongGioDongChay.maSongGioDongChay.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='huong')
    def choices_huong(self, request):
        try:
            choices = SongGioDongChay.huongThang1.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='thamso')
    def choices_thamSo(self, request):
        try:
            choices = SongGioDongChay.thamSo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 15. Tham số nước
@http_methods_enable('get')
class TSNViewSet(viewsets.ModelViewSet):
    queryset = ThamSoNuoc.objects.all()
    serializer_class = TSNSerializer

    @action(methods=['get'], detail=False, url_path='matsnuoc')
    def choices_maThamSoNuoc(self, request):
        try:
            choices = ThamSoNuoc.maThamSoNuoc.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='tangdosau')
    def choices_tangDoSau(self, request):
        try:
            choices = ThamSoNuoc.tangDoSau.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='thamso')
    def choices_thamSo(self, request):
        try:
            choices = ThamSoNuoc.thamSo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

