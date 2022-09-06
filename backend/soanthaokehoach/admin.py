from django.contrib import admin

from nendialy.admin import CustomGeoAdmin

from .utils import constants, form

from . import models, meta


# 1
class NVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.NVDHMeta, models.NVDH, constants.NVDH)
    list_display = ('tenNVDH', 'chihuyNVDH', 'ngayBDNVDH', 'ngayKTNVDH', 'kieu')

    @admin.display(description = 'Kiểu NVDH')
    def kieu(self, obj):
        return obj.get_kieuNVDH_display()


# 2
class DiemNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.DiemNVDHMeta, models.DiemNVDH, constants.DIEM_NVDH)
    list_display = ('tenDiem', 'ngayDiem', 'nvdh')


# 3
class TuyenNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.TuyenNVDHMeta, models.TuyenNVDH, constants.TUYEN_NVDH)
    list_display = ('tenTuyen', 'ngayTuyen', 'nvdh')


# 4
class VungNVDHAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.VungNVDHMeta, models.VungNVDH, constants.VUNG_NVDH)
    list_display = ('tenVung', 'ngayVung', 'nvdh')


# 5
class DonViAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.DonViMeta, models.DonVi, constants.DONVI)
    list_display = ('tenDV', 'quanSoDV', 'chucNangDV', 'diaChi')


# 6
class NVBPAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.NVBPMeta, models.NVBP, constants.NVBP)
    list_display = ('tenNVBP', 'ngayBDNVBP', 'ngayKTNVBP', 'ttnv', 'maNVDH', 'maDV')

    @admin.display(description = 'Trạng thái')
    def ttnv(self, obj):
        return obj.get_trangThaiNVBP_display()


# 7
class PhuongAnViTriAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PAViTriMeta, models.PhuongAnViTri, constants.PA_VTRI)
    list_display = ('tenPAVT', 'nguoiPAVT', 'ngayPAVT', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVT_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangthaiPAVT_display()


# 8
class PheDuyetPhuongAnViTriAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PDPAViTriMeta, models.PheDuyetPhuongAnViTri, constants.PDPA_VTRI)
    list_display = ('nguoiCMPAVT', 'ngayCMPAVT', 'tt', 'paViTri')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVT_display()


# 9
class PhuongAnTuyenAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PATuyenMeta, models.PhuongAnTuyen, constants.PA_TUYEN)
    list_display = ('tenPATuyen', 'nguoiPATuyen', 'ngayPATuyen', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPATuyen_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPATuyen_display()


# 10
class PheDuyetPhuongAnTuyenAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PDPATuyenMeta, models.PheDuyetPhuongAnTuyen, constants.PDPA_TUYEN)
    list_display = ('nguoiCMPATuyen', 'ngayCMPATuyen', 'tt', 'paTuyen')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPATuyen_display()


# 11
class PhuongAnVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PAVungMeta, models.PhuongAnVung, constants.PA_VUNG)
    list_display = ('tenPAVung', 'nguoiPAVung', 'ngayPAVung', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVung_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPAVung_display()


# 12
class PheDuyetPhuongAnVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PDPAVungMeta, models.PheDuyetPhuongAnVung, constants.PDPA_VUNG)
    list_display = ('nguoiCMPAVung', 'ngayCMPAVung', 'tt', 'paVung')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVung_display()


# 13
class PheDuyetChungNVBPAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PDChungNVBPMeta, models.PheDuyetChungNVBP, constants.PD_CHUNG)
    list_display = ('tenCMNVBP', 'nguoiCMNVBP', 'ngayCMNVBP', 'tt')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMNVBP_display()


# 14
class GanLucLuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.GanLLMeta, models.GanLucLuong, constants.GAN_LL)
    list_display = ('tenGanLL', 'quanSoGanLL', 'donViGanLL', 'thoiGianBDau', 'thoiGianKThuc', 'tt', 'pavt', 'pat', 'pav')

    @admin.display(description = 'Trạng thái lực lượng')
    def tt(self, obj):
        return obj.get_trangThaiLL_display()


# 15
class PheDuyetPhuongAnGanLucLuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    form = form.form_custom_MaNhanDang(meta.PDPAGanLLMeta, models.PheDuyetPhuongAnGanLucLuong, constants.PDPA_GANLL)
    list_display = ('cmDonViGanLL', 'cmThoiGianBDau', 'cmThoiGianKThuc', 'tt', 'ganLL')

    @admin.display(description = 'Trạng thái phê duyệt')
    def tt(self, obj):
        return obj.get_trangThaiCMGanLL_display()


# Register
from django.conf import settings
from .apps import SoanthaokehoachConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.NVDH, NVDHAdmin)
    admin.site.register(models.DiemNVDH, DiemNVDHAdmin)
    admin.site.register(models.TuyenNVDH, TuyenNVDHAdmin)
    admin.site.register(models.VungNVDH, VungNVDHAdmin)
    admin.site.register(models.DonVi, DonViAdmin)
    admin.site.register(models.NVBP, NVBPAdmin)
    admin.site.register(models.PhuongAnViTri, PhuongAnViTriAdmin)
    admin.site.register(models.PhuongAnTuyen, PhuongAnTuyenAdmin)
    admin.site.register(models.PhuongAnVung, PhuongAnVungAdmin)
    admin.site.register(models.PheDuyetPhuongAnViTri, PheDuyetPhuongAnViTriAdmin)
    admin.site.register(models.PheDuyetPhuongAnTuyen, PheDuyetPhuongAnTuyenAdmin)
    admin.site.register(models.PheDuyetPhuongAnVung, PheDuyetPhuongAnVungAdmin)
    admin.site.register(models.PheDuyetChungNVBP, PheDuyetChungNVBPAdmin)
    admin.site.register(models.GanLucLuong, GanLucLuongAdmin)
    admin.site.register(models.PheDuyetPhuongAnGanLucLuong, PheDuyetPhuongAnGanLucLuongAdmin)