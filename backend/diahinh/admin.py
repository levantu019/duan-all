from django.contrib import admin
from .models import (
    DiemDoCao,
    DuongBinhDo,
    ChatDay,
    DiemDoSau,
    DuongBinhDoSau,
    DiaHinhDacBietDayBien,
    DiaMao,
    MoHinhSoDoCaoGocLopDiem,
    MoHinhSoDoCaoGocLopDuong,
    MoHinhSoDoCaoGocLopVung,
    MoHinhSoDoCaoGocLopVungBienTap,
    LopLuoiTamGiacBatQuyTac,
    LopRaster,
    HoKhoanDiaChat,
    SoLieuHKDC,
    MatCatDienHinh,
    LoaiDiaChat
)
from nendialy.admin import CustomGeoAdmin


# 1
class DiemDoCaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'doCao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 2
class DuongBinhDoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaidbd', 'loaikcd', 'doCao')

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
    list_display = ('madt', 'loai')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()

    @admin.display(description = 'Loại')
    def loai(self, obj):
        return obj.get_loaiChatDay_display()


# 4
class DiemDoSauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'doSau')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 5
class DuongBinhDoSauAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'loaidbd', 'loaikcd', 'doSau')

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
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 7
class DiaMaoAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt', 'tenDiaMao', 'dongLucDiaMao', 'motaDiaMao', 'tyleDiaMao', 'ghichuDiaMao')

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 8
class MoHinhSoDoCaoGocLopDiemAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 9
class MoHinhSoDoCaoGocLopDuongAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 10
class MoHinhSoDoCaoGocLopVungAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 11
class MoHinhSoDoCaoGocLopVungBienTapAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('madt',)

    @admin.display(description = 'Mã đối tượng')
    def madt(self, obj):
        return obj.get_maDoiTuong_display()


# 12
class LopLuoiTamGiacBatQuyTacAdmin(CustomGeoAdmin, admin.ModelAdmin):
    pass


# 13
class LopRasterAdmin(CustomGeoAdmin, admin.ModelAdmin):
    pass


# 14
class HoKhoanDiaChatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('maHoKhoanDiaChat', 'tenHoKhoanDiaChat', 'motaHoKhoanDiaChat', 'dosauHoKhoanDiaChat')


# 15
class SoLieuHKDCAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('maSolieuHoKhoanDC', 'soHieuMau', 'sohieuTNghiemHKDC', 'lopHKDC')


# 16
class MatCatDienHinhAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('maMCDienHinh', 'ten', 'tyLeDung', 'tyLeNgang')


# 17
class LoaiDiaChatAdmin(CustomGeoAdmin, admin.ModelAdmin):
    list_display = ('maLoaiDC', 'phanHeThachHoc', 'kieuThachHoc', 'kieuDiaChatCongTrinh', 'tuoiDiaChatCongTrinh')


# Register
admin.site.register(DiemDoCao, DiemDoCaoAdmin)
admin.site.register(DuongBinhDo, DuongBinhDoAdmin)
admin.site.register(ChatDay, ChatDayAdmin)
admin.site.register(DiemDoSau, DiemDoSauAdmin)
admin.site.register(DuongBinhDoSau, DuongBinhDoSauAdmin)
admin.site.register(DiaHinhDacBietDayBien, DiaHinhDacBietDayBienAdmin)
admin.site.register(DiaMao, DiaMaoAdmin)
admin.site.register(MoHinhSoDoCaoGocLopDiem, MoHinhSoDoCaoGocLopDiemAdmin)
admin.site.register(MoHinhSoDoCaoGocLopDuong, MoHinhSoDoCaoGocLopDuongAdmin)
admin.site.register(MoHinhSoDoCaoGocLopVung, MoHinhSoDoCaoGocLopVungAdmin)
admin.site.register(MoHinhSoDoCaoGocLopVungBienTap, MoHinhSoDoCaoGocLopVungBienTapAdmin)
admin.site.register(LopLuoiTamGiacBatQuyTac, LopLuoiTamGiacBatQuyTacAdmin)
admin.site.register(LopRaster, LopRasterAdmin)
admin.site.register(HoKhoanDiaChat, HoKhoanDiaChatAdmin)
admin.site.register(SoLieuHKDC, SoLieuHKDCAdmin)
admin.site.register(MatCatDienHinh, MatCatDienHinhAdmin)
admin.site.register(LoaiDiaChat, LoaiDiaChatAdmin)