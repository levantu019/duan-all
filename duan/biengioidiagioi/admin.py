from django.contrib.gis import admin
from .models import (
    VungBien,
    DiaPhanHanhChinhTrenBien,
    DuongRanhGioiHanhChinhTrenBien
)
from nendialy.admin import CustomGeoAdmin


class VungBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'dientich')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


class DiaPhanHanhChinhTrenBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'madvhc', 'ten', 'dientich')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Mã đơn vị hành chính')
    def madvhc(self, obj):
        return obj.get_maDonViHanhChinh_display()


class DuongRanhGioiHanhChinhTrenBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaihtpl', 'chieuDai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại hiện trạng pháp lý')
    def loaihtpl(self, obj):
        return obj.get_loaiHienTrangPhapLy_display()


# Register
admin.site.register(VungBien, VungBienAdmin)
admin.site.register(DiaPhanHanhChinhTrenBien, DiaPhanHanhChinhTrenBienAdmin)
admin.site.register(DuongRanhGioiHanhChinhTrenBien, DuongRanhGioiHanhChinhTrenBienAdmin)