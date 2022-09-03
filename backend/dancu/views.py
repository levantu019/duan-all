from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1.Khu dân cư
class KDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.KhuDanCu.objects.all()
    serializer_class = serializers.KDCSerializer


# 2. Nhà
class Surface_NViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_Nha.objects.all()
    serializer_class = serializers.Surface_NSerializer

class Point_NViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_Nha.objects.all()
    serializer_class = serializers.Point_NSerializer


# 3. Công trình phụ trợ
class Surface_CTPTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhPhuTro.objects.all()
    serializer_class = serializers.Surface_CTPTSerializer

class Curve_CTPTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_CongTrinhPhuTro.objects.all()
    serializer_class = serializers.Curve_CTPTSerializer


# 4. Khối nhà
class KNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.KhoiNha.objects.all()
    serializer_class = serializers.KNSerializer


# 5. Địa danh dân cư
class DDDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiaDanhDanCu.objects.all()
    serializer_class = serializers.DDDCSerializer


# 6. Hạ tầng kỹ thuật khác
class Surface_HTKTKViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_HaTangKyThuatKhac.objects.all()
    serializer_class = serializers.Surface_HTKTKSerializer

class Point_HTKTKViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_HaTangKyThuatKhac.objects.all()
    serializer_class = serializers.Point_HTKTKSerializer


# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGiewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TramKhiTuongThuyVanQuocGia.objects.all()
    serializer_class = serializers.TKTTVQGSerializer


# 8. Trạm quan trắc môi trường
class TQTMTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TramQuanTracMoiTruong.objects.all()
    serializer_class = serializers.TQTMTSerializer


# 9. Trạm quan trắc tài nguyên nước
class TQTTNNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TramQuanTracTaiNguyenNuoc.objects.all()
    serializer_class = serializers.TQTTNNSerializer


# 10. Đường dây tải điện
class DDTDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongDayTaiDien.objects.all()
    serializer_class = serializers.DDTDSerializer


# 11. Cột điện
class CotDienViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CotDien.objects.all()
    serializer_class = serializers.CotDienSerializer


# 12. Đường ống dẫn
class DODViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongOngDan.objects.all()
    serializer_class = serializers.DODSerializer


# 13. Ranh giới
class RanhGioiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RanhGioi.objects.all()
    serializer_class = serializers.RanhGioiSerializer


# 14. Công trình y tế
class Surface_CTYTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhYTe.objects.all()
    serializer_class = serializers.Surface_CTYTSerializer

class Point_CTYTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhYTe.objects.all()
    serializer_class = serializers.Point_CTYTSerializer


# 15. Công trình giáo dục
class Surface_CTGDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhGiaoDuc.objects.all()
    serializer_class = serializers.Surface_CTGDSerializer

class Point_CTGDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhGiaoDuc.objects.all()
    serializer_class = serializers.Point_CTGDSerializer


# 16. Công trình thể thao
class Surface_CTTTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhTheThao.objects.all()
    serializer_class = serializers.Surface_CTTTSerializer

class Point_CTTTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhTheThao.objects.all()
    serializer_class = serializers.Point_CTTTSerializer


# 17. Công trình văn hoá
class Surface_CTVHViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhVanHoa.objects.all()
    serializer_class = serializers.Surface_CTVHSerializer

class Point_CTVHViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhVanHoa.objects.all()
    serializer_class = serializers.Point_CTVHSerializer


# 18. Công trình thương mại dịch vụ
class Surface_CTTMDVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhThuongMaiDichVu.objects.all()
    serializer_class = serializers.Surface_CTTMDVSerializer

class Point_CTTMDVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhThuongMaiDichVu.objects.all()
    serializer_class = serializers.Point_CTTMDVSerializer


# 19. Công trình tôn giáo tín ngưỡng
class Surface_CTTGTNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhTonGiaoTinNguong.objects.all()
    serializer_class = serializers.Surface_CTTGTNSerializer

class Point_CTTGTNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhTonGiaoTinNguong.objects.all()
    serializer_class = serializers.Point_CTTGTNSerializer


# 20. Trụ sở cơ quan nhà nước
class Surface_TSCQNNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_TruSoCoQuanNhaNuoc.objects.all()
    serializer_class = serializers.Surface_TSCQNNSerializer

class Point_TSCQNNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_TruSoCoQuanNhaNuoc.objects.all()
    serializer_class = serializers.Point_TSCQNNSerializer


# 21. Công trình công nghiệp
class Surface_CTCNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhCongNghiep.objects.all()
    serializer_class = serializers.Surface_CTCNSerializer

class Curve_CTCNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_CongTrinhCongNghiep.objects.all()
    serializer_class = serializers.Curve_CTCNSerializer

class Point_CTCNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhCongNghiep.objects.all()
    serializer_class = serializers.Point_CTCNSerializer


# 22. Cơ sở sản xuất nông lâm nghiệp
class Surface_CSSXNLNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CoSoSanXuatNongLamNghiep.objects.all()
    serializer_class = serializers.Surface_CSSXNLNSerializer

class Point_CSSXNLNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CoSoSanXuatNongLamNghiep.objects.all()
    serializer_class = serializers.Point_CSSXNLNSerializer


# 23. Khu chức năng đặc thù
class KCNDTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.KhuChucNangDacThu.objects.all()
    serializer_class = serializers.KCNDTSerializer


# 24. Công trình xử lý chát thải
class Surface_CTXLCTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhXuLyChatThai.objects.all()
    serializer_class = serializers.Surface_CTXLCTSerializer

class Point_CTXLCTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhXuLyChatThai.objects.all()
    serializer_class = serializers.Point_CTXLCTSerializer


# 25. Công trình an ninh
class Surface_CTANViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhAnNinh.objects.all()
    serializer_class = serializers.Surface_CTANSerializer

class Point_CTANViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhAnNinh.objects.all()
    serializer_class = serializers.Point_CTANSerializer


# 26. Công trình quốc phòng
class Surface_CTQPViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CongTrinhQuocPhong.objects.all()
    serializer_class = serializers.Surface_CTQPSerializer

class Point_CTQPViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongTrinhQuocPhong.objects.all()
    serializer_class = serializers.Point_CTQPSerializer
