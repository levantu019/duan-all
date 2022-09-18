from django.db import models
from django.core.validators import FileExtensionValidator
from eav.decorators import register_eav

from .utils import choices as mda, handleString, constants


# -------------------- Media Manage --------------------
# 
# 1. Nhóm dữ liệu
@register_eav()
class NhomDuLieu(models.Model):
    class Meta:
        verbose_name = 'Nhóm dữ liệu'
        verbose_name_plural = 'Nhóm dữ liệu'
    
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã nhóm', blank=True)
    tenNhom = models.CharField(max_length=50, verbose_name='Tên nhóm')
    moTaNhom = models.CharField(max_length=500, verbose_name='Mô tả nhóm', blank=True)

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(NhomDuLieu, constants.NHOM_DL)
        super(NhomDuLieu, self).save(*args, **kwargs)

    def __str__(self):
        return self.tenNhom


# 2. Loại Style
@register_eav()
class LoaiStyle(models.Model):
    class Meta:
        verbose_name = 'Loại Style'
        verbose_name_plural = 'Loại Style'
        
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã loại style')
    tenLoaiStyle = models.CharField(max_length=100, verbose_name='Tên loại style')
    ghiChu = models.CharField(max_length=500, verbose_name='Ghi chú', blank=True)

    # 
    def __str__(self):
        return self.tenLoaiStyle


# 3. Lớp dữ liệu
@register_eav()
class LopDuLieu(models.Model):
    class Meta:
        verbose_name = 'Lớp dữ liệu'
        verbose_name_plural = 'Lớp dữ liệu'
        
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã lớp', blank=True)
    tenLop = models.CharField(max_length=50, verbose_name='Tên lớp')
    tenHienThiLop = models.CharField(max_length=100, verbose_name='Tên hiển thị lớp', blank=True)
    publicGeoserver = models.BooleanField(default=False, verbose_name='Public Geoserver')
    pathPublic = models.CharField(max_length=200, verbose_name='Path public', blank=True)
    hienThiLopChuyenDe = models.BooleanField(default=False, verbose_name='Hiển thị lớp chuyên đề')
    thuTuHienThi = models.IntegerField(default=0, verbose_name='Thứ tự hiển thị')
    kieuLop = models.IntegerField(choices=mda.LDL_KIEU_CHOICES, verbose_name='Kiểu lớp')
    maNhom = models.ForeignKey(NhomDuLieu, on_delete=models.CASCADE, verbose_name='Nhóm dữ liệu')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(LopDuLieu, constants.LOP_DL)
        super(LopDuLieu, self).save(*args, **kwargs)

    def __str__(self):
        return self.tenLop


# 4. Style
@register_eav()
class Style(models.Model):
    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Style'
        
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã style')
    tenStyle = models.CharField(max_length=100, verbose_name='Tên style')
    kieuDinhDangStyle = models.IntegerField(choices=mda.STYLE_KIEU_CHOICES, verbose_name='Kiểu định dạng style')
    ngayStyle = models.DateTimeField(verbose_name='Ngày style', blank=True, null=True)
    hienThi = models.BooleanField(default=True, verbose_name='Hiển thị')
    styleXML = models.TextField(max_length=50000, verbose_name='Style XML', blank=True)
    styleCSS = models.TextField(max_length=50000, verbose_name='Style CSS', blank=True)
    stylePath = models.FileField(upload_to='styles/', verbose_name='Style file', validators=[FileExtensionValidator( ['xml', 'css', 'sld'] ) ], blank=True, null=True)
    maLop = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name='Lớp dữ liệu')
    maLoaiStyle = models.ForeignKey(LoaiStyle, on_delete=models.CASCADE, verbose_name='Loại style')

    # 
    def __str__(self):
        return self.tenStyle

# 5. Dữ liệu đa phương tiện
@register_eav()
class DuLieuDaPhuongTien(models.Model):
    class Meta:
        verbose_name = 'Dữ liệu đa phương tiện'
        verbose_name_plural = 'Dữ liệu đa phương tiện'
        
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã dữ liệu')
    tenDuLieu = models.CharField(max_length=100, verbose_name='Tên dữ liệu', blank=True)
    pathDuLieu = models.FileField(upload_to='other/', verbose_name='File dữ liệu')
    ngayDuLieu = models.DateTimeField(verbose_name='Ngày lưu dữ liệu', blank=True, null=True)
    duLieuAnhDaiDien = models.BooleanField(default=False, verbose_name='Ảnh đại diện')
    duLieuMoTa = models.BooleanField(default=False, verbose_name='Dữ liệu mô tả')
    maLop = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name='Lớp dữ liệu')
    maNhanDangObj = models.CharField(max_length=30, verbose_name='Mã nhận dạng đối tượng gốc')

# 6. MetaData
@register_eav()
class MetaData(models.Model):
    class Meta:
        verbose_name = 'MetaData'
        verbose_name_plural = 'MetaData'
        
    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã MetaData')
    tenMetaData = models.CharField(max_length=50, verbose_name='Tên MetaData')
    XMLMetaData = models.TextField(max_length=50000, verbose_name='XML MetaData', blank=True)
    PathMetaData = models.FileField(upload_to='metadata/', validators=[FileExtensionValidator( ['xml'] ) ], verbose_name='MetaData file')
    maLop = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name='Lớp dữ liệu')