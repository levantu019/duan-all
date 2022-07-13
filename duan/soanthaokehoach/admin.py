from django.contrib import admin
from .models import(
    NVDH,
    DiemNVDH,
    TuyenNVDH,
    VungNVDH,
    DonVi,
    NVBP,
    PhuongAnViTri,
    PhuongAnTuyen,
    PhuongAnVung,
    PheDuyetPhuongAnViTri,
    PheDuyetPhuongAnTuyen,
    PheDuyetPhuongAnVung,
    PheDuyetChungNVBP,
    GanLucLuong,
    PheDuyetPhuongAnGanLucLuong
)
from nendialy.admin import CustomGeoAdmin


# 1
class NVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenNVDH', 'chihuyNVDH', 'ngayBDNVDH', 'ngayKTNVDH', 'kieu')

    @admin.display(description = 'Kiểu NVDH')
    def kieu(self, obj):
        return obj.get_kieuNVDH_display()


# 2
class DiemNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenDiem', 'ngayDiem', 'nvdh')


# 3
class TuyenNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenTuyen', 'ngayTuyen', 'nvdh')


# 4
class VungNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenVung', 'ngayVung', 'nvdh')


# 5
class DonViAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenDV', 'quanSoDV', 'chucNangDV', 'diaChi')


# 6
class NVBPAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenNVBP', 'ngayBDNVBP', 'ngayKTNVBP', 'ttnv', 'maNVDH', 'maDV')

    @admin.display(description = 'Trạng thái')
    def ttnv(self, obj):
        return obj.get_trangThaiNVBP_display()


# 7
class PhuongAnViTriAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenPAVT', 'nguoiPAVT', 'ngayPAVT', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVT_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangthaiPAVT_display()


# 8
class PheDuyetPhuongAnViTriAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('nguoiCMPAVT', 'ngayCMPAVT', 'tt', 'paViTri')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVT_display()


# 9
class PhuongAnTuyenAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenPATuyen', 'nguoiPATuyen', 'ngayPATuyen', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPATuyen_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPATuyen_display()


# 10
class PheDuyetPhuongAnTuyenAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('nguoiCMPATuyen', 'ngayCMPATuyen', 'tt', 'paTuyen')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPATuyen_display()


# 11
class PhuongAnVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenPAVung', 'nguoiPAVung', 'ngayPAVung', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVung_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPAVung_display()


# 12
class PheDuyetPhuongAnVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('nguoiCMPAVung', 'ngayCMPAVung', 'tt', 'paVung')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVung_display()


# 13
class PheDuyetChungNVBPAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenCMNVBP', 'nguoiCMNVBP', 'ngayCMNVBP', 'tt')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMNVBP_display()


# 14
class GanLucLuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('tenGanLL', 'quanSoGanLL', 'donViGanLL', 'thoiGianBDau', 'thoiGianKThuc', 'tt', 'pavt', 'pat', 'pav')

    @admin.display(description = 'Trạng thái lực lượng')
    def tt(self, obj):
        return obj.get_trangThaiLL_display()


# 15
class PheDuyetPhuongAnGanLucLuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('cmDonViGanLL', 'cmThoiGianBDau', 'cmThoiGianKThuc', 'tt', 'ganLL')

    @admin.display(description = 'Trạng thái phê duyệt')
    def tt(self, obj):
        return obj.get_trangThaiCMGanLL_display()


admin.site.register(NVDH, NVDHAdmin)
admin.site.register(DiemNVDH, DiemNVDHAdmin)
admin.site.register(TuyenNVDH, TuyenNVDHAdmin)
admin.site.register(VungNVDH, VungNVDHAdmin)
admin.site.register(DonVi, DonViAdmin)
admin.site.register(NVBP, NVBPAdmin)
admin.site.register(PhuongAnViTri, PhuongAnViTriAdmin)
admin.site.register(PhuongAnTuyen, PhuongAnTuyenAdmin)
admin.site.register(PhuongAnVung, PhuongAnVungAdmin)
admin.site.register(PheDuyetPhuongAnViTri, PheDuyetPhuongAnViTriAdmin)
admin.site.register(PheDuyetPhuongAnTuyen, PheDuyetPhuongAnTuyenAdmin)
admin.site.register(PheDuyetPhuongAnVung, PheDuyetPhuongAnVungAdmin)
admin.site.register(PheDuyetChungNVBP, PheDuyetChungNVBPAdmin)
admin.site.register(GanLucLuong, GanLucLuongAdmin)
admin.site.register(PheDuyetPhuongAnGanLucLuong, PheDuyetPhuongAnGanLucLuongAdmin)