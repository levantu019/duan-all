from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import BienGioiDiaGioi as bgdg


# -------------------- 1. Biên giới địa giới --------------------
# Abstract


# Feature: Vùng biển
class VungBien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Vùng biển'
        verbose_name_plural = 'Vùng biển'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.VB_CHOICES, verbose_name='Mã đối tượng')
    dientich = models.FloatField(blank=True, null=True, verbose_name='Diện tích')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: Địa phận hành chính trên biển
class DiaPhanHanhChinhTrenBien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Địa phận hành chính trên biển'
        verbose_name_plural = 'Địa phận hành chính trên biển'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.DPHCTB_CHOICES, verbose_name='Mã đối tượng')
    maDonViHanhChinh = models.CharField(max_length=20, verbose_name='Mã đơn vị hành chính')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    dientich = models.FloatField(blank=True, null=True, verbose_name='Diện tích')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: Đường ranh giới hành chính trên biển
class DuongRanhGioiHanhChinhTrenBien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường ranh giới hành chính trên biển'
        verbose_name_plural = 'Đường ranh giới hành chính trên biển'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=bgdg.DRGHCTB_CHOICES, verbose_name='Mã đối tượng')
    loaiHienTrangPhapLy = models.IntegerField(choices=bgdg.DRGHCTB_HTPL_CHOICES, verbose_name='Loại hiện trạng pháp lý')
    chieuDai = models.FloatField(verbose_name='Chiều dài')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()