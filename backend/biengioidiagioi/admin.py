from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import BienGioiDiaGioi as bgdg
from nendialy.utils import media, form, config

from . import models, meta


# 1. Vùng biển
class VungBienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.VBMeta, bgdg.VB_CHOICES, models.VungBien)
    list_display = ('maNhanDang', 'madt')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2. Địa phận hành chính trên biển
class DiaPhanHanhChinhTrenBienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DPHCTBMeta, bgdg.DPHCTB_CHOICES, models.DiaPhanHanhChinhTrenBien)
    list_display = ('maNhanDang', 'madt', 'madvhc', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Mã đơn vị hành chính')
    def madvhc(self, obj):
        return obj.get_maDonViHanhChinh_display()


# 3. Đường ranh giới hành chính trên biển
class DuongRanhGioiHanhChinhTrenBienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DRGHCTBMeta, bgdg.DRGHCTB_CHOICES, models.DuongRanhGioiHanhChinhTrenBien)
    list_display = ('maNhanDang', 'madt', 'loaihtpl', 'chieuDai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại hiện trạng pháp lý')
    def loaihtpl(self, obj):
        return obj.get_loaiHienTrangPhapLy_display()


# 4. Địa phận hành chính trên đất liền
class DiaPhanHanhChinhTrenDatLienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DPHCTDLMeta, bgdg.DPHCTDL_CHOICES, models.DiaPhanHanhChinhTrenDatLien)
    list_display = ('maNhanDang', 'madt', 'madvhc', 'ten', 'dienTich', 'soDan')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Mã đơn vị hành chính')
    def madvhc(self, obj):
        return obj.get_maDonViHanhChinh_display()


# Register
from django.conf import settings
from .apps import BiengioidiagioiConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.VungBien, VungBienAdmin)
    admin.site.register(models.DiaPhanHanhChinhTrenBien, DiaPhanHanhChinhTrenBienAdmin)
    admin.site.register(models.DuongRanhGioiHanhChinhTrenBien, DuongRanhGioiHanhChinhTrenBienAdmin)
    admin.site.register(models.DiaPhanHanhChinhTrenDatLien, DiaPhanHanhChinhTrenDatLienAdmin)