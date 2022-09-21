from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import GiaoThong as gt
from nendialy.utils import media, form, config

from . import models, meta


# 1
class DuongBoAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DuongBoMeta, gt.DB_CHOICES, models.DuongBo, have_images=False)
    list_display = ('madt', 'ten', 'loai', 'capkt', 'loaicltm', 'loaihtsd', 'chieu', 'vitri', 'soLanDuong', 'chieuRong')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại đường bộ')
    def loai(self, obj):
        return obj.get_loaiDuongBo_display()

    @admin.display(description = 'Cấp kỹ thuật')
    def capkt(self, obj):
        return obj.get_capKyThuat_display()

    @admin.display(description = 'Loại chất liệu trải mặt')
    def loaicltm(self, obj):
        return obj.get_loaiChatLieuTraiMat_display()

    @admin.display(description = 'Loại hiện trạng sử dụng')
    def loaihtsd(self, obj):
        return obj.get_loaiHienTrangSuDung_display()

    @admin.display(description = 'Chiều xe chạy')
    def chieu(self, obj):
        return obj.get_chiễuChay_display()

    @admin.display(description = 'Vị trí')
    def vitri(self, obj):
        return obj.get_viTri_display()


# 2
class CongGiaoThongAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.Curve_CongGTMeta, gt.CGT_CHOICES, models.Curve_CongGiaoThong, models.Point_CongGiaoThong, have_images=False)
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 2.1.
class Curve_CongGiaoThongAdmin(CongGiaoThongAdmin):
    form = form.base_form(meta.Curve_CongGTMeta, gt.CGT_CHOICES, models.Curve_CongGiaoThong, models.Point_CongGiaoThong, have_images=False)

# 2.2.
class Point_CongGiaoThongAdmin(CongGiaoThongAdmin):
    form = form.base_form(meta.Point_CongGTMeta, gt.CGT_CHOICES, models.Curve_CongGiaoThong, models.Point_CongGiaoThong, have_images=False)


# 3
class DuongBangAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DBANGMeta, gt.DBANG_CHOICES, models.DuongBang, have_images=False)
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 4
class BaiDapTrucThangAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BDTTMeta, gt.BDTT_CHOICES, models.BaiDapTrucThang, have_images=False)
    list_display = ('madt', 'vitri', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Vị trí bãi đáp')
    def vitri(self, obj):
        return obj.get_vitriBaiDap_display()


# 5
class BaoHieuHangHaiAISAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BHHHAISMeta, gt.BHHHAIS_CHOICES, models.BaoHieuHangHaiAIS, have_images=False)
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 6
class BenCangAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BenCangMeta, gt.BC_CHOICES, models.BenCang, have_images=False)
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class CauTauAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiCauTau_display()

# 7.1.
class Surface_CauTauAdmin(CauTauAdmin):
    form = form.base_form(meta.Surface_CauTauMeta, gt.CT_CHOICES, models.Surface_CauTau, models.Curve_CauTau, have_images=False)

# 7.2.
class Curve_CauTauAdmin(CauTauAdmin):
    form = form.base_form(meta.Curve_CauTauMeta, gt.CT_CHOICES, models.Surface_CauTau, models.Curve_CauTau, have_images=False)


# 8
class BaoHieuDanLuongHangHaiDuongThuyAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.BHDLHHDTMeta, gt.BHDLHHDT_CHOICES, models.BaoHieuDanLuongHangHaiDuongThuy, have_images=False)
    list_display = ('madt', 'coDen', 'huong', 'hinhdang', 'mausac', 'phoihopmau')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Hướng báo hiệu')
    def huong(self, obj):
        return obj.get_huongBaoHieu_display()

    @admin.display(description = 'Hình dạng')
    def hinhdang(self, obj):
        return obj.get_hinhDang_display()

    @admin.display(description = 'Màu sắc')
    def mausac(self, obj):
        return obj.get_mauSac_display()

    @admin.display(description = 'Phối hợp màu sắc')
    def phoihopmau(self, obj):
        return obj.get_phoiHopMauSac_display()


# 9
class CacDoiTuongHangHaiHaiVanAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 9.1.
class Surface_CacDoiTuongHangHaiHaiVanAdmin(CacDoiTuongHangHaiHaiVanAdmin):
    form = form.base_form(meta.Surface_CDTHHHVMeta, gt.CDTHHHV_CHOICES, models.Surface_CacDoiTuongHangHaiHaiVan, models.Point_CacDoiTuongHangHaiHaiVan, have_images=False)

# 9.2.
class Point_CacDoiTuongHangHaiHaiVanAdmin(CacDoiTuongHangHaiHaiVanAdmin):
    form = form.base_form(meta.Point_CDTHHHVMeta, gt.CDTHHHV_CHOICES, models.Surface_CacDoiTuongHangHaiHaiVan, models.Point_CacDoiTuongHangHaiHaiVan, have_images=False)


# 10
class NhomAuTauAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 10.1.
class Surface_NhomAuTauAdmin(NhomAuTauAdmin):
    form = form.base_form(meta.Surface_NhomAuTauMeta, gt.NAT_CHOICES, models.Surface_NhomAuTau, models.Curve_NhomAuTau, have_images=False)

# 10.2.
class Curve_NhomAuTauAdmin(NhomAuTauAdmin):
    form = form.base_form(meta.Curve_NhomAuTauMeta, gt.NAT_CHOICES, models.Surface_NhomAuTau, models.Curve_NhomAuTau, have_images=False)


# Register
from django.conf import settings
from .apps import GiaothongConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.DuongBo, DuongBoAdmin)
    admin.site.register(models.Curve_CongGiaoThong, Curve_CongGiaoThongAdmin)
    admin.site.register(models.Point_CongGiaoThong, Point_CongGiaoThongAdmin)
    admin.site.register(models.DuongBang, DuongBangAdmin)
    admin.site.register(models.BaiDapTrucThang, BaiDapTrucThangAdmin)
    admin.site.register(models.BaoHieuHangHaiAIS, BaoHieuHangHaiAISAdmin)
    admin.site.register(models.BenCang, BenCangAdmin)
    admin.site.register(models.Surface_CauTau, Surface_CauTauAdmin)
    admin.site.register(models.Curve_CauTau, Curve_CauTauAdmin)
    admin.site.register(models.BaoHieuDanLuongHangHaiDuongThuy, BaoHieuDanLuongHangHaiDuongThuyAdmin)
    admin.site.register(models.Surface_CacDoiTuongHangHaiHaiVan, Surface_CacDoiTuongHangHaiHaiVanAdmin)
    admin.site.register(models.Point_CacDoiTuongHangHaiHaiVan, Point_CacDoiTuongHangHaiHaiVanAdmin)
    admin.site.register(models.Surface_NhomAuTau, Surface_NhomAuTauAdmin)
    admin.site.register(models.Curve_NhomAuTau, Curve_NhomAuTauAdmin)