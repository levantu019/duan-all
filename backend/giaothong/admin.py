from django.contrib import admin
from .models import (
    DuongBo,
    CongGiaoThong,
    DuongBang,
    BaiDapTrucThang,
    BaoHieuHangHaiAIS,
    BenCang,
    CauTau,
    BaoHieuDanLuongHangHaiDuongThuy,
    CacDoiTuongHangHaiHaiVan,
    NhomAuTau
)
from nendialy.admin import CustomGeoAdmin


# 1
class DuongBoAdmin(CustomGeoAdmin, admin.ModelAdmin):
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
class CongGiaoThongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 3
class DuongBangAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 4
class BaiDapTrucThangAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'vitri', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Vị trí bãi đáp')
    def vitri(self, obj):
        return obj.get_vitriBaiDap_display()


# 5
class BaoHieuHangHaiAISAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 6
class BenCangAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class CauTauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiCauTau_display()


# 8
class BaoHieuDanLuongHangHaiDuongThuyAdmin(CustomGeoAdmin, admin.ModelAdmin):
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
class CacDoiTuongHangHaiHaiVanAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'ten')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class NhomAuTauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# Register
admin.site.register(DuongBo, DuongBoAdmin)
admin.site.register(CongGiaoThong, CongGiaoThongAdmin)
admin.site.register(DuongBang, DuongBangAdmin)
admin.site.register(BaiDapTrucThang, BaiDapTrucThangAdmin)
admin.site.register(BaoHieuHangHaiAIS, BaoHieuHangHaiAISAdmin)
admin.site.register(BenCang, BenCangAdmin)
admin.site.register(CauTau, CauTauAdmin)
admin.site.register(BaoHieuDanLuongHangHaiDuongThuy, BaoHieuDanLuongHangHaiDuongThuyAdmin)
admin.site.register(CacDoiTuongHangHaiHaiVan, CacDoiTuongHangHaiHaiVanAdmin)
admin.site.register(NhomAuTau, NhomAuTauAdmin)