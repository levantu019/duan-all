from django.contrib import admin
from .models import (
    CayDocLap,
    RanhGioiPhuBeMat,
    BeMatCongTrinh,
    BeMatKhuDanCu,
    DatTrong,
    NuocMat,
    ThucVatDayBien
)
from nendialy.admin import CustomGeoAdmin


# 1
class CayDocLapAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'tenCay', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class RanhGioiPhuBeMatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiRanhGioiPhuBeMat_display()


# 3
class BeMatCongTrinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 4
class BeMatKhuDanCuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'tv')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Thực vật')
    def tv(self, obj):
        return obj.get_thucVat_display()


# 5
class DatTrongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 6
class NuocMatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class ThucVatDayBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
admin.site.register(CayDocLap, CayDocLapAdmin)
admin.site.register(RanhGioiPhuBeMat, RanhGioiPhuBeMatAdmin)
admin.site.register(BeMatCongTrinh, BeMatCongTrinhAdmin)
admin.site.register(BeMatKhuDanCu, BeMatKhuDanCuAdmin)
admin.site.register(DatTrong, DatTrongAdmin)
admin.site.register(NuocMat, NuocMatAdmin)
admin.site.register(ThucVatDayBien, ThucVatDayBienAdmin)