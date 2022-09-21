from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import PhuBeMat as pbm
from eav.decorators import register_eav
from multimedia.utils import choices


# -------------------- 6. Phủ bề mặt --------------------
# Abstract
class PhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

    # Fiedls
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')


# Feature: 1. Cây độc lập
@register_eav()
class CayDocLap(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Cây độc lập'
        verbose_name_plural = 'Cây độc lập'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.CDL_CHOICES, verbose_name='Mã đối tượng')
    tenCay = models.CharField(max_length=255, verbose_name='Tên cây')
    chieuCao = models.FloatField(verbose_name='Chiều cao')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 2. Ranh giới phủ bề mặt
@register_eav()
class RanhGioiPhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Ranh giới phủ bề mặt'
        verbose_name_plural = 'Ranh giới phủ bề mặt'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.RGPBM_CHOICES, verbose_name='Mã đối tượng')
    loaiRanhGioiPhuBeMat = models.IntegerField(choices=pbm.RGPBM_LOAI_CHOICES, verbose_name='Loại')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 3. Bề mặt công trình
@register_eav()
class BeMatCongTrinh(PhuBeMat):
    class Meta:
        verbose_name = 'Bề mặt công trình'
        verbose_name_plural = 'Bề mặt công trình'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMCT_CHOICES, verbose_name='Mã đối tượng')
    thucVat = models.IntegerField(choices=pbm.BMCT_TV_CHOICES, verbose_name='Thực vật')


# Feature: 4. Bề mặt khu dân cư
@register_eav()
class BeMatKhuDanCu(PhuBeMat):
    class Meta:
        verbose_name = 'Bề mặt khu dân cư'
        verbose_name_plural = 'Bề mặt khu dân cư'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMKDC_CHOICES, verbose_name='Mã đối tượng')
    thucVat = models.IntegerField(choices=pbm.BMKDC_TV_CHOICES, verbose_name='Thực vật')


# Feature: 5. Đất trống
@register_eav()
class DatTrong(PhuBeMat):
    class Meta:
        verbose_name = 'Đất trống'
        verbose_name_plural = 'Đất trống'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.DT_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, blank=True, verbose_name='Tên')


# Feature: 6. Nước mặt 
@register_eav()
class NuocMat(PhuBeMat):
    class Meta:
        verbose_name = 'Nước mặt'
        verbose_name_plural = 'Nước mặt'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.NM_CHOICES, verbose_name='Mã đối tượng')


# Feature: 7. Thực vật đáy biển
@register_eav()
class ThucVatDayBien(PhuBeMat):
    class Meta:
        verbose_name = 'Thực vật đáy biển'
        verbose_name_plural = 'Thực vật đáy biển'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.TVDB_CHOICES, verbose_name='Mã đối tượng')