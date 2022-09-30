from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import ThuyVan as tv
from eav.decorators import register_eav
from multimedia.utils import choices


# -------------------- 7. Thuỷ văn --------------------
# Abstract
class RanhGioiNuocMat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

    # Fields
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 1. Biển đảo
class BienDao(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BD_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 1.1.
@register_eav()
class Surface_BienDao(BienDao):
    class Meta:
        verbose_name = 'Biển đảo (Surface)'
        verbose_name_plural = 'Biển đảo (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 1.2.
@register_eav()
class Point_BienDao(BienDao):
    class Meta:
        verbose_name = 'Biển đảo (Point)'
        verbose_name_plural = 'Biển đảo (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 2. Đảo
class Dao(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DAO_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    loaiTrangThaiXuatLo = models.IntegerField(choices=tv.DAO_LOAITTXL_CHOICES, verbose_name='Loại trạng thái xuất lô')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 2.1.
@register_eav()
class Surface_Dao(Dao):
    class Meta:
        verbose_name = 'Đảo (Surface)'
        verbose_name_plural = 'Đảo (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 2.2.
@register_eav()
class Point_Dao(Dao):
    class Meta:
        verbose_name = 'Đảo (Point)'
        verbose_name_plural = 'Đảo (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 3. Bãi bồi
class BaiBoi(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BB_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    loaiBaiBoi = models.IntegerField(choices=tv.BB_LOAI_CHOICES, verbose_name='Loại')
    trangThaiXuatLo = models.IntegerField(choices=tv.BB_TTXL_CHOICES, verbose_name='Trạng thái xuất lô')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 3.1.
@register_eav()
class Surface_BaiBoi(BaiBoi):
    class Meta:
        verbose_name = 'Bãi bồi (Surface)'
        verbose_name_plural = 'Bãi bồi (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 3.2.
@register_eav()
class Point_BaiBoi(BaiBoi):
    class Meta:
        verbose_name = 'Bãi bồi (Point)'
        verbose_name_plural = 'Bãi bồi (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 4. Bãi đá dưới nước
class BaiDaDuoiNuoc(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BDDN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    trangThaiXuatLo = models.IntegerField(choices=tv.BDDN_TTXL_CHOICES, verbose_name='Trạng thái xuất lô')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 4.1.
@register_eav()
class Surface_BaiDaDuoiNuoc(BaiDaDuoiNuoc):
    class Meta:
        verbose_name = 'Bãi đá dưới nước (Surface)'
        verbose_name_plural = 'Bãi đá dưới nước (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 4.2.
@register_eav()
class Point_BaiDaDuoiNuoc(BaiDaDuoiNuoc):
    class Meta:
        verbose_name = 'Bãi đá dưới nước (Point)'
        verbose_name_plural = 'Bãi đá dưới nước (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 5. Nguồn nước
class NguonNuoc(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.NN_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    loaiNguonNuoc = models.IntegerField(choices=tv.NN_LOAI_CHOICES, verbose_name='Loại nguồn nước')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 5.1.
@register_eav()
class Surface_NguonNuoc(NguonNuoc):
    class Meta:
        verbose_name = 'Nguồn nước (Surface)'
        verbose_name_plural = 'Nguồn nước (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 5.2.
@register_eav()
class Point_NguonNuoc(NguonNuoc):
    class Meta:
        verbose_name = 'Nguồn nước (Point)'
        verbose_name_plural = 'Nguồn nước (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 6. Điểm độ cao mực nước
@register_eav()
class DiemDoCaoMucNuoc(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Điểm độ cao mực nước'
        verbose_name_plural = 'Điểm độ cao mực nước'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DDCMN_CHOICES, verbose_name='Mã đối tượng')
    doCao = models.FloatField(verbose_name='Độ cao')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 7. Đường bờ nước
@register_eav()
class DuongBoNuoc(RanhGioiNuocMat):
    class Meta:
        verbose_name = 'Đường bờ nước'
        verbose_name_plural = 'Đường bờ nước'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DBN_CHOICES, verbose_name='Mã đối tượng')
    loaiTrangThaiDuongBoNuoc = models.IntegerField(choices=tv.DBN_LOAITT_CHOICES, verbose_name='Loại trạng thái')
    loaiDuongBoNuoc = models.IntegerField(choices=tv.DBN_LOAI_CHOICES, verbose_name='Loại đường bờ nước')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 8. Đường mép nước
@register_eav()
class DuongMepNuoc(RanhGioiNuocMat):
    class Meta:
        verbose_name = 'Đường mép nước'
        verbose_name_plural = 'Đường mép nước'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DMN_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongMepNuoc = models.IntegerField(choices=tv.DMN_LOAI_CHOICES, verbose_name='Loại')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 9. Ranh giới nước mặt quy ước
@register_eav()
class RanhGioiNuocMatQuyUoc(RanhGioiNuocMat):
    class Meta:
        verbose_name = 'Ranh giới nước mặt quy ước'
        verbose_name_plural = 'Ranh giới nước mặt quy ước'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.RGNMQU_CHOICES, verbose_name='Mã đối tượng')
    loaiRanhGioiNuocMatQuyUoc = models.IntegerField(choices=tv.RGNMQU_LOAI_CHOICES, verbose_name='Loại')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 10. Bờ kè bờ cạp
@register_eav()
class BoKeBoCap(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Bờ kè bờ cạp'
        verbose_name_plural = 'Bờ kè bờ cạp'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BKBC_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    loaiChatLieu = models.IntegerField(choices=tv.BKBC_LOAICL_CHOICES, verbose_name='Loại chất liệU')
    loaiThanhPhan = models.IntegerField(choices=tv.BKBC_LOAITP_CHOICES, verbose_name='Loại thành phần')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 11. Kênh mương
class KenhMuong(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.KM_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    loaiHienTrangSuDung = models.IntegerField(choices=tv.KM_LOAIHTSD_CHOICES, verbose_name='Loại hiện trạng sử dụng')
    chieuRong = models.FloatField(verbose_name='Chiều rộng')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 11.1.
@register_eav()
class Surface_KenhMuong(KenhMuong):
    class Meta:
        verbose_name = 'Kênh mương (Surface)'
        verbose_name_plural = 'Kênh mương (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 11.2.
@register_eav()
class Curve_KenhMuong(KenhMuong):
    class Meta:
        verbose_name = 'Kênh mương (Curve)'
        verbose_name_plural = 'Kênh mương (Curve)'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 12. Trạm thu thập TTTV
@register_eav()
class TramThuThapKTTV(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Trạm thu thập TTTV'
        verbose_name_plural = 'Trạm thu thập TTTV'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.TTTKTTV_CHOICES, verbose_name='Mã trạm')
    tenTram = models.CharField(max_length=255, verbose_name='Tên trạm')
    loaiTramThuThapKTTV = models.IntegerField(choices=tv.TTTKTTV_LOAI_CHOICES, verbose_name='Loại trạm')
    kieuThuThapKTTV = models.IntegerField(choices=tv.TTTKTTV_KTT_CHOICES, verbose_name='Kiểu thu thập')
    Mota_TramKTTV = models.CharField(max_length=500, blank=True, null=True, verbose_name='Mô tả')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 13. Tham số KTTV
@register_eav()
class ThamSoKTTV(models.Model):
    class Meta:
        verbose_name = 'Tham số KTTV'
        verbose_name_plural = 'Tham số KTTV'
        
    type_model = choices.LDL_KIEU_KHAC
        
    # Fields
    maThamSoKTTV = models.CharField(max_length=50, choices=tv.TSKTTV_CHOICES, verbose_name='Mã trạm')
    thoigianThuThap = models.DateTimeField(null=True, blank=True, verbose_name='Thời gian thu thập')
    giatriThang1 = models.FloatField(null=True, blank=True, verbose_name='Tháng 1')
    giatriThang2 = models.FloatField(null=True, blank=True, verbose_name='Tháng 2')
    giatriThang3 = models.FloatField(null=True, blank=True, verbose_name='Tháng 3')
    giatriThang4 = models.FloatField(null=True, blank=True, verbose_name='Tháng 4')
    giatriThang5 = models.FloatField(null=True, blank=True, verbose_name='Tháng 5')
    giatriThang6 = models.FloatField(null=True, blank=True, verbose_name='Tháng 6')
    giatriThang7 = models.FloatField(null=True, blank=True, verbose_name='Tháng 7')
    giatriThang8 = models.FloatField(null=True, blank=True, verbose_name='Tháng 8')
    giatriThang9 = models.FloatField(null=True, blank=True, verbose_name='Tháng 9')
    giatriThang10 = models.FloatField(null=True, blank=True, verbose_name='Tháng 10')
    giatriThang11 = models.FloatField(null=True, blank=True, verbose_name='Tháng 11')
    giatriThang12 = models.FloatField(null=True, blank=True, verbose_name='Tháng 12')
    thamSo = models.IntegerField(choices=tv.TSKTTV_TS_CHOICES, verbose_name='Tham số')
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE, verbose_name='Trạm KTTV')


# Feature: 14. Số liệu sóng, gió, dòng chảy
class SongGioDongChay(models.Model):
    class Meta:
        verbose_name = 'Số liệu sóng, gió, dòng chảy'
        verbose_name_plural = 'Số liệu sóng, gió, dòng chảy'
        
    type_model = choices.LDL_KIEU_KHAC
        
    # Fields
    maSongGioDongChay = models.CharField(max_length=50, choices=tv.SGDC_CHOICES, verbose_name='Mã')
    thoigianThuThap = models.DateTimeField(null=True, blank=True, verbose_name='Thời gian thu thập')
    huongThang1 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 1')
    giaTriThang1 = models.FloatField(verbose_name='Giá trị tháng 1')
    huongThang2 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 2')
    giaTriThang2 = models.FloatField(verbose_name='Giá trị tháng 2')
    huongThang3 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 3')
    giaTriThang3 = models.FloatField(verbose_name='Giá trị tháng 3')
    huongThang4 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 4')
    giaTriThang4 = models.FloatField(verbose_name='Giá trị tháng 4')
    huongThang5 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 5')
    giaTriThang5 = models.FloatField(verbose_name='Giá trị tháng 5')
    huongThang6 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 6')
    giaTriThang6 = models.FloatField(verbose_name='Giá trị tháng 6')
    huongThang7 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 7')
    giaTriThang7 = models.FloatField(verbose_name='Giá trị tháng 7')
    huongThang8 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 8')
    giaTriThang8 = models.FloatField(verbose_name='Giá trị tháng 8')
    huongThang9 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 9')
    giaTriThang9 = models.FloatField(verbose_name='Giá trị tháng 9')
    huongThang10 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 10')
    giaTriThang10 = models.FloatField(verbose_name='Giá trị tháng 10')
    huongThang11 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 11')
    giaTriThang11 = models.FloatField(verbose_name='Giá trị tháng 11')
    huongThang12 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES, verbose_name='Hướng tháng 12')
    giaTriThang12 = models.FloatField(verbose_name='Giá trị tháng 12')
    thamSo = models.IntegerField(choices=tv.SGDC_TS_CHOICES, verbose_name='Tham số')
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE, verbose_name='Trạm KTTV')


# Feature: 15. Tham số nước
class ThamSoNuoc(models.Model):
    class Meta:
        verbose_name = 'Tham số nước'
        verbose_name_plural = 'Tham số nước'
        
    type_model = choices.LDL_KIEU_KHAC
        
    # Fields
    maThamSoNuoc = models.CharField(max_length=50, choices=tv.TSN_CHOICES)
    thoigianThuThap = models.DateTimeField(null=True, blank=True)
    giatriThang1 = models.FloatField(null=True, blank=True)
    giatriThang2 = models.FloatField(null=True, blank=True)
    giatriThang3 = models.FloatField(null=True, blank=True)
    giatriThang4 = models.FloatField(null=True, blank=True)
    giatriThang5 = models.FloatField(null=True, blank=True)
    giatriThang6 = models.FloatField(null=True, blank=True)
    giatriThang7 = models.FloatField(null=True, blank=True)
    giatriThang8 = models.FloatField(null=True, blank=True)
    giatriThang9 = models.FloatField(null=True, blank=True)
    giatriThang10 = models.FloatField(null=True, blank=True)
    giatriThang11 = models.FloatField(null=True, blank=True)
    giatriThang12 = models.FloatField(null=True, blank=True)
    tangDoSau = models.IntegerField(choices=tv.TSN_TDS_CHOICES)
    thamSo = models.IntegerField(choices=tv.TSN_TS_CHOICES)
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE)



