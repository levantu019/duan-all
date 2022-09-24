from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from eav.decorators import register_eav
from .utils import choices as mda, handleString, constants, funcs


# -------------------- Media Manage --------------------
#
# 1. Nhóm dữ liệu
@register_eav()
class NhomDuLieu(models.Model):
    class Meta:
        verbose_name = "Nhóm dữ liệu"
        verbose_name_plural = "Nhóm dữ liệu"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=50, primary_key=True, verbose_name="Nhóm")
    tenNhom = models.CharField(max_length=50, verbose_name="Tên nhóm", blank=True)
    moTaNhom = models.CharField(max_length=500, verbose_name="Mô tả nhóm", blank=True)

    #    
    def __str__(self):
        return self.tenNhom


# 2. Loại Style
@register_eav()
class LoaiStyle(models.Model):
    class Meta:
        verbose_name = "Loại Style"
        verbose_name_plural = "Loại Style"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã loại style", blank=True)
    tenLoaiStyle = models.CharField(max_length=100, verbose_name="Tên loại style")
    ghiChu = models.CharField(max_length=500, verbose_name="Ghi chú", blank=True)

    #
    def __str__(self):
        return self.tenLoaiStyle


# 3. Lớp dữ liệu
@register_eav()
class LopDuLieu(models.Model):
    class Meta:
        verbose_name = "Lớp dữ liệu"
        verbose_name_plural = "Lớp dữ liệu"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    content_type = models.OneToOneField(ContentType, on_delete=models.CASCADE, unique=True, blank=True, null=True)
    nhomDL = models.ForeignKey(NhomDuLieu, on_delete=models.CASCADE, verbose_name="Nhóm dữ liệu")
    maNhanDang = models.CharField(max_length=50, primary_key=True, verbose_name="Mã lớp", blank=True)
    tenHienThiLop = models.CharField(max_length=100, verbose_name="Tên hiển thị lớp", blank=True)
    publicGeoserver = models.BooleanField(default=False, verbose_name="Public Geoserver")
    pathPublic = models.CharField(max_length=200, verbose_name="Path public", blank=True)
    hienThiLopChuyenDe = models.BooleanField(default=False, verbose_name="Hiển thị lớp chuyên đề")
    thuTuHienThi = models.IntegerField(default=0, verbose_name="Thứ tự hiển thị")
    kieuLop = models.IntegerField(choices=mda.LDL_KIEU_CHOICES, verbose_name="Kiểu lớp", blank=True)

    #
    def __str__(self):
        return self.nhomDL.tenNhom + " | " + self.tenHienThiLop


# 4. Style
@register_eav()
class Style(models.Model):
    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Style"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã style", blank=True)
    tenStyle = models.CharField(max_length=100, verbose_name="Tên style")
    kieuDinhDangStyle = models.IntegerField(choices=mda.STYLE_KIEU_CHOICES, verbose_name="Kiểu định dạng style")
    ngayStyle = models.DateTimeField(verbose_name="Ngày style", blank=True, null=True)
    hienThi = models.BooleanField(default=True, verbose_name="Hiển thị")
    styleXML = models.TextField(max_length=50000, verbose_name="Style XML", blank=True)
    styleCSS = models.TextField(max_length=50000, verbose_name="Style CSS", blank=True)
    stylePath = models.FileField(
        upload_to="styles/",
        verbose_name="Style file",
        validators=[FileExtensionValidator(["xml", "css", "sld"])],
        blank=True,
        null=True,
    )
    maLop = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name="Lớp dữ liệu")
    maLoaiStyle = models.ForeignKey(LoaiStyle, on_delete=models.CASCADE, verbose_name="Loại style")

    #
    def __str__(self):
        return self.tenStyle


# 5. Dữ liệu đa phương tiện
@register_eav()
class DuLieuDaPhuongTien(models.Model):
    class Meta:
        verbose_name = "Dữ liệu đa phương tiện"
        verbose_name_plural = "Dữ liệu đa phương tiện"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã dữ liệu", blank=True)
    tenDuLieu = models.CharField(max_length=100, verbose_name="Tên dữ liệu", blank=True)
    pathDuLieu = models.FileField(upload_to=funcs.multimedia_upload_to, verbose_name="File dữ liệu")
    ngayDuLieu = models.DateTimeField(verbose_name="Ngày lưu dữ liệu", auto_now_add=True, blank=True, null=True)
    duLieuAnhDaiDien = models.BooleanField(default=False, verbose_name="Ảnh đại diện")
    duLieuMoTa = models.BooleanField(default=False, verbose_name="Dữ liệu mô tả")
    lopDL = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name="Lớp dữ liệu")
    maNhanDangObj = models.CharField(max_length=30, verbose_name="Mã nhận dạng đối tượng gốc")


# 6. MetaData
@register_eav()
class MetaData(models.Model):
    class Meta:
        verbose_name = "MetaData"
        verbose_name_plural = "MetaData"

    type_model = mda.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã MetaData")
    tenMetaData = models.CharField(max_length=50, verbose_name="Tên MetaData")
    XMLMetaData = models.TextField(max_length=50000, verbose_name="XML MetaData", blank=True)
    PathMetaData = models.FileField(
        upload_to="metadata/", validators=[FileExtensionValidator(["xml"])], verbose_name="MetaData file"
    )
    maLop = models.ForeignKey(LopDuLieu, on_delete=models.CASCADE, verbose_name="Lớp dữ liệu")
