from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import DiaHinh as dh
from nendialy.utils import media, form

from . import models, meta


# 1
class DiemDoCaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDCMeta, dh.DDC_CHOICES, models.DiemDoCao)
    list_display = ('maNhanDang', 'madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class DuongBinhDoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DBDMeta, dh.DBD_CHOICES, models.DuongBinhDo)
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
class ChatDayAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.ChatDayMeta, dh.CD_CHOICES, models.ChatDay)
    list_display = ('maNhanDang', 'madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiChatDay_display()


# 4
class DiemDoSauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDSMeta, dh.DDS_CHOICES, models.DiemDoSau)
    list_display = ('maNhanDang', 'madt', 'doSau')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 5
class DuongBinhDoSauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DBDSMeta, dh.DBDS_CHOICES, models.DuongBinhDoSau)
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
class DiaHinhDacBietDayBienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 6.1.
class Surface_DiaHinhDacBietDayBienAdmin(DiaHinhDacBietDayBienAdmin):
    form = form.base_form(meta.Surface_DHDBDBMeta, dh.DHDBDB_CHOICES, models.Surface_DiaHinhDacBietDayBien, models.Curve_DiaHinhDacBietDayBien)

# 6.2.
class Curve_DiaHinhDacBietDayBienAdmin(DiaHinhDacBietDayBienAdmin):
    form = form.base_form(meta.Curve_DHDBDBMeta, dh.DHDBDB_CHOICES, models.Surface_DiaHinhDacBietDayBien, models.Curve_DiaHinhDacBietDayBien)


# 7
class DiaMaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DiaMaoMeta, dh.DIAMAO_CHOICES, models.DiaMao)
    list_display = ('maNhanDang', 'madt', 'tenDiaMao', 'dongLucDiaMao', 'tyleDiaMao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 8
class MoHinhSoDoCaoGocLopDiemAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DEMGLPMeta, dh.DEMGLP_CHOICES, models.MoHinhSoDoCaoGocLopDiem)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 9
class MoHinhSoDoCaoGocLopDuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DEMGLLMeta, dh.DEMGLL_CHOICES, models.MoHinhSoDoCaoGocLopDuong)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class MoHinhSoDoCaoGocLopVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DEMGLAMeta, dh.DEMGLA_CHOICES, models.MoHinhSoDoCaoGocLopVung)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 11
class MoHinhSoDoCaoGocLopVungBienTapAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DEMDLVBTMeta, dh.DEMGLVBT_CHOICES, models.MoHinhSoDoCaoGocLopVungBienTap)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# # 12
# class LopLuoiTamGiacBatQuyTacAdmin(CustomGeoAdmin, admin.ModelAdmin):
#     pass


# # 13
# class LopRasterAdmin(CustomGeoAdmin, admin.ModelAdmin):
#     pass


# 14
class HoKhoanDiaChatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.HKDCMeta, dh.HKDC_CHOICES, models.HoKhoanDiaChat)
    list_display = ('maNhanDang', 'madt', 'tenHoKhoanDiaChat', 'dosauHoKhoanDiaChat')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 15
class SoLieuHKDCAdmin(admin.ModelAdmin):
    list_display = ('maSolieuHoKhoanDC', 'soHieuMau', 'sohieuTNghiemHKDC', 'lopHKDC')


# 16
class MatCatDienHinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.MCDHMeta, dh.MCDHDC_CHOICES, models.MatCatDienHinh)
    list_display = ('maNhanDang', 'madt', 'ten', 'tyLeDung', 'tyLeNgang')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 17
class LoaiDiaChatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.LDCMeta, dh.DIACHAT_CHOICES, models.LoaiDiaChat)
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