from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import DanCu as dc


# -------------------- 3. Dân cư --------------------
# Abstract


# Feature: 1. Khu dân cư
class KhuDanCu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Khu dân cư'
        verbose_name_plural = 'Khu dân cư'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KDC_CHOICES, verbose_name='Mã đối tượng')
    loaiKhuDanCu = models.IntegerField(choices=dc.KDC_LOAI_CHOICES, verbose_name='Loại')
    soDan = models.IntegerField(null=True, blank=True, verbose_name='Số dân')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 2. Nhà
class Nha(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Nhà'
        verbose_name_plural = 'Nhà'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.NHA_CHOICES, verbose_name='Mã đối tượng')
    loaiNha = models.IntegerField(choices=dc.NHA_LOAI_CHOICES, verbose_name='Loại')
    mucDoKienCo = models.IntegerField(choices=dc.NHA_MUCDOKIENCO_CHOICES, verbose_name='Mức độ kiên cố')
    chieuCao = models.FloatField(verbose_name='Chiều cao')
    soTang = models.IntegerField(verbose_name='Số tầng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    diaChi = models.CharField(max_length=255, null=True, blank=True, verbose_name='Địa chỉ')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 3. Công trình phụ trợ
class CongTrinhPhuTro(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình phụ trợ'
        verbose_name_plural = 'Công trình phụ trợ'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTPT_CHOICES, verbose_name='Mã đối tượng')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 4. Khối nhà
class KhoiNha(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Khối nhà'
        verbose_name_plural = 'Khối nhà'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KN_CHOICES, verbose_name='Mã đối tượng')
    nhomSoTang = models.IntegerField(choices=dc.KN_NHOMSOTANG_CHOICES, verbose_name='Nhóm số tầng')
    nhomChieuCao = models.IntegerField(choices=dc.KN_NHOMCHIEUCAO_CHOICES, verbose_name='Nhóm chiều cao')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 5. Địa danh dân cư
class DiaDanhDanCu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Địa danh dân cư'
        verbose_name_plural = 'Địa danh dân cư'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DD_CHOICES, verbose_name='Mã đối tượng')
    danhTuChung = models.IntegerField(choices=dc.DD_DANHTUCHUNG_CHOICES, verbose_name='Danh từ chung')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 6. Hạ tầng kỹ thuật khác
class HaTangKyThuatKhac(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Hạ tầng kỹ thuật khác'
        verbose_name_plural = 'Hạ tầng kỹ thuật khác'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.HTKTK_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    chieuCao = models.FloatField(null=True, blank=True, verbose_name='Chiều cao')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 7. Trạm khí tượng thuỷ văn quốc gia
class TramKhiTuongThuyVanQuocGia(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Trạm khí tượng thuỷ văn quốc gia'
        verbose_name_plural = 'Trạm khí tượng thuỷ văn quốc gia'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TKTTVQG_CHOICES, verbose_name='Mã đối tượng')
    loaiTramKhiTuongThuyVan = models.IntegerField(choices=dc.TKTTVQG_LOAI_CHOICES, verbose_name='Loại')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 8. Trạm quan trắc môi trường
class TramQuanTracMoiTruong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Trạm quan trắc môi trường'
        verbose_name_plural = 'Trạm quan trắc môi trường'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TQTMT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 9. Trạm quan trắc tài nguyên nước
class TramQuanTracTaiNguyenNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Trạm quan trắc tài nguyên nước'
        verbose_name_plural = 'Trạm quan trắc tài nguyên nước'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TQTTNN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 10. Đường dây tải điện
class DuongDayTaiDien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường dây tải điện'
        verbose_name_plural = 'Đường dây tải điện'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DDTD_CHOICES, verbose_name='Mã đối tượng')
    dienAp = models.FloatField(verbose_name='Điện áp')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 11. Cột điện
class CotDien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Cột điện'
        verbose_name_plural = 'Cột điện'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CD_CHOICES, verbose_name='Mã đối tượng')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 12. Đường ống dẫn
class DuongOngDan(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường ống dẫn'
        verbose_name_plural = 'Đường ống dẫn'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DOD_CHOICES, verbose_name='Mã đối tượng')
    loaiOngDan = models.IntegerField(choices=dc.DOD_LOAI_CHOICES, verbose_name='Loại')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 13. Ranh giới
class RanhGioi(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Ranh giới'
        verbose_name_plural = 'Ranh giới'

    # Fields
    maDoiTuong = models.CharField(max_length=50, verbose_name='Mã đối tượng')
    loaiRanhGioi = models.IntegerField(choices=dc.RG_LOAI_CHOICES, verbose_name='Loại')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 14. Công trình y tế
class CongTrinhYTe(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình y tế'
        verbose_name_plural = 'Công trình y tế'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTYT_CHOICES, verbose_name='Mã đối tượng')
    capYTe = models.IntegerField(choices=dc.CTYT_CAPYTE_CHOICES, verbose_name='Cấp y tế')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 15. Công trình giáo dục
class CongTrinhGiaoDuc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình giáo dục'
        verbose_name_plural = 'Công trình giáo dục'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTGD_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 16. Công trình thể thao
class CongTrinhTheThao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình thể thao'
        verbose_name_plural = 'Công trình thể thao'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 17. Công trình văn hoá
class CongTrinhVanHoa(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình văn hoá'
        verbose_name_plural = 'Công trình văn hoá'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTVH_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    xepHangDiTich = models.IntegerField(choices=dc.CTVH_XEPHANG_CHOICES, verbose_name='Xếp hạng di tích')
    chieuCao = models.FloatField(null=True, blank=True, verbose_name='Chiều cao')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 18. Công trình thương mại dịch vụ
class CongTrinhThuongMaiDichVu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình thương mại dịch vụ'
        verbose_name_plural = 'Công trình thương mại dịch vụ'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTMDV_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 19. Công trình tôn giáo tín ngưỡng
class CongTrinhTonGiaoTinNguong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình tôn giáo tín ngưỡng'
        verbose_name_plural = 'Công trình tôn giáo tín ngưỡng'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTGTN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    xepHangDiTich = models.IntegerField(choices=dc.CTTGTN_XEPHANG_CHOICES, verbose_name='Xếp hạng di tích')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 20. Trụ sở cơ quan nhà nước
class TruSoCoQuanNhaNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Trụ sở cơ quan nhà nước'
        verbose_name_plural = 'Trụ sở cơ quan nhà nước'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TSCQNN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 21. Công trình công nghiệp
class CongTrinhCongNghiep(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình công nghiệp'
        verbose_name_plural = 'Công trình công nghiệp'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTCN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    loaiCongTrinhCongNghiep = models.IntegerField(choices=dc.CTCN_LOAI_CHOICES, verbose_name='Loại')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 22. Cơ sở sản xuất nông lâm nghiệp
class CoSoSanXuatNongLamNghiep(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Cơ sở sản xuất nông lâm nghiệp'
        verbose_name_plural = 'Cơ sở sản xuất nông lâm nghiệp'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CSSXNLN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 23. Khu chức năng đặc thù
class KhuChucNangDacThu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Khu chức năng đặc thù'
        verbose_name_plural = 'Khu chức năng đặc thù'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KCNDT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 24. Công trình xử lý chát thải
class CongTrinhXuLyChatThai(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình xử lý chát thải'
        verbose_name_plural = 'Công trình xử lý chát thải'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTXLCT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 25. Công trình an ninh
class CongTrinhAnNinh(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình an ninh'
        verbose_name_plural = 'Công trình an ninh'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTAN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)
    
    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()

    # @property
    def set_GM_Point(self, data):
        self.GM_Point = data


# Feature: 26. Công trình quốc phòng
class CongTrinhQuocPhong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Công trình quốc phòng'
        verbose_name_plural = 'Công trình quốc phòng'

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTQP_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()

