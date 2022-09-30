from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import CoSoDoDac as csdd
from nendialy.utils import media, form, config

from . import models, meta


# 1.Điểm gốc đo đạc quốc gia
class DiemGocDoDacQuocGiaAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DGDDQGMeta, csdd.DGDDQG_CHOICES, models.DiemGocDoDacQuocGia, have_images=False)
    list_display = ("maNhanDang", "madt", "doCao")

    @admin.display(description="Mã đối tượng")
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2. Điểm đo đạc quốc gia
class DiemDoDacQuocGiaAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DDDQGMeta, csdd.DDDQG_CHOICES, models.DiemDoDacQuocGia, have_images=False)
    list_display = ("maNhanDang", "madt", "loaimoc", "loaicaphang", "doCao")

    @admin.display(description="Mã đối tượng")
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description="Loại mốc")
    def loaimoc(self, obj):
        return obj.get_loaiMoc_display()

    @admin.display(description="Loại cấp hạng")
    def loaicaphang(self, obj):
        return obj.get_loaiCapHang_display()


# 3. Trạm định vị vệ tinh quốc gia
class TramDinhViVeTinhQuocGiaAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.TDVVTQGMeta, csdd.TDVVTQG_CHOICES, models.TramDinhViVeTinhQuocGia, have_images=False)
    list_display = ("maNhanDang", "madt", "loaitdvvt")

    @admin.display(description="Mã đối tượng")
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description="Loại trạm")
    def loaitdvvt(self, obj):
        return obj.get_loaiTramDinhViVeTinh_display()


# Register
from django.conf import settings
from .apps import CosododacConfig as app

if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.DiemGocDoDacQuocGia, DiemGocDoDacQuocGiaAdmin)
    admin.site.register(models.DiemDoDacQuocGia, DiemDoDacQuocGiaAdmin)
    admin.site.register(models.TramDinhViVeTinhQuocGia, TramDinhViVeTinhQuocGiaAdmin)
