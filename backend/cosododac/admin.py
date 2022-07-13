from django.contrib import admin
from .models import (
    DiemGocDoDacQuocGia,
    DiemDoDacQuocGia,
    TramDinhViVeTinhQuocGia
)
from nendialy.admin import CustomGeoAdmin


class DiemGocDoDacQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


class DieemDoDacQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaimoc', 'loaicaphang', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại mốc')
    def loaimoc(self, obj):
        return obj.get_loaiMoc_display()

    @admin.display(description = 'Loại cấp hạng')
    def loaicaphang(self, obj):
        return obj.get_loaiCapHang_display()


class TramDinhViVeTinhQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaitdvvt')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại trạm')
    def loaitdvvt(self, obj):
        return obj.get_loaiTramDinhViVeTinh_display()


# Register
admin.site.register(DiemGocDoDacQuocGia, CustomGeoAdmin)
admin.site.register(DiemDoDacQuocGia, CustomGeoAdmin)
admin.site.register(TramDinhViVeTinhQuocGia, CustomGeoAdmin)