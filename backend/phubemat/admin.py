from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import PhuBeMat as pbm
from nendialy.utils import media, form, config

from . import models, meta

# 1
class CayDocLapAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.CayDocLapMeta, pbm.CDL_CHOICES, models.CayDocLap, have_images=False)
    list_display = ('madt', 'tenCay', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class RanhGioiPhuBeMatAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.RGPBMMeta, pbm.RGPBM_CHOICES, models.RanhGioiPhuBeMat, have_images=False)
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiRanhGioiPhuBeMat_display()


# 3
class BeMatCongTrinhAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BMCTMeta, pbm.BMCT_CHOICES, models.BeMatCongTrinh, have_images=False)
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 4
class BeMatKhuDanCuAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BMKDCMeta, pbm.BMKDC_CHOICES, models.BeMatKhuDanCu, have_images=False)
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 5
class DatTrongAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DatTrongMeta, pbm.DT_CHOICES, models.DatTrong, have_images=False)
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 6
class NuocMatAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.NuocMatMeta, pbm.NM_CHOICES, models.NuocMat, have_images=False)
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class ThucVatDayBienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.TVDBMeta, pbm.TVDB_CHOICES, models.ThucVatDayBien, have_images=False)
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
from django.conf import settings
from .apps import PhubematConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.CayDocLap, CayDocLapAdmin)
    admin.site.register(models.RanhGioiPhuBeMat, RanhGioiPhuBeMatAdmin)
    admin.site.register(models.BeMatCongTrinh, BeMatCongTrinhAdmin)
    admin.site.register(models.BeMatKhuDanCu, BeMatKhuDanCuAdmin)
    admin.site.register(models.DatTrong, DatTrongAdmin)
    admin.site.register(models.NuocMat, NuocMatAdmin)
    admin.site.register(models.ThucVatDayBien, ThucVatDayBienAdmin)