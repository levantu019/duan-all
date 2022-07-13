from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    KhuDanCu,
    Nha,
    CongTrinhPhuTro,
    KhoiNha,
    DiaDanhDanCu,
    HaTangKyThuatKhac,
    TramKhiTuongThuyVanQuocGia,
    TramQuanTracMoiTruong,
    TramQuanTracTaiNguyenNuoc,
    DuongDayTaiDien,
    CotDien,
    DuongOngDan,
    RanhGioi,
    CongTrinhYTe,
    CongTrinhGiaoDuc,
    CongTrinhTheThao,
    CongTrinhVanHoa,
    CongTrinhThuongMaiDichVu,
    CongTrinhTonGiaoTinNguong,
    TruSoCoQuanNhaNuoc,
    CongTrinhCongNghiep,
    CoSoSanXuatNongLamNghiep,
    KhuChucNangDacThu,
    CongTrinhXuLyChatThai,
    CongTrinhAnNinh,
    CongTrinhQuocPhong
)
from .serializers import (
    KDCSerializer,
    NSerializer,
    CTPTSerializer,
    KNSerializer,
    DDDCSerializer,
    HTKTKSerializer,
    TKTTVQGSerializer,
    TQTMTSerializer,
    TQTTNNSerializer,
    DDTDSerializer,
    COTDIENSerializer,
    DODSerializer,
    RGSerializer,
    CTYTSerializer,
    CTGDSerializer,
    CTTTSerializer,
    CTVHSerializer,
    CTTMDVSerializer,
    CTTGTNSerializer,
    TSCQNNSerializer,
    CTCNSerializer,
    CSSXNLNSerializer,
    KCNDTSerializer,
    CTXLCTSerializer,
    CTANSerializer,
    CTQPSerializer
)
from nendialy.decorators import http_methods_disable


# 1.Khu dân cư
@http_methods_disable('post', 'put', 'patch', 'delete')
class KDCViewSet(viewsets.ModelViewSet):
    queryset = KhuDanCu.objects.all()
    serializer_class = KDCSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = KhuDanCu.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaikhudancu')
    def choices_loaiKhuDanCu(self, request):
        try:
            choices = KhuDanCu.loaiKhuDanCu.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Nhà
@http_methods_disable('post', 'put', 'patch', 'delete')
class NViewSet(viewsets.ModelViewSet):
    queryset = Nha.objects.all()
    serializer_class = NSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = Nha.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loainha')
    def choices_loaiNha(self, request):
        try:
            choices = Nha.loaiNha.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='mucdokienco')
    def choices_mucDoKienCo(self, request):
        try:
            choices = Nha.mucDoKienCo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Công trình phụ trợ
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTPTViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhPhuTro.objects.all()
    serializer_class = CTPTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhPhuTro.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 4. Khối nhà
@http_methods_disable('post', 'put', 'patch', 'delete')
class KNViewSet(viewsets.ModelViewSet):
    queryset = KhoiNha.objects.all()
    serializer_class = KNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = KhoiNha.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='nhomsotang')
    def choices_nhomSoTang(self, request):
        try:
            choices = KhoiNha.nhomSoTang.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='nhomchieucao')
    def choices_nhomChieuCao(self, request):
        try:
            choices = KhoiNha.nhomChieuCao.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 5. Địa danh dân cư
@http_methods_disable('post', 'put', 'patch', 'delete')
class DDDCViewSet(viewsets.ModelViewSet):
    queryset = DiaDanhDanCu.objects.all()
    serializer_class = DDDCSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiaDanhDanCu.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='danhtuchung')
    def choices_danhTuChung(self, request):
        try:
            choices = DiaDanhDanCu.danhTuChung.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 6. Hạ tầng kỹ thuật khác
@http_methods_disable('post', 'put', 'patch', 'delete')
class HTKTKViewSet(viewsets.ModelViewSet):
    queryset = HaTangKyThuatKhac.objects.all()
    serializer_class = HTKTKSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = HaTangKyThuatKhac.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 7. Trạm khí tượng thuỷ văn quốc gia
@http_methods_disable('post', 'put', 'patch', 'delete')
class TKTTVQGiewSet(viewsets.ModelViewSet):
    queryset = TramKhiTuongThuyVanQuocGia.objects.all()
    serializer_class = TKTTVQGSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = TramKhiTuongThuyVanQuocGia.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaitkttv')
    def choices_loaiTramKhiTuongThuyVan(self, request):
        try:
            choices = TramKhiTuongThuyVanQuocGia.loaiTramKhiTuongThuyVan.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 8. Trạm quan trắc môi trường
@http_methods_disable('post', 'put', 'patch', 'delete')
class TQTMTViewSet(viewsets.ModelViewSet):
    queryset = TramQuanTracMoiTruong.objects.all()
    serializer_class = TQTMTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = TramQuanTracMoiTruong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 9. Trạm quan trắc tài nguyên nước
@http_methods_disable('post', 'put', 'patch', 'delete')
class TQTTNNViewSet(viewsets.ModelViewSet):
    queryset = TramQuanTracTaiNguyenNuoc.objects.all()
    serializer_class = TQTTNNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = TramQuanTracTaiNguyenNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 10. Đường dây tải điện
@http_methods_disable('post', 'put', 'patch', 'delete')
class DDTDViewSet(viewsets.ModelViewSet):
    queryset = DuongDayTaiDien.objects.all()
    serializer_class = DDTDSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongDayTaiDien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 11. Cột điện
@http_methods_disable('post', 'put', 'patch', 'delete')
class CDViewSet(viewsets.ModelViewSet):
    queryset = CotDien.objects.all()
    serializer_class = COTDIENSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CotDien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 12. Đường ống dẫn
@http_methods_disable('post', 'put', 'patch', 'delete')
class DODViewSet(viewsets.ModelViewSet):
    queryset = DuongOngDan.objects.all()
    serializer_class = DODSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongOngDan.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaiongdan')
    def choices_loaiOngDan(self, request):
        try:
            choices = DuongOngDan.loaiOngDan.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 13. Ranh giới
@http_methods_disable('post', 'put', 'patch', 'delete')
class RGViewSet(viewsets.ModelViewSet):
    queryset = RanhGioi.objects.all()
    serializer_class = RGSerializer

    @action(methods=['get'], detail=False, url_path='loairanhgioi')
    def choices_loaiRanhGioi(self, request):
        try:
            choices = RanhGioi.loaiRanhGioi.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 14. Công trình y tế
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTYTViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhYTe.objects.all()
    serializer_class = CTYTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhYTe.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='capyte')
    def choices_capYTe(self, request):
        try:
            choices = CongTrinhYTe.capYTe.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 15. Công trình giáo dục
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTGDViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhGiaoDuc.objects.all()
    serializer_class = CTGDSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhGiaoDuc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 16. Công trình thể thao
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTTTViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhTheThao.objects.all()
    serializer_class = CTTTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhTheThao.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 17. Công trình văn hoá
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTVHViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhVanHoa.objects.all()
    serializer_class = CTVHSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhVanHoa.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='xephangditich')
    def choices_xepHangDiTich(self, request):
        try:
            choices = CongTrinhVanHoa.xepHangDiTich.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 18. Công trình thương mại dịch vụ
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTTMDVViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhThuongMaiDichVu.objects.all()
    serializer_class = CTTMDVSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhThuongMaiDichVu.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 19. Công trình tôn giáo tín ngưỡng
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTTGTNViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhTonGiaoTinNguong.objects.all()
    serializer_class = CTTGTNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhTonGiaoTinNguong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='xephangditich')
    def choices_xepHangDiTich(self, request):
        try:
            choices = CongTrinhTonGiaoTinNguong.xepHangDiTich.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 20. Trụ sở cơ quan nhà nước
@http_methods_disable('post', 'put', 'patch', 'delete')
class TSCQNNViewSet(viewsets.ModelViewSet):
    queryset = TruSoCoQuanNhaNuoc.objects.all()
    serializer_class = TSCQNNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = TruSoCoQuanNhaNuoc.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 21. Công trình công nghiệp
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTCNViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhCongNghiep.objects.all()
    serializer_class = CTCNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhCongNghiep.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaictcn')
    def choices_loaiCongTrinhCongNghiep(self, request):
        try:
            choices = CongTrinhCongNghiep.loaiCongTrinhCongNghiep.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 22. Cơ sở sản xuất nông lâm nghiệp
@http_methods_disable('post', 'put', 'patch', 'delete')
class CSSXNLNViewSet(viewsets.ModelViewSet):
    queryset = CoSoSanXuatNongLamNghiep.objects.all()
    serializer_class = CSSXNLNSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CoSoSanXuatNongLamNghiep.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 23. Khu chức năng đặc thù
@http_methods_disable('post', 'put', 'patch', 'delete')
class KCNDTViewSet(viewsets.ModelViewSet):
    queryset = KhuChucNangDacThu.objects.all()
    serializer_class = KCNDTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = KhuChucNangDacThu.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 24. Công trình xử lý chát thải
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTXLCTViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhXuLyChatThai.objects.all()
    serializer_class = CTXLCTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhXuLyChatThai.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 25. Công trình an ninh
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTANViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhAnNinh.objects.all()
    serializer_class = CTANSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhAnNinh.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 26. Công trình quốc phòng
@http_methods_disable('post', 'put', 'patch', 'delete')
class CTQPViewSet(viewsets.ModelViewSet):
    queryset = CongTrinhQuocPhong.objects.all()
    serializer_class = CTQPSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CongTrinhQuocPhong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
