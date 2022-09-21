from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import BienGioiDiaGioi as bgdg
from eav.decorators import register_eav
from multimedia.utils import choices

# -------------------- 1. Biên giới địa giới --------------------
# Abstract


# Feature: Vùng biển
@register_eav()
class VungBien(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Vùng biển'
        verbose_name_plural = 'Vùng biển'

    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.VB_CHOICES, verbose_name='Mã đối tượng')
    dienTich = models.FloatField(blank=True, null=True, verbose_name='Diện tích')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: Địa phận hành chính trên biển
@register_eav()
class DiaPhanHanhChinhTrenBien(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Địa phận hành chính trên biển'
        verbose_name_plural = 'Địa phận hành chính trên biển'

    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.DPHCTB_CHOICES, verbose_name='Mã đối tượng')
    maDonViHanhChinh = models.CharField(max_length=20, verbose_name='Mã đơn vị hành chính')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    dienTich = models.FloatField(blank=True, null=True, verbose_name='Diện tích')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: Đường ranh giới hành chính trên biển
@register_eav()
class DuongRanhGioiHanhChinhTrenBien(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đường ranh giới hành chính trên biển'
        verbose_name_plural = 'Đường ranh giới hành chính trên biển'

    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.DRGHCTB_CHOICES, verbose_name='Mã đối tượng')
    loaiHienTrangPhapLy = models.IntegerField(choices=bgdg.DRGHCTB_HTPL_CHOICES, verbose_name='Loại hiện trạng pháp lý')
    chieuDai = models.FloatField(verbose_name='Chiều dài')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: Địa phận hành chính trên đất liền
@register_eav()
class DiaPhanHanhChinhTrenDatLien(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Địa phận hành chính trên đất liền'
        verbose_name_plural = 'Địa phận hành chính trên đất liền'

    type_model = choices.LDL_KIEU_VUNG

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.DPHCTDL_CHOICES, verbose_name='Mã đối tượng')
    maDonViHanhChinh = models.CharField(max_length=50, verbose_name='Mã đơn vị hành chính')
    ten = models.CharField(max_length=50, verbose_name='Tên')
    dienTich = models.FloatField(verbose_name='Diện tích')
    soDan = models.IntegerField(verbose_name='Số dân')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()