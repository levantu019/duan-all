from django.contrib import admin
from .models import (
    BienDao,
    Dao,
    BaiBoi,
    BaiDaDuoiNuoc,
    NguonNuoc,
    DiemDoCaoMucNuoc,
    DuongBoNuoc,
    DuongMepNuoc,
    RanhGioiNuocMatQuyUoc,
    BoKeBoCap,
    KenhMuong,
    TramThuThapKTTV,
    ThamSoKTTV,
    SongGioDongChay,
    ThamSoNuoc
)
from nendialy.admin import CustomGeoAdmin


# 1
class BienDaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()
        

# 2
class DaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'loaittxl')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại trạng thái xuất lô')
    def loaittxl(self, obj):
        return obj.get_loaiTrangThaiXuatLo_display()


# 3
class BaiBoiAdmin(CustomGeoAdmin, admin.ModelAdmin):
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


# 4
class BaiDaDuoiNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'ttxl')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Trạng thái xuất lô')
    def ttxl(self, obj):
        return obj.get_trangThaiXuatLo_display()


# 5
class NguonNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiNguonNuoc_display()


# 6
class DiemDoCaoMucNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class DuongBoNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
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
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiDuongMepNuoc_display()


# 9
class RanhGioiNuocMatQuyUocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loảianhGioiNuocMatQuyUoc_display()


# 10
class BoKeBoCapAdmin(CustomGeoAdmin, admin.ModelAdmin):
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
    list_display = ('madt', 'ten', 'loaihtsd', 'chieuRong')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại hiện trạng sử dụng')
    def loaihtsd(self, obj):
        return obj.get_loaiHienTrangSuDung_display()


# 12
class TramThuThapKTTVAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('ma', 'tenTram', 'loai', 'kieutt')

    @admin.display(description = 'Mã trạm')
    def ma(self, obj):
        return obj.get_maTramKTTV_display()

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
admin.site.register(BienDao, BienDaoAdmin)
admin.site.register(Dao, DaoAdmin)
admin.site.register(BaiBoi, BaiBoiAdmin)
admin.site.register(BaiDaDuoiNuoc, BaiDaDuoiNuocAdmin)
admin.site.register(NguonNuoc, NguonNuocAdmin)
admin.site.register(DiemDoCaoMucNuoc, DiemDoCaoMucNuocAdmin)
admin.site.register(DuongBoNuoc, DuongMepNuocAdmin)
admin.site.register(DuongMepNuoc, DuongMepNuocAdmin)
admin.site.register(RanhGioiNuocMatQuyUoc, RanhGioiNuocMatQuyUocAdmin)
admin.site.register(BoKeBoCap, BoKeBoCapAdmin)
admin.site.register(KenhMuong, KenhMuongAdmin)
admin.site.register(TramThuThapKTTV, TramThuThapKTTVAdmin)
admin.site.register(ThamSoKTTV, ThamSoKTTVAdmin)
admin.site.register(SongGioDongChay, SongGioDongChayAdmin)
admin.site.register(ThamSoNuoc, ThamSoNuocAdmin)
