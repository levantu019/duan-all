from django.contrib import admin
from .models import (
    KhuDanCu,
    Nha,
    CongTrinhPhuTro,
    KhoiNha,
    DiaDanhDanCu,
    HaTangKyThuatKhac,
    TramKhiTuongThuyVanQuocGia,
    TramQuanTracMoiTruong,
    TramQuanTracTaiNguyenNuoc,
    DuongDayTaiDien,
    CotDien,
    DuongOngDan,
    RanhGioi,
    CongTrinhYTe,
    CongTrinhGiaoDuc,
    CongTrinhTheThao,
    CongTrinhVanHoa,
    CongTrinhThuongMaiDichVu,
    CongTrinhTonGiaoTinNguong,
    TruSoCoQuanNhaNuoc,
    CongTrinhCongNghiep,
    CoSoSanXuatNongLamNghiep,
    KhuChucNangDacThu,
    CongTrinhXuLyChatThai,
    CongTrinhAnNinh,
    CongTrinhQuocPhong
)
from nendialy.admin import CustomGeoAdmin


# 1
class KhuDanCuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaikdc', 'soDan', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loaikdc(self, obj):
        return obj.get_loaiKhuDanCu_display()


# 2
class NhaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai', 'mucdokienco', 'chieuCao', 'soTang', 'ten', 'diaChi')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại nhà')
    def loai(self, obj):
        return obj.get_loaiNha_display()

    @admin.display(description = 'Mức độ kiên cố')
    def mucdokienco(self, obj):
        return obj.get_mucDoKienCo_display()


# 3
class CongTrinhPhuTroAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 4
class KhoiNhaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'nhomst', 'nhomcc')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Nhóm số tầng')
    def nhomst(self, obj):
        return obj.get_nhomSoTang_display()

    @admin.display(description = 'Nhóm chiều cao')
    def nhomcc(self, obj):
        return obj.get_nhomChieuCao_display()


# 5
class DiaDanhDanCuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'dtchung', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Danh từ chung')
    def dtchung(self, obj):
        return obj.get_danhTuChung_display()


# 6
class HaTangKyThuatKhacAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class TramKhiTuongThuyVanQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiTramKhiTuongThuyVan_display()


# 8
class TramQuanTracMoiTruongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 9
class TramQuanTracTaiNguyenNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class DuongDayTaiDienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'dienAp')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 11
class CotDienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 12
class DuongOngDanAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại ống dẫn')
    def loai(self, obj):
        return obj.get_loaiOngDan_display()


# 13
class RanhGioiAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loảianhGioi_display()


# 14
class CongTrinhYTeAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'capyte', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Cấp y tế')
    def capyte(self, obj):
        return obj.get_capYTe_display()


# 15
class CongTrinhGiaoDucAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 16
class CongTrinhTheThaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 17
class CongTrinhVanHoaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'xephang', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Xếp hạng di tích')
    def xephang(self, obj):
        return obj.get_xepHangDiTich_display()


# 18
class CongTrinhThuongMaiDichVuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 19
class CongTrinhTonGiaoTinNguongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'xephang')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Xếp hạng di tích')
    def xephang(self, obj):
        return obj.get_xepHangDiTich_display()


# 20
class TruSoCoQuanNhaNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 21
class CongTrinhCongNghiepAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiCongTrinhCongNghiep_display()


# 22 
class CoSoSanXuatNongLamNghiepAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 23
class KhuChucNangDacThuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 24
class CongTrinhXuLyChatThaiAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 25
class CongTrinhAnNinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 26
class CongTrinhQuocPhongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
admin.site.register(KhuDanCu, KhuDanCuAdmin)
admin.site.register(Nha, NhaAdmin)
admin.site.register(CongTrinhPhuTro, CongTrinhPhuTroAdmin)
admin.site.register(KhoiNha, KhoiNhaAdmin)
admin.site.register(DiaDanhDanCu, DiaDanhDanCuAdmin)
admin.site.register(HaTangKyThuatKhac, HaTangKyThuatKhacAdmin)
admin.site.register(TramKhiTuongThuyVanQuocGia, TramKhiTuongThuyVanQuocGiaAdmin)
admin.site.register(TramQuanTracMoiTruong, TramQuanTracMoiTruongAdmin)
admin.site.register(TramQuanTracTaiNguyenNuoc, TramQuanTracTaiNguyenNuocAdmin)
admin.site.register(DuongDayTaiDien, DuongDayTaiDienAdmin)
admin.site.register(CotDien, CotDienAdmin)
admin.site.register(DuongOngDan, DuongOngDanAdmin)
admin.site.register(RanhGioi, RanhGioiAdmin)
admin.site.register(CongTrinhYTe, CongTrinhYTeAdmin)
admin.site.register(CongTrinhGiaoDuc, CongTrinhGiaoDucAdmin)
admin.site.register(CongTrinhTheThao, CongTrinhTheThaoAdmin)
admin.site.register(CongTrinhVanHoa, CongTrinhVanHoaAdmin)
admin.site.register(CongTrinhThuongMaiDichVu, CongTrinhThuongMaiDichVuAdmin)
admin.site.register(CongTrinhTonGiaoTinNguong, CongTrinhTonGiaoTinNguongAdmin)
admin.site.register(TruSoCoQuanNhaNuoc, TruSoCoQuanNhaNuocAdmin)
admin.site.register(CongTrinhCongNghiep, CongTrinhCongNghiepAdmin)
admin.site.register(CoSoSanXuatNongLamNghiep, CoSoSanXuatNongLamNghiepAdmin)
admin.site.register(KhuChucNangDacThu, KhuChucNangDacThuAdmin)
admin.site.register(CongTrinhXuLyChatThai, CongTrinhXuLyChatThaiAdmin)
admin.site.register(CongTrinhAnNinh, CongTrinhAnNinhAdmin)
admin.site.register(CongTrinhQuocPhong, CongTrinhQuocPhongAdmin)