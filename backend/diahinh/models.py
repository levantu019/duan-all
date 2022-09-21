from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import DiaHinh as dh
from eav.decorators import register_eav
from multimedia.utils import choices


# -------------------- 4. Địa hình --------------------
# Abstract
class MoHinhSoDoCao(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

class MoHinhSoDoCaoGoc(MoHinhSoDoCao):
    class Meta:
        abstract = True

class DiaChat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True


# Feature: 1. Điểm độ cao
@register_eav()
class DiemDoCao(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Điểm độ cao'
        verbose_name_plural = 'Điểm độ cao'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDC_CHOICES, verbose_name='Mã đối tượng')
    doCao = models.FloatField(verbose_name='Độ cao')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 2. Đường bình độ
@register_eav()
class DuongBinhDo(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đường bình độ'
        verbose_name_plural = 'Đường bình độ'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBD_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBD_LOAI_CHOICES, verbose_name='Loại đường bình độ')
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBD_LOAIKCD_CHOICES, verbose_name='Loại khoảng cao đều')
    doCao = models.FloatField(verbose_name='Độ cao')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 3. Chất đáy
@register_eav()
class ChatDay(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Chất đáy'
        verbose_name_plural = 'Chất đáy'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.CD_CHOICES, verbose_name='Mã đối tượng')
    loaiChatDay = models.IntegerField(choices=dh.CD_LOAI_CHOICES, verbose_name='Loại')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 4. Điểm độ sâu
@register_eav()
class DiemDoSau(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Điểm độ sâu'
        verbose_name_plural = 'Điểm độ sâu'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDS_CHOICES, verbose_name='Mã đối tượng')
    doSau = models.FloatField(verbose_name='Độ sâu')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 5. Đường bình độ sâu
@register_eav()
class DuongBinhDoSau(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đường bình độ sâu'
        verbose_name_plural = 'Đường bình độ sâu'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBDS_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBDS_LOAI_CHOICES, verbose_name='Loại đường bình độ')
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBDS_LOAIKCD_CHOICES, verbose_name='Loại khoảng cao đều')
    doSau = models.FloatField(verbose_name='Độ sâu')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 6. Địa hình đặc biệt đáy biển
class DiaHinhDacBietDayBien(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DHDBDB_CHOICES, verbose_name='Mã đối tượng')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()

# 6.1.
@register_eav()
class Surface_DiaHinhDacBietDayBien(DiaHinhDacBietDayBien):
    class Meta:
        verbose_name = 'Địa hình đặc biệt đáy biển (Surface)'
        verbose_name_plural = 'Địa hình đặc biệt đáy biển (Surface)'
        
    type_model = choices.LDL_KIEU_VUNG

    # Fields
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

# 6.2.
@register_eav()
class Curve_DiaHinhDacBietDayBien(DiaHinhDacBietDayBien):
    class Meta:
        verbose_name = 'Địa hình đặc biệt đáy biển (Curve)'
        verbose_name_plural = 'Địa hình đặc biệt đáy biển (Curve)'
        
    type_model = choices.LDL_KIEU_DUONG

    # Fields
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 7. Địa mạo
@register_eav()
class DiaMao(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Địa mạo'
        verbose_name_plural = 'Địa mạo'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DIAMAO_CHOICES, verbose_name='Mã địa mạo')
    tenDiaMao = models.CharField(max_length=255, verbose_name='Tên')
    dongLucDiaMao = models.CharField(max_length=255, verbose_name='Động lực')
    motaDiaMao = models.CharField(max_length=255, blank=True, verbose_name='Mô tả')
    tyleDiaMao = models.FloatField(verbose_name='Tỷ lệ')
    ghichuDiaMao = models.CharField(max_length=500, blank=True, verbose_name='Ghi chú')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 8. Mô hình số độ cao gốc lớp điểm
@register_eav()
class MoHinhSoDoCaoGocLopDiem(MoHinhSoDoCaoGoc):
    class Meta:
        verbose_name = 'Mô hình số độ cao gốc lớp điểm'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp điểm'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLP_CHOICES, verbose_name='Mã đối tượng')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 9. Mô hình số độ cao gốc lớp đường
@register_eav()
class MoHinhSoDoCaoGocLopDuong(MoHinhSoDoCaoGoc):
    class Meta:
        verbose_name = 'Mô hình số độ cao gốc lớp đường'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp đường'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLL_CHOICES, verbose_name='Mã đối tượng')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 10. Mô hình số độ cao gốc lớp vùng
@register_eav()
class MoHinhSoDoCaoGocLopVung(MoHinhSoDoCaoGoc):
    class Meta:
        verbose_name = 'Mô hình số độ cao gốc lớp vùng'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp vùng'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLA_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# Feature: 11. Mô hình số độ cao gốc lớp vùng biển tập
@register_eav()
class MoHinhSoDoCaoGocLopVungBienTap(MoHinhSoDoCaoGoc):
    class Meta:
        verbose_name = 'Mô hình số độ cao gốc lớp vùng biển tập'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp vùng biển tập'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLVBT_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.get_maDoiTuong_display()


# # Feature: 12. Lớp lưới tam giác bất quy tắc (TIN)
# class LopLuoiTamGiacBatQuyTac(MoHinhSoDoCao):
#     class Meta:
#         verbose_name = 'Lớp lưới tam giác bất quy tắc (TIN)'
#         verbose_name_plural = 'Lớp lưới tam giác bất quy tắc (TIN)'
        
#     # Fields
#     doChinhXac = models.FloatField(verbose_name='Độ chính xác')


# # Feature: 13. Lớp Raster
# class LopRaster(MoHinhSoDoCao):
#     class Meta:
#         verbose_name = 'Lớp Raster'
#         verbose_name_plural = 'Lớp Raster'
        
#     # Fields
#     maDEMRaster = models.CharField(max_length=50, verbose_name='Mã DEM Raster')
#     duongDanDEMRaster = models.CharField(max_length=255, verbose_name='Đường dẫn DEM')
#     moTaDEM = models.CharField(max_length=500, blank=True, verbose_name='Mô tả')
#     # rst


# Feature: 14. Hố khoan địa chất
@register_eav()
class HoKhoanDiaChat(DiaChat):
    class Meta:
        verbose_name = 'Hố khoan địa chất'
        verbose_name_plural = 'Hố khoan địa chất'
        
    type_model = choices.LDL_KIEU_DIEM
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.HKDC_CHOICES, verbose_name='Mã hố khoan')
    tenHoKhoanDiaChat = models.CharField(max_length=255, verbose_name='Tên')
    motaHoKhoanDiaChat = models.CharField(max_length=500, blank=True, verbose_name='Mô tả')
    dosauHoKhoanDiaChat = models.FloatField(verbose_name='Độ sâu')
    # hinhanhHoKhoanDiaChat = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Hình ảnh')
    ghichuHoKhoanDiaChat = models.CharField(max_length=500, blank=True, verbose_name='Ghi chú')
    GM_Point = models.PointField(srid=4756, verbose_name='Hình dạng (Point)')


# Feature: 15. Số liệu hố khoan địa chất
@register_eav()
class SoLieuHKDC(models.Model):
    class Meta:
        verbose_name = 'Số liệu hố khoan địa chất'
        verbose_name_plural = 'Số liệu hố khoan địa chất'
        
    type_model = choices.LDL_KIEU_KHAC
        
    # Fields
    maSolieuHoKhoanDC = models.CharField(max_length=50, verbose_name='Mã số liệu')
    dosauBDLaymauHKDC = models.FloatField(verbose_name='Độ sâu BD lấy mẫu')
    dosauKTLaymauHKDC = models.FloatField(verbose_name='Độ sâu KT lấy mẫu')
    soHieuMau = models.CharField(max_length=500, verbose_name='Số hiệu mẫu')
    sohieuTNghiemHKDC = models.CharField(max_length=500, verbose_name='Số hiệu thí nghiệm')
    lopHKDC = models.CharField(max_length=500, verbose_name='Lớp hố khoan địa chất')
    P10 = models.FloatField(null=True, blank=True)
    P5 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P0_5 = models.FloatField(null=True, blank=True)
    P0_25 = models.FloatField(null=True, blank=True)
    P0_1 = models.FloatField(null=True, blank=True)
    P0_05 = models.FloatField(null=True, blank=True)
    P0_01 = models.FloatField(null=True, blank=True)
    P0_005 = models.FloatField(null=True, blank=True)
    DoAmTuNhien = models.FloatField(null=True, blank=True, verbose_name='Độ ẩm tự nhiên')
    KLTheTichTuNhien = models.FloatField(null=True, blank=True, verbose_name='KL thể tích tự nhiên')
    KLTheTichKho = models.FloatField(null=True, blank=True, verbose_name='KL thể tích kho')
    KLRieng = models.FloatField(null=True, blank=True, verbose_name='KL riêng')
    HeSoRong = models.FloatField(null=True, blank=True, verbose_name='Hệ số rong')
    DoLoRong = models.FloatField(null=True, blank=True, verbose_name='Do lo rong')
    DoBaoHoa = models.FloatField(null=True, blank=True, verbose_name='Độ bão hoà')
    GocNghiKho = models.FloatField(null=True, blank=True, verbose_name='Goc nghi kho')
    GocNghiUot = models.FloatField(null=True, blank=True, verbose_name='Goc nghi uot')
    HSRongLonNhat = models.FloatField(null=True, blank=True, verbose_name='Hệ số rong lớn nhất')
    HSRongNhoNhat = models.FloatField(null=True, blank=True, verbose_name='Hệ số rong nhỏ nhất')
    DungTrongMaxCat = models.FloatField(null=True, blank=True, verbose_name='Dung trong max cat')
    DungTrongMinCat = models.FloatField(null=True, blank=True, verbose_name='Dung trong min cat')
    CDKNKho = models.FloatField(null=True, blank=True, verbose_name='CDKN kho')
    CDKNBaoHoa = models.FloatField(null=True, blank=True, verbose_name='CDKN bão hoà')
    CDKNHeSoMem = models.FloatField(null=True, blank=True, verbose_name='CDKN hệ số mềm')
    TinhCoLyDa_KLTTTN = models.FloatField(null=True, blank=True, verbose_name='Tinh co ly da KLTTTN')
    TinhCoLyDa_DoRong = models.FloatField(null=True, blank=True, verbose_name='Tinh co ly da độ rộng')
    TinhCoLyDa_TyLeKheHo = models.FloatField(null=True, blank=True, verbose_name='Tinh co ly da tỷ lệ khe hở')
    TinhCoLyDa_DoKheHo = models.FloatField(null=True, blank=True, verbose_name='Tinh co ly da do ke ho')
    TinhCoLyDa_KLRieng = models.FloatField(null=True, blank=True, verbose_name='Tinh co ly da KL riêng')
    TNNenDa_Kho = models.FloatField(null=True, blank=True)
    TNNenDa_BaoHoa = models.FloatField(null=True, blank=True)
    TNNenDa_HeSoHM = models.FloatField(null=True, blank=True)
    R0 = models.FloatField(null=True, blank=True)
    E0 = models.FloatField(null=True, blank=True)
    Phanloaidat_HKDC = models.FloatField(null=True, blank=True)
    HKDC = models.ForeignKey(HoKhoanDiaChat, on_delete=models.CASCADE)


# Feature: 16. Mặt cắt điển hình địa chất
@register_eav()
class MatCatDienHinh(DiaChat):
    class Meta:
        verbose_name = 'Mặt cắt điển hình địa chất'
        verbose_name_plural = 'Mặt cắt điển hình địa chất'
        
    type_model = choices.LDL_KIEU_DUONG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.MCDHDC_CHOICES, verbose_name='Mã mặt cắt')
    ten = models.CharField(max_length=255, blank=True, verbose_name='Tên')
    # hinhAnh = models.ImageField(upload_to='images/', verbose_name='Hình ảnh')
    moTa = models.CharField(max_length=500, verbose_name='Mô tả')
    tyLeDung = models.FloatField(verbose_name='Tỷ lệ đứng')
    tyLeNgang = models.FloatField(verbose_name='Tỷ lệ ngang')
    ghiChu = models.CharField(max_length=500, blank=True, verbose_name='Ghi chú')
    GM_Curve = models.LineStringField(srid=4756, verbose_name='Hình dạng (Curve)')


# Feature: 17. Loại Địa chất
@register_eav()
class LoaiDiaChat(DiaChat):
    class Meta:
        verbose_name = 'Loại Địa chất'
        verbose_name_plural = 'Loại Địa chất'
        
    type_model = choices.LDL_KIEU_VUNG
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DIACHAT_CHOICES, verbose_name='Mã loại địa chất')
    phanHeThachHoc = models.CharField(max_length=255, verbose_name='Phân hệ thạch học')
    kieuThachHoc = models.CharField(max_length=255, verbose_name='Kiểu thạch học')
    kieuDiaChatCongTrinh = models.CharField(max_length=255, verbose_name='Kiểu địa chất công trình')
    tuoiDiaChatCongTrinh = models.FloatField(verbose_name='Tuổi địa chất công trình')
    kyHieu = models.CharField(max_length=50, blank=True, verbose_name='Ký hiệu')
    moTa = models.CharField(max_length=500, blank=True, verbose_name='Mô tả')
    GM_Surface = models.PolygonField(srid=4756, verbose_name='Hình dạng (Surface)')