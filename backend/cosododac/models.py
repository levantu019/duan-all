from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import CoSoDoDac as csdd
from eav.decorators import register_eav


# -------------------- 2. Cơ sở đo đạc --------------------
# Abstract
class CoSoDoDac(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    soHieuDiem = models.CharField(max_length=50, verbose_name='Số hiệu điểm')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')
    

# Feature: 1. Điểm gốc đo đạc quốc gia
@register_eav()
class DiemGocDoDacQuocGia(CoSoDoDac):
    class Meta:
        verbose_name = 'Điểm gốc đo đạc quốc gia'
        verbose_name_plural = 'Điểm gốc đo đạc quốc gia'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.DGDDQG_CHOICES, verbose_name='Mã đối tượng')
    doCao = models.FloatField(verbose_name='Độ cao')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 2. Điểm đo đạc quốc gia
@register_eav()
class DiemDoDacQuocGia(CoSoDoDac):
    class Meta:
        verbose_name = 'Điểm đo đạc quốc gia'
        verbose_name_plural = 'Điểm đo đạc quốc gia'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.DDDQG_CHOICES, verbose_name='Mã đối tượng')
    doCao = models.FloatField(verbose_name='Độ cao')
    loaiMoc = models.IntegerField(choices=csdd.DDDQG_LOAIMOC_CHOICES, verbose_name='Loại mốc')
    loaiCapHang = models.IntegerField(choices=csdd.DDDQG_LOAICAPHANG_CHOICES, verbose_name='Loại cấp hạng')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 3. Trạm định vị vệ tinh quốc gia
@register_eav()
class TramDinhViVeTinhQuocGia(CoSoDoDac):
    class Meta:
        verbose_name = 'Trạm định vị vệ tinh quốc gia'
        verbose_name_plural = 'Trạm định vị vệ tinh quốc gia'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.TDVVTQG_CHOICES, verbose_name='Mã đối tượng')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    loaiTramDinhViVeTinh = models.IntegerField(choices=csdd.TDVVTQG_LOAI_CHOICES, verbose_name='Loại')
    
    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()
