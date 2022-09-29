from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import GiaoThong as gt
from eav.decorators import register_eav
from multimedia.utils import choices

# -------------------- 5. Giao thông --------------------
# Abstract


# Feature: 1. Đường bộ
@register_eav()
class DuongBo(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đường bộ'
        verbose_name_plural = 'Đường bộ'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.DB_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongBo = models.IntegerField(choices=gt.DB_LOAI_CHOICES, verbose_name='Loại')
    capKyThuat = models.IntegerField(choices=gt.DB_CKT_CHOICES, verbose_name='Cấp kỹ thuật')
    loaiChatLieuTraiMat = models.IntegerField(choices=gt.DB_LOAICLTM_CHOICES, verbose_name='Loại chất liệu trải mặt')
    loaiHienTrangSuDung = models.IntegerField(choices=gt.DB_LOAIHTSD_CHOICES, verbose_name='Loại hiện trạng sử dụng')
    chieuXeChay = models.IntegerField(choices=gt.DB_CHIEUXECHAY_CHOICES, verbose_name='Chiều xe chạy')
    viTri = models.IntegerField(choices=gt.DB_VITRI_CHOICES, verbose_name='Vị trí')
    soLanDuong = models.IntegerField(verbose_name='Số làn đường')
    chieuRong = models.FloatField(verbose_name='Chiều rộng')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    lienKetGiaoThong = models.IntegerField(choices=gt.DB_LKGT_CHOICES, verbose_name='Liên kết giao thông')
    tenTuyenGiaoThongXuyenQuocGia = models.CharField(max_length=255, verbose_name='Tuyến giao thông xuyên quốc gia')
    tenQuocLo = models.CharField(max_length=255, verbose_name='Tên quốc lộ')
    tenDuongTinh = models.CharField(max_length=255, verbose_name='Tên đường tỉnh')
    tenDuongHuyen = models.CharField(max_length=255, verbose_name='Tên đường huyện')
    tenDuongXa = models.CharField(max_length=255, verbose_name='Tên đường xã')
    tenDuongDoThi = models.CharField(max_length=255, verbose_name='Tên đường đô thị')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 2. Cống giao thông
class CongGiaoThong(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CGT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 2.1.
@register_eav()
class Curve_CongGiaoThong(CongGiaoThong):
    class Meta:
        verbose_name = 'Cống giao thông (Curve)'
        verbose_name_plural = 'Cống giao thông (Curve)'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    GM_Curve = models.LineStringField(srid=4756 , verbose_name='Hình dạng (Curve)')

# 2.2.
@register_eav()
class Point_CongGiaoThong(CongGiaoThong):
    class Meta:
        verbose_name = 'Cống giao thông (Point)'
        verbose_name_plural = 'Cống giao thông (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 3. Đường băng
@register_eav()
class DuongBang(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đường băng'
        verbose_name_plural = 'Đường băng'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.DBANG_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 4. Bãi đáp trực thăng
@register_eav()
class BaiDapTrucThang(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Bãi đáp trực thăng'
        verbose_name_plural = 'Bãi đáp trực thăng'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BDTT_CHOICES, verbose_name='Mã đối tượng')
    viTriBaiDap = models.IntegerField(choices=gt.BDTT_VTBD_CHOICES, verbose_name='Vị trí')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 5. Báo hiệu hàng hải AIS
@register_eav()
class BaoHieuHangHaiAIS(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Báo hiệu hàng hải AIS'
        verbose_name_plural = 'Báo hiệu hàng hải AIS'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHHHAIS_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 6. Bến cảng
@register_eav()
class BenCang(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Bến cảng'
        verbose_name_plural = 'Bến cảng'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BC_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 7. Cầu tàu
class CauTau(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CT_CHOICES, verbose_name='Mã đối tượng')
    loaiCauTau = models.IntegerField(choices=gt.CT_LOAI_CHOICES, verbose_name='Loại')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# 7.1.
@register_eav()
class Surface_CauTau(CauTau):
    class Meta:
        verbose_name = 'Cầu tàu (Surface)'
        verbose_name_plural = 'Cầu tàu (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 7.2.
@register_eav()
class Curve_CauTau(CauTau):
    class Meta:
        verbose_name = 'Cầu tàu (Curve)'
        verbose_name_plural = 'Cầu tàu (Curve)'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
@register_eav()
class BaoHieuDanLuongHangHaiDuongThuy(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Báo hiệu dẫn luồng hàng hải đường thuỷ'
        verbose_name_plural = 'Báo hiệu dẫn luồng hàng hải đường thuỷ'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHDLHHDT_CHOICES, verbose_name='Mã đối tượng')
    coDen = models.BooleanField(default=True, verbose_name='Có đèn')
    huongBaoHieu = models.IntegerField(choices=gt.BHDLHHDT_HUONGBH_CHOICES, verbose_name='Hướng báo hiệu')
    hinhDang = models.IntegerField(choices=gt.BHDLHHDT_HINHDANG_CHOICES, verbose_name='Hình dạng')
    mauSac = models.IntegerField(choices=gt.BHDLHHDT_MAUSAC_CHOICES, verbose_name='Màu sắc')
    phoiHopMauSac = models.IntegerField(choices=gt.BHDLHHDT_PHMS_CHOICES, verbose_name='Phối hợp màu sắc')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 9. Các đối tượng hàng hải hải văn
class CacDoiTuongHangHaiHaiVan(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CDTHHHV_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tên')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# 9.1.
@register_eav()
class Surface_CacDoiTuongHangHaiHaiVan(CacDoiTuongHangHaiHaiVan):
    class Meta:
        verbose_name = 'Các đối tượng hàng hải hải văn (Surface)'
        verbose_name_plural = 'Các đối tượng hàng hải hải văn (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 9.2.
@register_eav()
class Point_CacDoiTuongHangHaiHaiVan(CacDoiTuongHangHaiHaiVan):
    class Meta:
        verbose_name = 'Các đối tượng hàng hải hải văn (Point)'
        verbose_name_plural = 'Các đối tượng hàng hải hải văn (Point)'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 10. Nhóm Âu tàu
class NhomAuTau(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.NAT_CHOICES, verbose_name='Mã đối tượng')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# 10.1.
@register_eav()
class Surface_NhomAuTau(NhomAuTau):
    class Meta:
        verbose_name = 'Nhóm Âu tàu (Surface)'
        verbose_name_plural = 'Nhóm Âu tàu (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 10.2.
@register_eav()
class Curve_NhomAuTau(NhomAuTau):
    class Meta:
        verbose_name = 'Nhóm Âu tàu (Curve)'
        verbose_name_plural = 'Nhóm Âu tàu (Curve)'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')