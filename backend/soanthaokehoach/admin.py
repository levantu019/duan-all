from django.contrib import admin

from nendialy.admin import CustomGeoAdmin

from . import models, meta
from .utils import constants, form, media
from .utils.config import ENABLE_EAV, enable_eav_cls


# 
NVDH_cfg = enable_eav_cls(ENABLE_EAV.NVDH)
DiemNVDH_cfg = enable_eav_cls(ENABLE_EAV.DiemNVDH)
TuyenNVDH_cfg = enable_eav_cls(ENABLE_EAV.TuyenNVDH)
VungNVDH_cfg = enable_eav_cls(ENABLE_EAV.VungNVDH)
NVBP_cfg = enable_eav_cls(ENABLE_EAV.NVBP)
PAViTri_cfg = enable_eav_cls(ENABLE_EAV.PhuongAnViTri)
PDPAViTri_cfg = enable_eav_cls(ENABLE_EAV.PheDuyetPhuongAnViTri)
PATuyen_cfg = enable_eav_cls(ENABLE_EAV.PhuongAnTuyen)
PDPATuyen_cfg = enable_eav_cls(ENABLE_EAV.PheDuyetPhuongAnTuyen)
PAVung_cfg = enable_eav_cls(ENABLE_EAV.PhuongAnVung)
PDPAVung_cfg = enable_eav_cls(ENABLE_EAV.PheDuyetPhuongAnVung)
PDCNVBP_cfg = enable_eav_cls(ENABLE_EAV.PheDuyetChungNVBP)
GanLL_cfg = enable_eav_cls(ENABLE_EAV.GanLucLuong)
PDPAGanLL_cfg = enable_eav_cls(ENABLE_EAV.PheDuyetPhuongAnGanLucLuong)


# 1
class NVDHAdmin(CustomGeoAdmin, NVDH_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(NVDH_cfg.BASE_FORM, meta.NVDHMeta, models.NVDH, constants.NVDH)
    list_display = ('tenNVDH', 'chihuyNVDH', 'ngayBDNVDH', 'ngayKTNVDH', 'kieu')

    @admin.display(description = 'Kiểu NVDH')
    def kieu(self, obj):
        return obj.get_kieuNVDH_display()


# 2
class DiemNVDHAdmin(CustomGeoAdmin, DiemNVDH_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(DiemNVDH_cfg.BASE_FORM, meta.DiemNVDHMeta, models.DiemNVDH, constants.DIEM_NVDH)
    list_display = ('tenDiem', 'ngayDiem', 'nvdh')


# 3
class TuyenNVDHAdmin(CustomGeoAdmin, TuyenNVDH_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(TuyenNVDH_cfg.BASE_FORM, meta.TuyenNVDHMeta, models.TuyenNVDH, constants.TUYEN_NVDH)
    list_display = ('tenTuyen', 'ngayTuyen', 'nvdh')


# 4
class VungNVDHAdmin(CustomGeoAdmin, VungNVDH_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(VungNVDH_cfg.BASE_FORM, meta.VungNVDHMeta, models.VungNVDH, constants.VUNG_NVDH)
    list_display = ('tenVung', 'ngayVung', 'nvdh')


# # 5
# class DonViAdmin(CustomGeoAdmin, .BASE_ADMIN):
#     form = form.form_custom_MaNhanDang(meta.DonViMeta, models.DonVi, constants.DONVI)
#     list_display = ('tenDV', 'quanSoDV', 'chucNangDV', 'diaChi')


# 6
class NVBPAdmin(CustomGeoAdmin, NVBP_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(NVBP_cfg.BASE_FORM, meta.NVBPMeta, models.NVBP, constants.NVBP)
    list_display = ('tenNVBP', 'ngayBDNVBP', 'ngayKTNVBP', 'ttnv', 'maNVDH', 'maDV')

    @admin.display(description = 'Trạng thái')
    def ttnv(self, obj):
        return obj.get_trangThaiNVBP_display()


# 7
class PhuongAnViTriAdmin(CustomGeoAdmin, PAViTri_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PAViTri_cfg.BASE_FORM, meta.PAViTriMeta, models.PhuongAnViTri, constants.PA_VTRI)
    list_display = ('tenPAVT', 'nguoiPAVT', 'ngayPAVT', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVT_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangthaiPAVT_display()


# 8
class PheDuyetPhuongAnViTriAdmin(CustomGeoAdmin, PDPAViTri_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PDPAViTri_cfg.BASE_FORM, meta.PDPAViTriMeta, models.PheDuyetPhuongAnViTri, constants.PDPA_VTRI)
    list_display = ('nguoiCMPAVT', 'ngayCMPAVT', 'tt', 'paViTri')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVT_display()


# 9
class PhuongAnTuyenAdmin(CustomGeoAdmin, PATuyen_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PATuyen_cfg.BASE_FORM, meta.PATuyenMeta, models.PhuongAnTuyen, constants.PA_TUYEN)
    list_display = ('tenPATuyen', 'nguoiPATuyen', 'ngayPATuyen', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPATuyen_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPATuyen_display()


# 10
class PheDuyetPhuongAnTuyenAdmin(CustomGeoAdmin, PDPATuyen_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PDPATuyen_cfg.BASE_FORM, meta.PDPATuyenMeta, models.PheDuyetPhuongAnTuyen, constants.PDPA_TUYEN)
    list_display = ('nguoiCMPATuyen', 'ngayCMPATuyen', 'tt', 'paTuyen')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPATuyen_display()


# 11
class PhuongAnVungAdmin(CustomGeoAdmin, PAVung_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PAVung_cfg.BASE_FORM, meta.PAVungMeta, models.PhuongAnVung, constants.PA_VUNG)
    list_display = ('tenPAVung', 'nguoiPAVung', 'ngayPAVung', 'kieu', 'tt', 'nvbp')

    @admin.display(description = 'Kiểu phương án')
    def kieu(self, obj):
        return obj.get_kieuPAVung_display()

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiPAVung_display()


# 12
class PheDuyetPhuongAnVungAdmin(CustomGeoAdmin, PDPAVung_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PDPAVung_cfg.BASE_FORM, meta.PDPAVungMeta, models.PheDuyetPhuongAnVung, constants.PDPA_VUNG)
    list_display = ('nguoiCMPAVung', 'ngayCMPAVung', 'tt', 'paVung')

    @admin.display(description = 'Trạng thái phương án')
    def tt(self, obj):
        return obj.get_trangThaiCMPAVung_display()


# 13
class PheDuyetChungNVBPAdmin(CustomGeoAdmin, PDCNVBP_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PDCNVBP_cfg.BASE_FORM, meta.PDChungNVBPMeta, models.PheDuyetChungNVBP, constants.PD_CHUNG)
    list_display = ('tenCMNVBP', 'nguoiCMNVBP', 'ngayCMNVBP', 'tt')

    @admin.display(description = 'Trạng thái')
    def tt(self, obj):
        return obj.get_trangThaiCMNVBP_display()


# 14
class GanLucLuongAdmin(CustomGeoAdmin, GanLL_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(GanLL_cfg.BASE_FORM, meta.GanLLMeta, models.GanLucLuong, constants.GAN_LL)
    list_display = ('tenGanLL', 'quanSoGanLL', 'donViGanLL', 'thoiGianBDau', 'thoiGianKThuc', 'tt', 'pavt', 'pat', 'pav')

    @admin.display(description = 'Trạng thái lực lượng')
    def tt(self, obj):
        return obj.get_trangThaiLL_display()


# 15
class PheDuyetPhuongAnGanLucLuongAdmin(CustomGeoAdmin, PDPAGanLL_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(PDPAGanLL_cfg.BASE_FORM, meta.PDPAGanLLMeta, models.PheDuyetPhuongAnGanLucLuong, constants.PDPA_GANLL)
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
    # admin.site.register(models.DonVi, DonViAdmin)
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