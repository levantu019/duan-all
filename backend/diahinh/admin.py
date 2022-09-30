from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import DiaHinh as dh
from nendialy.utils import media, form, config

from . import models, meta


# 1
class DiemDoCaoAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DDCMeta, dh.DDC_CHOICES, models.DiemDoCao, have_images=False)
    list_display = ('maNhanDang', 'madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class DuongBinhDoAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DBDMeta, dh.DBD_CHOICES, models.DuongBinhDo, have_images=False)
    list_display = ('maNhanDang', 'madt', 'loaidbd', 'loaikcd', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại đường bình độ')
    def loaidbd(self, obj):
        return obj.get_loaiDuongBinhDo_display()

    @admin.display(description = 'Loại khoảng cao đều')
    def loaikcd(self, obj):
        return obj.get_loaiKhoangCaoDeu_display()


# 3
class ChatDayAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.ChatDayMeta, dh.CD_CHOICES, models.ChatDay, have_images=False)
    list_display = ('maNhanDang', 'madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiChatDay_display()


# 4
class DiemDoSauAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DDSMeta, dh.DDS_CHOICES, models.DiemDoSau, have_images=False)
    list_display = ('maNhanDang', 'madt', 'doSau')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 5
class DuongBinhDoSauAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DBDSMeta, dh.DBDS_CHOICES, models.DuongBinhDoSau, have_images=False)
    list_display = ('maNhanDang', 'madt', 'loaidbd', 'loaikcd', 'doSau')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại đường bình độ')
    def loaidbd(self, obj):
        return obj.get_loaiDuongBinhDo_display()

    @admin.display(description = 'Loại khoảng cao đều')
    def loaikcd(self, obj):
        return obj.get_loaiKhoangCaoDeu_display()


# 6
class DiaHinhDacBietDayBienAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 6.1.
class Surface_DiaHinhDacBietDayBienAdmin(DiaHinhDacBietDayBienAdmin):
    form = form.base_form(meta.Surface_DHDBDBMeta, dh.DHDBDB_CHOICES, models.Surface_DiaHinhDacBietDayBien, models.Curve_DiaHinhDacBietDayBien, have_images=False)

# 6.2.
class Curve_DiaHinhDacBietDayBienAdmin(DiaHinhDacBietDayBienAdmin):
    form = form.base_form(meta.Curve_DHDBDBMeta, dh.DHDBDB_CHOICES, models.Surface_DiaHinhDacBietDayBien, models.Curve_DiaHinhDacBietDayBien, have_images=False)


# 7
class DiaMaoAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DiaMaoMeta, dh.DIAMAO_CHOICES, models.DiaMao, have_images=False)
    list_display = ('maNhanDang', 'madt', 'tenDiaMao', 'dongLucDiaMao', 'tyleDiaMao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 8
class MoHinhSoDoCaoGocLopDiemAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DEMGLPMeta, dh.DEMGLP_CHOICES, models.MoHinhSoDoCaoGocLopDiem, have_images=False)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 9
class MoHinhSoDoCaoGocLopDuongAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DEMGLLMeta, dh.DEMGLL_CHOICES, models.MoHinhSoDoCaoGocLopDuong, have_images=False)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class MoHinhSoDoCaoGocLopVungAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DEMGLAMeta, dh.DEMGLA_CHOICES, models.MoHinhSoDoCaoGocLopVung, have_images=False)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 11
class MoHinhSoDoCaoGocLopVungBienTapAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.DEMDLVBTMeta, dh.DEMGLVBT_CHOICES, models.MoHinhSoDoCaoGocLopVungBienTap, have_images=False)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# # 12
# class LopLuoiTamGiacBatQuyTacAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
#     pass


# # 13
# class LopRasterAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
#     pass


# 14
class HoKhoanDiaChatAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.HKDCMeta, dh.HKDC_CHOICES, models.HoKhoanDiaChat, have_images=True)
    list_display = ('maNhanDang', 'madt', 'tenHoKhoanDiaChat', 'dosauHoKhoanDiaChat')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 15
class SoLieuHKDCAdmin(config.AdminCommon, config.BASE_ADMIN):
    list_display = ('maSolieuHoKhoanDC', 'soHieuMau', 'sohieuTNghiemHKDC', 'lopHKDC')


# 16
class MatCatDienHinhAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.MCDHMeta, dh.MCDHDC_CHOICES, models.MatCatDienHinh, have_images=True)
    list_display = ('maNhanDang', 'madt', 'ten', 'tyLeDung', 'tyLeNgang')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 17
class LoaiDiaChatAdmin(config.AdminCommon, CustomGeoAdmin, config.BASE_ADMIN):
    form = form.base_form(meta.LDCMeta, dh.DIACHAT_CHOICES, models.LoaiDiaChat, have_images=False)
    list_display = ('maNhanDang', 'madt', 'phanHeThachHoc', 'kieuThachHoc', 'kieuDiaChatCongTrinh', 'tuoiDiaChatCongTrinh')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
from django.conf import settings
from .apps import DiahinhConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.DiemDoCao, DiemDoCaoAdmin)
    admin.site.register(models.DuongBinhDo, DuongBinhDoAdmin)
    admin.site.register(models.ChatDay, ChatDayAdmin)
    admin.site.register(models.DiemDoSau, DiemDoSauAdmin)
    admin.site.register(models.DuongBinhDoSau, DuongBinhDoSauAdmin)
    admin.site.register(models.Surface_DiaHinhDacBietDayBien, DiaHinhDacBietDayBienAdmin)
    admin.site.register(models.Curve_DiaHinhDacBietDayBien, DiaHinhDacBietDayBienAdmin)
    admin.site.register(models.DiaMao, DiaMaoAdmin)
    admin.site.register(models.MoHinhSoDoCaoGocLopDiem, MoHinhSoDoCaoGocLopDiemAdmin)
    admin.site.register(models.MoHinhSoDoCaoGocLopDuong, MoHinhSoDoCaoGocLopDuongAdmin)
    admin.site.register(models.MoHinhSoDoCaoGocLopVung, MoHinhSoDoCaoGocLopVungAdmin)
    admin.site.register(models.MoHinhSoDoCaoGocLopVungBienTap, MoHinhSoDoCaoGocLopVungBienTapAdmin)
    # admin.site.register(models.LopLuoiTamGiacBatQuyTac, LopLuoiTamGiacBatQuyTacAdmin)
    # admin.site.register(models.LopRaster, LopRasterAdmin)
    admin.site.register(models.HoKhoanDiaChat, HoKhoanDiaChatAdmin)
    admin.site.register(models.SoLieuHKDC, SoLieuHKDCAdmin)
    admin.site.register(models.MatCatDienHinh, MatCatDienHinhAdmin)
    admin.site.register(models.LoaiDiaChat, LoaiDiaChatAdmin)