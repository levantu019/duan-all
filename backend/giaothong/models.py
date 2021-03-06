from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import GiaoThong as gt


# -------------------- 5. Giao thông --------------------
# Abstract


# Feature: 1. Đường bộ
class DuongBo(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường bộ'
        verbose_name_plural = 'Đường bộ'
        
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
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 2. Cống giao thông
class CongGiaoThong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Cống giao thông'
        verbose_name_plural = 'Cống giao thông'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CGT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 3. Đường băng
class DuongBang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường băng'
        verbose_name_plural = 'Đường băng'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.DBANG_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 4. Bãi đáp trực thăng
class BaiDapTrucThang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Bãi đáp trực thăng'
        verbose_name_plural = 'Bãi đáp trực thăng'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BDTT_CHOICES, verbose_name='Mã đối tượng')
    viTriBaiDap = models.IntegerField(choices=gt.BDTT_VTBD_CHOICES, verbose_name='Vị trí')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 5. Báo hiệu hàng hải AIS
class BaoHieuHangHaiAIS(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Báo hiệu hàng hải AIS'
        verbose_name_plural = 'Báo hiệu hàng hải AIS'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHHHAIS_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 6. Bến cảng
class BenCang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Bến cảng'
        verbose_name_plural = 'Bến cảng'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BC_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 7. Cầu tàu
class CauTau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Cầu tàu'
        verbose_name_plural = 'Cầu tàu'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CT_CHOICES, verbose_name='Mã đối tượng')
    loaiCauTau = models.IntegerField(choices=gt.CT_LOAI_CHOICES, verbose_name='Loại')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BaoHieuDanLuongHangHaiDuongThuy(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Báo hiệu dẫn luồng hàng hải đường thuỷ'
        verbose_name_plural = 'Báo hiệu dẫn luồng hàng hải đường thuỷ'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHDLHHDT_CHOICES, verbose_name='Mã đối tượng')
    coDen = models.BooleanField(default=True, verbose_name='Có đèn')
    huongBaoHieu = models.IntegerField(choices=gt.BHDLHHDT_HUONGBH_CHOICES, verbose_name='Hướng báo hiệu')
    hinhDang = models.IntegerField(choices=gt.BHDLHHDT_HINHDANG_CHOICES, verbose_name='Hình dạng')
    mauSac = models.IntegerField(choices=gt.BHDLHHDT_MAUSAC_CHOICES, verbose_name='Màu sắc')
    phoiHopMauSac = models.IntegerField(choices=gt.BHDLHHDT_PHMS_CHOICES, verbose_name='Phối hợp màu sắc')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 9. Các đối tượng hàng hải hải văn
class CacDoiTuongHangHaiHaiVan(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Các đối tượng hàng hải hải văn'
        verbose_name_plural = 'Các đối tượng hàng hải hải văn'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CDTHHHV_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 10. Nhóm Âu tàu
class NhomAuTau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Nhóm Âu tàu'
        verbose_name_plural = 'Nhóm Âu tàu'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.NAT_CHOICES, verbose_name='Mã đối tượng')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

