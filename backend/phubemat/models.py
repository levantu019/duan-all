from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import PhuBeMat as pbm


# -------------------- 6. Phủ bề mặt --------------------
# Abstract
class PhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

    # Fiedls
    GM_Surface = models.PolygonField(null=True, blank=True)


# Feature: 1. Cây độc lập
class CayDocLap(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Cây độc lập'
        verbose_name_plural = 'Cây độc lập'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.CDL_CHOICES, verbose_name='Mã đối tượng')
    tenCay = models.CharField(max_length=255, verbose_name='Tên cây')
    chieuCao = models.FloatField(verbose_name='Chiều cao')
    GM_Point = models.PointField(null=True, blank=True)


# Feature: 2. Ranh giới phủ bề mặt
class RanhGioiPhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Ranh giới phủ bề mặt'
        verbose_name_plural = 'Ranh giới phủ bề mặt'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.RGPBM_CHOICES, verbose_name='Mã đối tượng')
    loaiRanhGioiPhuBeMat = models.IntegerField(choices=pbm.RGPBM_LOAI_CHOICES, verbose_name='Loại')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 3. Bề mặt công trình
class BeMatCongTrinh(PhuBeMat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Bề mặt công trình'
        verbose_name_plural = 'Bề mặt công trình'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMCT_CHOICES, verbose_name='Mã đối tượng')
    thucVat = models.IntegerField(choices=pbm.BMCT_TV_CHOICES, verbose_name='Thực vật')


# Feature: 4. Bề mặt khu dân cư
class BeMatKhuDanCu(PhuBeMat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Bề mặt khu dân cư'
        verbose_name_plural = 'Bề mặt khu dân cư'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMKDC_CHOICES, verbose_name='Mã đối tượng')
    thucVat = models.IntegerField(choices=pbm.BMKDC_TV_CHOICES, verbose_name='Thực vật')


# Feature: 5. Đất trống
class DatTrong(PhuBeMat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đất trống'
        verbose_name_plural = 'Đất trống'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.DT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')


# Feature: 6. Nước mặt 
class NuocMat(PhuBeMat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Nước mặt'
        verbose_name_plural = 'Nước mặt'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.NM_CHOICES, verbose_name='Mã đối tượng')


# Feature: 7. Thực vật đáy biển
class ThucVatDayBien(PhuBeMat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Thực vật đáy biển'
        verbose_name_plural = 'Thực vật đáy biển'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.TVDB_CHOICES, verbose_name='Mã đối tượng')