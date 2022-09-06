from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import ThuyVan as tv
from nendialy.utils import media, form

from . import models, meta


# 1
class BienDaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 1.1.
class Surface_BienDaoAdmin(BienDaoAdmin):
    form = form.base_form(meta.Surface_BienDaoMeta, tv.BD_CHOICES, models.Surface_BienDao, models.Point_BienDao)

# 1.2.
class Point_BienDaoAdmin(BienDaoAdmin):
    form = form.base_form(meta.Point_BienDaoMeta, tv.BD_CHOICES, models.Surface_BienDao, models.Point_BienDao)



# 2
class DaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten', 'loaittxl')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại trạng thái xuất lô')
    def loaittxl(self, obj):
        return obj.get_loaiTrangThaiXuatLo_display()

# 2.1.
class Surface_DaoAdmin(DaoAdmin):
    form = form.base_form(meta.Surface_DaoMeta, tv.DAO_CHOICES, models.Surface_Dao, models.Point_Dao)

# 2.2.
class Point_DaoAdmin(DaoAdmin):
    form = form.base_form(meta.Point_DaoMeta, tv.DAO_CHOICES, models.Surface_Dao, models.Point_Dao)


# 3
class BaiBoiAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten', 'loai', 'ttxl')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiBaiBoi_display()

    @admin.display(description = 'Trạng thái xuất lô')
    def ttxl(self, obj):
        return obj.get_trangThaiXuatLo_display()

# 3.1.
class Surface_BaiBoiAdmin(BaiBoiAdmin):
    form = form.base_form(meta.Surface_BaiBoiMeta, tv.BB_CHOICES, models.Surface_BaiBoi, models.Point_BaiBoi)

# 3.2.
class Point_BaiBoiAdmin(BaiBoiAdmin):
    form = form.base_form(meta.Point_BaiBoiMeta, tv.BB_CHOICES, models.Surface_BaiBoi, models.Point_BaiBoi)


# 4
class BaiDaDuoiNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten', 'ttxl')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Trạng thái xuất lô')
    def ttxl(self, obj):
        return obj.get_trangThaiXuatLo_display()

# 4.1.
class Surface_BaiDaDuoiNuocAdmin(BaiDaDuoiNuocAdmin):
    form = form.base_form(meta.Surface_BDDNMeta, tv.BDDN_CHOICES, models.Surface_BaiDaDuoiNuoc, models.Point_BaiDaDuoiNuoc)

# 4.2.
class Point_BaiDaDuoiNuocAdmin(BaiDaDuoiNuocAdmin):
    form = form.base_form(meta.Point_BDDNMeta, tv.BDDN_CHOICES, models.Surface_BaiDaDuoiNuoc, models.Point_BaiDaDuoiNuoc)


# 5
class NguonNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiNguonNuoc_display()

# 5.1.
class Surface_NguonNuocAdmin(NguonNuocAdmin):
    form = form.base_form(meta.Surface_NguonNuocMeta, tv.NN_CHOICES, models.Surface_NguonNuoc, models.Point_NguonNuoc)

# 5.2.
class Point_NguonNuocAdmin(NguonNuocAdmin):
    form = form.base_form(meta.Point_NguonNuocMeta, tv.NN_CHOICES, models.Surface_NguonNuoc, models.Point_NguonNuoc)



# 6
class DiemDoCaoMucNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDCMNMeta, tv.DDCMN_CHOICES, models.DiemDoCaoMucNuoc)
    list_display = ('madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class DuongBoNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DBNMeta, tv.DBN_CHOICES, models.DuongBoNuoc)
    list_display = ('madt', 'loai', 'loaitt')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiDuongBoNuoc_display()

    @admin.display(description = 'Loại trạng thái')
    def loaitt(self, obj):
        return obj.get_loaiTrangThaiDuongBoNuoc_display()


# 8
class DuongMepNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DMNMeta, tv.DMN_CHOICES, models.DuongMepNuoc)
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiDuongMepNuoc_display()


# 9
class RanhGioiNuocMatQuyUocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.RGNMQUMeta, tv.RGNMQU_CHOICES, models.RanhGioiNuocMatQuyUoc)
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loảianhGioiNuocMatQuyUoc_display()


# 10
class BoKeBoCapAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.BKBCMeta, tv.BKBC_CHOICES, models.BoKeBoCap)
    list_display = ('madt', 'ten', 'loaicl', 'loaitp')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại chất liệu')
    def loaicl(self, obj):
        return obj.get_loaiChatLieu_display()

    @admin.display(description = 'Loại thành phần')
    def loaitp(self, obj):
        return obj.get_loaiThanhPhan_display()


# 11
class KenhMuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('madt', 'ten', 'loaihtsd', 'chieuRong')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại hiện trạng sử dụng')
    def loaihtsd(self, obj):
        return obj.get_loaiHienTrangSuDung_display()

# 11.1.
class Surface_KenhMuongAdmin(KenhMuongAdmin):
    form = form.base_form(meta.Surface_KenhMuongMeta, tv.KM_CHOICES, models.Surface_KenhMuong, models.Curve_KenhMuong)

# 11.2.
class Curve_KenhMuongAdmin(KenhMuongAdmin):
    form = form.base_form(meta.Curve_KenhMuongMeta, tv.KM_CHOICES, models.Surface_KenhMuong, models.Curve_KenhMuong)


# 12
class TramThuThapKTTVAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TTTTTTVMeta, tv.TTTKTTV_CHOICES, models.TramThuThapKTTV)
    list_display = ('ma', 'tenTram', 'loai', 'kieutt')

    @admin.display(description = 'Mã trạm')
    def ma(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiTramThuThapKTTV_display()

    @admin.display(description = 'Kiểu thu thập')
    def kieutt(self, obj):
        return obj.get_kieuThuThapKTTV_display()


# 13
class ThamSoKTTVAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('ma', 'thoigianThuThap', 'ts', 'tramKTTV')

    @admin.display(description = 'Mã tham số')
    def ma(self, obj):
        return obj.get_maThamSoKTTV_display()

    @admin.display(description = 'Tham số')
    def ts(self, obj):
        return obj.get_thamSo_display()


# 14
class SongGioDongChayAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('ma', 'thoigianThuThap', 'ts', 'tramKTTV')

    @admin.display(description = 'Mã')
    def ma(self, obj):
        return obj.get_maSongGioDongChay_display()

    @admin.display(description = 'Tham số')
    def ts(self, obj):
        return obj.get_thamSo_display()


# 15
class ThamSoNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('ma', 'thoigianThuThap', 'tangds', 'ts', 'tramKTTV')

    @admin.display(description = 'Mã')
    def ma(self, obj):
        return obj.get_maThamSoNuoc_display()

    @admin.display(description = 'Tầng độ sâu')
    def tangds(self, obj):
        return obj.get_tangDoSau_display()

    @admin.display(description = 'Tham số')
    def ts(self, obj):
        return obj.get_thamSo_display()


# Register
from django.conf import settings
from .apps import ThuyvanConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.Surface_BienDao, Surface_BienDaoAdmin)
    admin.site.register(models.Point_BienDao, Point_BienDaoAdmin)
    admin.site.register(models.Surface_Dao, Surface_DaoAdmin)
    admin.site.register(models.Point_Dao, Point_DaoAdmin)
    admin.site.register(models.Surface_BaiBoi, Surface_BaiBoiAdmin)
    admin.site.register(models.Point_BaiBoi, Point_BaiBoiAdmin)
    admin.site.register(models.Surface_BaiDaDuoiNuoc, Surface_BaiDaDuoiNuocAdmin)
    admin.site.register(models.Point_BaiDaDuoiNuoc, Point_BaiDaDuoiNuocAdmin)
    admin.site.register(models.Surface_NguonNuoc, Surface_NguonNuocAdmin)
    admin.site.register(models.Point_NguonNuoc, Point_NguonNuocAdmin)
    admin.site.register(models.DiemDoCaoMucNuoc, DiemDoCaoMucNuocAdmin)
    admin.site.register(models.DuongBoNuoc, DuongMepNuocAdmin)
    admin.site.register(models.DuongMepNuoc, DuongMepNuocAdmin)
    admin.site.register(models.RanhGioiNuocMatQuyUoc, RanhGioiNuocMatQuyUocAdmin)
    admin.site.register(models.BoKeBoCap, BoKeBoCapAdmin)
    admin.site.register(models.Surface_KenhMuong, Surface_KenhMuongAdmin)
    admin.site.register(models.Curve_KenhMuong, Curve_KenhMuongAdmin)
    admin.site.register(models.TramThuThapKTTV, TramThuThapKTTVAdmin)
    admin.site.register(models.ThamSoKTTV, ThamSoKTTVAdmin)
    admin.site.register(models.SongGioDongChay, SongGioDongChayAdmin)
    admin.site.register(models.ThamSoNuoc, ThamSoNuocAdmin)
