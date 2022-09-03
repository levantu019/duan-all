from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import PhuBeMat as pbm
from nendialy.utils import media, form

from . import models, meta

# 1
class CayDocLapAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.CayDocLapMeta, pbm.CDL_CHOICES, models.CayDocLap)
    list_display = ('madt', 'tenCay', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class RanhGioiPhuBeMatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.RGPBMMeta, pbm.RGPBM_CHOICES, models.RanhGioiPhuBeMat)
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiRanhGioiPhuBeMat_display()


# 3
class BeMatCongTrinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.BMCTMeta, pbm.BMCT_CHOICES, models.BeMatCongTrinh)
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 4
class BeMatKhuDanCuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.BMKDCMeta, pbm.BMKDC_CHOICES, models.BeMatKhuDanCu)
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 5
class DatTrongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DatTrongMeta, pbm.DT_CHOICES, models.DatTrong)
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 6
class NuocMatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.NuocMatMeta, pbm.NM_CHOICES, models.NuocMat)
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class ThucVatDayBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TVDBMeta, pbm.TVDB_CHOICES, models.ThucVatDayBien)
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
admin.site.register(models.CayDocLap, CayDocLapAdmin)
admin.site.register(models.RanhGioiPhuBeMat, RanhGioiPhuBeMatAdmin)
admin.site.register(models.BeMatCongTrinh, BeMatCongTrinhAdmin)
admin.site.register(models.BeMatKhuDanCu, BeMatKhuDanCuAdmin)
admin.site.register(models.DatTrong, DatTrongAdmin)
admin.site.register(models.NuocMat, NuocMatAdmin)
admin.site.register(models.ThucVatDayBien, ThucVatDayBienAdmin)