from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import CoSoDoDac as csdd
from nendialy.utils import media, form

from . import models, meta

# 1.Điểm gốc đo đạc quốc gia
class DiemGocDoDacQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DGDDQGMeta, csdd.DGDDQG_CHOICES, models.DiemGocDoDacQuocGia)
    list_display = ('maNhanDang', 'madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2. Điểm đo đạc quốc gia
class DiemDoDacQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDDQGMeta, csdd.DDDQG_CHOICES, models.DiemDoDacQuocGia)
    list_display = ('maNhanDang', 'madt', 'loaimoc', 'loaicaphang', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại mốc')
    def loaimoc(self, obj):
        return obj.get_loaiMoc_display()

    @admin.display(description = 'Loại cấp hạng')
    def loaicaphang(self, obj):
        return obj.get_loaiCapHang_display()


# 3. Trạm định vị vệ tinh quốc gia
class TramDinhViVeTinhQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TDVVTQGMeta, csdd.TDVVTQG_CHOICES, models.TramDinhViVeTinhQuocGia)
    list_display = ('maNhanDang', 'madt', 'loaitdvvt')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại trạm')
    def loaitdvvt(self, obj):
        return obj.get_loaiTramDinhViVeTinh_display()


# Register
admin.site.register(models.DiemGocDoDacQuocGia, DiemGocDoDacQuocGiaAdmin)
admin.site.register(models.DiemDoDacQuocGia, DiemDoDacQuocGiaAdmin)
admin.site.register(models.TramDinhViVeTinhQuocGia, TramDinhViVeTinhQuocGiaAdmin)