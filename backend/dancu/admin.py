from django.contrib import admin

from nendialy.admin import CustomGeoAdmin
from nendialy.choices import DanCu as dc
from nendialy.utils import media, form

from . import models, meta


# 1
class KhuDanCuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.KDCMeta, dc.KDC_CHOICES, models.KhuDanCu)
    list_display = ('maNhanDang', 'madt', 'loaikdc', 'soDan', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loaikdc(self, obj):
        return obj.get_loaiKhuDanCu_display()


# 2
class NhaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'loai', 'mucdokienco', 'chieuCao', 'soTang')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại nhà')
    def loai(self, obj):
        return obj.get_loaiNha_display()

    @admin.display(description = 'Mức độ kiên cố')
    def mucdokienco(self, obj):
        return obj.get_mucDoKienCo_display()

# 2.1.
class Surface_NhaAdmin(NhaAdmin):
    form = form.base_form(meta.Surface_NMeta, dc.NHA_CHOICES, models.Surface_Nha, models.Point_Nha)

# 2.2.
class Point_NhaAdmin(NhaAdmin):
    form = form.base_form(meta.Point_NMeta, dc.NHA_CHOICES, models.Surface_Nha, models.Point_Nha)


# 3
class CongTrinhPhuTroAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 3.1.
class Surface_CongTrinhPhuTroAdmin(CongTrinhPhuTroAdmin):
    form = form.base_form(meta.Surface_CTPTMeta, dc.CTPT_CHOICES, models.Surface_CongTrinhPhuTro, models.Curve_CongTrinhPhuTro)

# 3.2.
class Curve_CongTrinhPhuTroAdmin(CongTrinhPhuTroAdmin):
    form = form.base_form(meta.Curve_CTPTMeta, dc.CTPT_CHOICES, models.Surface_CongTrinhPhuTro, models.Curve_CongTrinhPhuTro)


# 4
class KhoiNhaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.KhoiNhaMeta, dc.KN_CHOICES, models.KhoiNha)
    list_display = ('maNhanDang', 'madt', 'nhomst', 'nhomcc')

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
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDDCMeta, dc.DD_CHOICES, models.DiaDanhDanCu)
    list_display = ('maNhanDang', 'madt', 'dtchung', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Danh từ chung')
    def dtchung(self, obj):
        return obj.get_danhTuChung_display()


# 6
class HaTangKyThuatKhacAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 6.1.
class Surface_HaTangKyThuatKhacAdmin(HaTangKyThuatKhacAdmin):
    form = form.base_form(meta.Surface_HTKTKMeta, dc.HTKTK_CHOICES, models.Surface_HaTangKyThuatKhac, models.Point_HaTangKyThuatKhac)

# 6.2.
class Point_HaTangKyThuatKhacAdmin(HaTangKyThuatKhacAdmin):
    form = form.base_form(meta.Point_HTKTKMeta, dc.HTKTK_CHOICES, models.Surface_HaTangKyThuatKhac, models.Point_HaTangKyThuatKhac)


# 7
class TramKhiTuongThuyVanQuocGiaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TKTTVQGMeta, dc.TKTTVQG_CHOICES, models.TramKhiTuongThuyVanQuocGia)
    list_display = ('maNhanDang', 'madt', 'loai', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiTramKhiTuongThuyVan_display()


# 8
class TramQuanTracMoiTruongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TQTMTMeta, dc.TQTMT_CHOICES, models.TramQuanTracMoiTruong)
    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 9
class TramQuanTracTaiNguyenNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.TQTTNNMeta, dc.TQTTNN_CHOICES, models.TramQuanTracTaiNguyenNuoc)
    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class DuongDayTaiDienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DDTDMeta, dc.DDTD_CHOICES, models.DuongDayTaiDien)
    list_display = ('maNhanDang', 'madt', 'dienAp')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 11
class CotDienAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.CotDienMeta, dc.CD_CHOICES, models.CotDien)
    list_display = ('maNhanDang', 'madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 12
class DuongOngDanAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.DODMeta, dc.DOD_CHOICES, models.DuongOngDan)
    list_display = ('maNhanDang', 'madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại ống dẫn')
    def loai(self, obj):
        return obj.get_loaiOngDan_display()


# 13
class RanhGioiAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.RanhGioiMeta, dc.RG_LOAI_CHOICES, models.RanhGioi)
    list_display = ('maNhanDang', 'madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiRanhGioi_display()


# 14
class CongTrinhYTeAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'capyte', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Cấp y tế')
    def capyte(self, obj):
        return obj.get_capYTe_display()

# 14.1.
class Surface_CongTrinhYTeAdmin(CongTrinhYTeAdmin):
    form = form.base_form(meta.Surface_CTYTMeta, dc.CTYT_CHOICES, models.Surface_CongTrinhYTe, models.Point_CongTrinhYTe)

# 14.1.
class Point_CongTrinhYTeAdmin(CongTrinhYTeAdmin):
    form = form.base_form(meta.Point_CTYTMeta, dc.CTYT_CHOICES, models.Surface_CongTrinhYTe, models.Point_CongTrinhYTe)


# 15
class CongTrinhGiaoDucAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 15.1.
class Surface_CongTrinhGiaoDucAdmin(CongTrinhGiaoDucAdmin):
    form = form.base_form(meta.Surface_CTGDMeta, dc.CTGD_CHOICES, models.Surface_CongTrinhGiaoDuc, models.Point_CongTrinhGiaoDuc)

# 15.2.
class Point_CongTrinhGiaoDucAdmin(CongTrinhGiaoDucAdmin):
    form = form.base_form(meta.Point_CTGDMeta, dc.CTGD_CHOICES, models.Surface_CongTrinhGiaoDuc, models.Point_CongTrinhGiaoDuc)


# 16
class CongTrinhTheThaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 16.1.
class Surface_CongTrinhTheThaoAdmin(CongTrinhTheThaoAdmin):
    form = form.base_form(meta.Surface_CTTTMeta, dc.CTTT_CHOICES, models.Surface_CongTrinhTheThao, models.Point_CongTrinhTheThao)

# 16.2.
class Point_CongTrinhTheThaoAdmin(CongTrinhTheThaoAdmin):
    form = form.base_form(meta.Point_CTTTMeta, dc.CTTT_CHOICES, models.Surface_CongTrinhTheThao, models.Point_CongTrinhTheThao)


# 17
class CongTrinhVanHoaAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten', 'xephang', 'chieuCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Xếp hạng di tích')
    def xephang(self, obj):
        return obj.get_xepHangDiTich_display()

# 17.1.
class Surface_CongTrinhVanHoaAdmin(CongTrinhVanHoaAdmin):
    form = form.base_form(meta.Surface_NMeta, dc.CTVH_CHOICES, models.Surface_CongTrinhVanHoa, models.Point_CongTrinhVanHoa)

# 17.2.
class Point_CongTrinhVanHoaAdmin(CongTrinhVanHoaAdmin):
    form = form.base_form(meta.Point_CTVHMeta, dc.CTVH_CHOICES, models.Surface_CongTrinhVanHoa, models.Point_CongTrinhVanHoa)


# 18
class CongTrinhThuongMaiDichVuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 18.1.
class Surface_CongTrinhThuongMaiDichVuAdmin(CongTrinhThuongMaiDichVuAdmin):
    form = form.base_form(meta.Surface_CTTMDVMeta, dc.CTTMDV_CHOICES, models.Surface_CongTrinhThuongMaiDichVu, models.Point_CongTrinhThuongMaiDichVu)

# 18.2.
class Point_CongTrinhThuongMaiDichVuAdmin(CongTrinhThuongMaiDichVuAdmin):
    form = form.base_form(meta.Point_CTTMDVMeta, dc.CTTMDV_CHOICES, models.Surface_CongTrinhThuongMaiDichVu, models.Point_CongTrinhThuongMaiDichVu)


# 19
class CongTrinhTonGiaoTinNguongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten', 'xephang')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Xếp hạng di tích')
    def xephang(self, obj):
        return obj.get_xepHangDiTich_display()

# 19.1.
class Surface_CongTrinhTonGiaoTinNguongAdmin(CongTrinhTonGiaoTinNguongAdmin):
    form = form.base_form(meta.Surface_CTTGTNMeta, dc.CTTGTN_CHOICES, models.Surface_CongTrinhTonGiaoTinNguong, models.Point_CongTrinhTonGiaoTinNguong)

# 19.2.
class Point_CongTrinhTonGiaoTinNguongAdmin(CongTrinhTonGiaoTinNguongAdmin):
    form = form.base_form(meta.Point_CTTGTNMeta, dc.CTTGTN_CHOICES, models.Surface_CongTrinhTonGiaoTinNguong, models.Point_CongTrinhTonGiaoTinNguong)


# 20
class TruSoCoQuanNhaNuocAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 20.1.
class Surface_TruSoCoQuanNhaNuocAdmin(TruSoCoQuanNhaNuocAdmin):
    form = form.base_form(meta.Surface_TSCQNNMeta, dc.TSCQNN_CHOICES, models.Surface_TruSoCoQuanNhaNuoc, models.Point_TruSoCoQuanNhaNuoc)

# 20.2.
class Point_TruSoCoQuanNhaNuocAdmin(TruSoCoQuanNhaNuocAdmin):
    form = form.base_form(meta.Point_TSCQNNMeta, dc.TSCQNN_CHOICES, models.Surface_TruSoCoQuanNhaNuoc, models.Point_TruSoCoQuanNhaNuoc)


# 21
class CongTrinhCongNghiepAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiCongTrinhCongNghiep_display()

# 21.1.
class Surface_CongTrinhCongNghiepAdmin(CongTrinhCongNghiepAdmin):
    form = form.base_form(meta.Surface_CTCNMeta, dc.CTCN_CHOICES, models.Surface_CongTrinhCongNghiep, models.Curve_CongTrinhCongNghiep, models.Point_CongTrinhCongNghiep)

# 21.2.
class Curve_CongTrinhCongNghiepAdmin(CongTrinhCongNghiepAdmin):
    form = form.base_form(meta.Curve_CTCNMeta, dc.CTCN_CHOICES, models.Surface_CongTrinhCongNghiep, models.Curve_CongTrinhCongNghiep, models.Point_CongTrinhCongNghiep)

# 21.3.
class Point_CongTrinhCongNghiepAdmin(CongTrinhCongNghiepAdmin):
    form = form.base_form(meta.Point_CTCNMeta, dc.CTCN_CHOICES, models.Surface_CongTrinhCongNghiep, models.Curve_CongTrinhCongNghiep, models.Point_CongTrinhCongNghiep)


# 22 
class CoSoSanXuatNongLamNghiepAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 22.1.
class Surface_CoSoSanXuatNongLamNghiepAdmin(CoSoSanXuatNongLamNghiepAdmin):
    form = form.base_form(meta.Surface_CSSXNLNMeta, dc.CSSXNLN_CHOICES, models.Surface_CoSoSanXuatNongLamNghiep, models.Point_CoSoSanXuatNongLamNghiep)

# 22.2.
class Point_CoSoSanXuatNongLamNghiepAdmin(CoSoSanXuatNongLamNghiepAdmin):
    form = form.base_form(meta.Point_CSSXNLNMeta, dc.CSSXNLN_CHOICES, models.Surface_CoSoSanXuatNongLamNghiep, models.Point_CoSoSanXuatNongLamNghiep)


# 23
class KhuChucNangDacThuAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    form = form.base_form(meta.KCNDTMeta, dc.KCNDT_CHOICES, models.KhuChucNangDacThu)
    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 24
class CongTrinhXuLyChatThaiAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 24.1.
class Surface_CongTrinhXuLyChatThaiAdmin(CongTrinhXuLyChatThaiAdmin):
    form = form.base_form(meta.Surface_CTXLCTMeta, dc.CTXLCT_CHOICES, models.Surface_CongTrinhXuLyChatThai, models.Point_CongTrinhXuLyChatThai)

# 24.2.
class Point_CongTrinhXuLyChatThaiAdmin(CongTrinhXuLyChatThaiAdmin):
    form = form.base_form(meta.Point_CTXLCTMeta, dc.CTXLCT_CHOICES, models.Surface_CongTrinhXuLyChatThai, models.Point_CongTrinhXuLyChatThai)


# 25
class CongTrinhAnNinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 25.1.
class Surface_CongTrinhAnNinhAdmin(CongTrinhAnNinhAdmin):
    form = form.base_form(meta.Surface_CTANMeta, dc.CTAN_CHOICES, models.Surface_CongTrinhAnNinh, models.Point_CongTrinhAnNinh)

# 25.2.
class Point_CongTrinhAnNinhAdmin(CongTrinhAnNinhAdmin):
    form = form.base_form(meta.Point_CTANMeta, dc.CTAN_CHOICES, models.Surface_CongTrinhAnNinh, models.Point_CongTrinhAnNinh)


# 26
class CongTrinhQuocPhongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    class Media:
        js = media.JS_ADMIN_BASE

    list_display = ('maNhanDang', 'madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

# 26.1.
class Surface_CongTrinhQuocPhongAdmin(CongTrinhQuocPhongAdmin):
    form = form.base_form(meta.Surface_CTQPMeta, dc.CTQP_CHOICES, models.Surface_CongTrinhQuocPhong, models.Point_CongTrinhQuocPhong)

# 26.2.
class Point_CongTrinhQuocPhongAdmin(CongTrinhQuocPhongAdmin):
    form = form.base_form(meta.Point_CTQPMeta, dc.CTQP_CHOICES, models.Surface_CongTrinhQuocPhong, models.Point_CongTrinhQuocPhong)


# Register
admin.site.register(models.KhuDanCu, KhuDanCuAdmin)
admin.site.register(models.Surface_Nha, Surface_NhaAdmin)
admin.site.register(models.Point_Nha, Point_NhaAdmin)
admin.site.register(models.Surface_CongTrinhPhuTro, Surface_CongTrinhPhuTroAdmin)
admin.site.register(models.Curve_CongTrinhPhuTro, Curve_CongTrinhPhuTroAdmin)
admin.site.register(models.KhoiNha, KhoiNhaAdmin)
admin.site.register(models.DiaDanhDanCu, DiaDanhDanCuAdmin)
admin.site.register(models.Surface_HaTangKyThuatKhac, Surface_HaTangKyThuatKhacAdmin)
admin.site.register(models.Point_HaTangKyThuatKhac, Point_HaTangKyThuatKhacAdmin)
admin.site.register(models.TramKhiTuongThuyVanQuocGia, TramKhiTuongThuyVanQuocGiaAdmin)
admin.site.register(models.TramQuanTracMoiTruong, TramQuanTracMoiTruongAdmin)
admin.site.register(models.TramQuanTracTaiNguyenNuoc, TramQuanTracTaiNguyenNuocAdmin)
admin.site.register(models.DuongDayTaiDien, DuongDayTaiDienAdmin)
admin.site.register(models.CotDien, CotDienAdmin)
admin.site.register(models.DuongOngDan, DuongOngDanAdmin)
admin.site.register(models.RanhGioi, RanhGioiAdmin)
admin.site.register(models.Surface_CongTrinhYTe, Surface_CongTrinhYTeAdmin)
admin.site.register(models.Point_CongTrinhYTe, Point_CongTrinhYTeAdmin)
admin.site.register(models.Surface_CongTrinhGiaoDuc, Surface_CongTrinhGiaoDucAdmin)
admin.site.register(models.Point_CongTrinhGiaoDuc, Point_CongTrinhGiaoDucAdmin)
admin.site.register(models.Surface_CongTrinhTheThao, Surface_CongTrinhTheThaoAdmin)
admin.site.register(models.Point_CongTrinhTheThao, Point_CongTrinhTheThaoAdmin)
admin.site.register(models.Surface_CongTrinhVanHoa, Surface_CongTrinhVanHoaAdmin)
admin.site.register(models.Point_CongTrinhVanHoa, Point_CongTrinhVanHoaAdmin)
admin.site.register(models.Surface_CongTrinhThuongMaiDichVu, Surface_CongTrinhThuongMaiDichVuAdmin)
admin.site.register(models.Point_CongTrinhThuongMaiDichVu, Point_CongTrinhThuongMaiDichVuAdmin)
admin.site.register(models.Surface_CongTrinhTonGiaoTinNguong, Surface_CongTrinhTonGiaoTinNguongAdmin)
admin.site.register(models.Point_CongTrinhTonGiaoTinNguong, Point_CongTrinhTonGiaoTinNguongAdmin)
admin.site.register(models.Surface_TruSoCoQuanNhaNuoc, Surface_TruSoCoQuanNhaNuocAdmin)
admin.site.register(models.Point_TruSoCoQuanNhaNuoc, Point_TruSoCoQuanNhaNuocAdmin)
admin.site.register(models.Surface_CongTrinhCongNghiep, Surface_CongTrinhCongNghiepAdmin)
admin.site.register(models.Curve_CongTrinhCongNghiep, Point_CongTrinhCongNghiepAdmin)
admin.site.register(models.Point_CongTrinhCongNghiep, CongTrinhCongNghiepAdmin)
admin.site.register(models.Surface_CoSoSanXuatNongLamNghiep, Surface_CoSoSanXuatNongLamNghiepAdmin)
admin.site.register(models.Point_CoSoSanXuatNongLamNghiep, Point_CoSoSanXuatNongLamNghiepAdmin)
admin.site.register(models.KhuChucNangDacThu, KhuChucNangDacThuAdmin)
admin.site.register(models.Surface_CongTrinhXuLyChatThai, Surface_CongTrinhXuLyChatThaiAdmin)
admin.site.register(models.Point_CongTrinhXuLyChatThai, Point_CongTrinhXuLyChatThaiAdmin)
admin.site.register(models.Surface_CongTrinhAnNinh, Surface_CongTrinhAnNinhAdmin)
admin.site.register(models.Point_CongTrinhAnNinh, Point_CongTrinhAnNinhAdmin)
admin.site.register(models.Surface_CongTrinhQuocPhong, Surface_CongTrinhQuocPhongAdmin)
admin.site.register(models.Point_CongTrinhQuocPhong, Point_CongTrinhQuocPhongAdmin)