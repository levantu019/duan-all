from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import DiaHinh as dh


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
class DiemDoCao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Điểm độ cao'
        verbose_name_plural = 'Điểm độ cao'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDC_CHOICES, verbose_name='Mã đối tượng')
    doCao = models.FloatField(verbose_name='Độ cao')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 2. Đường bình độ
class DuongBinhDo(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường bình độ'
        verbose_name_plural = 'Đường bình độ'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBD_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBD_LOAI_CHOICES, verbose_name='Loại đường bình độ')
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBD_LOAIKCD_CHOICES, verbose_name='Loại khoảng cao đều')
    doCao = models.FloatField(verbose_name='Độ cao')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 3. Chất đáy
class ChatDay(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Chất đáy'
        verbose_name_plural = 'Chất đáy'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.CD_CHOICES, verbose_name='Mã đối tượng')
    loaiChatDay = models.IntegerField(choices=dh.CD_LOAI_CHOICES, verbose_name='Loại')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 4. Điểm độ sâu
class DiemDoSau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Điểm độ sâu'
        verbose_name_plural = 'Điểm độ sâu'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDS_CHOICES, verbose_name='Mã đối tượng')
    doSau = models.FloatField(verbose_name='Độ sâu')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 5. Đường bình độ sâu
class DuongBinhDoSau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Đường bình độ sâu'
        verbose_name_plural = 'Đường bình độ sâu'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBDS_CHOICES, verbose_name='Mã đối tượng')
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBDS_LOAI_CHOICES, verbose_name='Loại đường bình độ')
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBDS_LOAIKCD_CHOICES, verbose_name='Loại khoảng cao đều')
    doSau = models.FloatField(verbose_name='Độ sâu')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 6. Địa hình đặc biệt đáy biển
class DiaHinhDacBietDayBien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Địa hình đặc biệt đáy biển'
        verbose_name_plural = 'Địa hình đặc biệt đáy biển'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DHDBDB_CHOICES, verbose_name='Mã đối tượng')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 7. Địa mạo
class DiaMao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        verbose_name = 'Địa mạo'
        verbose_name_plural = 'Địa mạo'
        
    # Fields
    maDiaMao = models.CharField(max_length=50, verbose_name='Mã địa mạo')
    tenDiaMao = models.CharField(max_length=255, verbose_name='Tên')
    dongLucDiaMao = models.CharField(max_length=255, verbose_name='Động lực')
    motaDiaMao = models.CharField(max_length=255, null=True, blank=True, verbose_name='Mô tả')
    tyleDiaMao = models.FloatField(verbose_name='Tỷ lệ')
    ghichuDiaMao = models.CharField(max_length=500, null=True, blank=True, verbose_name='Ghi chú')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 8. Mô hình số độ cao gốc lớp điểm
class MoHinhSoDoCaoGocLopDiem(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        verbose_name = 'Mô hình số độ cao gốc lớp điểm'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp điểm'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLP_CHOICES, verbose_name='Mã đối tượng')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 9. Mô hình số độ cao gốc lớp đường
class MoHinhSoDoCaoGocLopDuong(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        verbose_name = 'Mô hình số độ cao gốc lớp đường'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp đường'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLL_CHOICES, verbose_name='Mã đối tượng')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 10. Mô hình số độ cao gốc lớp vùng
class MoHinhSoDoCaoGocLopVung(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        verbose_name = 'Mô hình số độ cao gốc lớp vùng'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp vùng'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLA_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 11. Mô hình số độ cao gốc lớp vùng biển tập
class MoHinhSoDoCaoGocLopVungBienTap(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        verbose_name = 'Mô hình số độ cao gốc lớp vùng biển tập'
        verbose_name_plural = 'Mô hình số độ cao gốc lớp vùng biển tập'
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLVBT_CHOICES, verbose_name='Mã đối tượng')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 12. Lớp lưới tam giác bất quy tắc (TIN)
class LopLuoiTamGiacBatQuyTac(MoHinhSoDoCao):
    class Meta:
        ordering = ['id']
        verbose_name = 'Lớp lưới tam giác bất quy tắc (TIN)'
        verbose_name_plural = 'Lớp lưới tam giác bất quy tắc (TIN)'
        
    # Fields
    doChinhXac = models.FloatField(verbose_name='Độ chính xác')
    # rst = 


# Feature: 13. Lớp Raster
class LopRaster(MoHinhSoDoCao):
    class Meta:
        ordering = ['id']
        verbose_name = 'Lớp Raster'
        verbose_name_plural = 'Lớp Raster'
        
    # Fields
    maDEMRaster = models.CharField(max_length=50, verbose_name='Mã DEM Raster')
    duongDanDEMRaster = models.CharField(max_length=255, verbose_name='Đường dẫn DEM')
    moTaDEM = models.CharField(max_length=500, null=True, blank=True, verbose_name='Mô tả')
    # rst


# Feature: 14. Hố khoan địa chất
class HoKhoanDiaChat(DiaChat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Hố khoan địa chất'
        verbose_name_plural = 'Hố khoan địa chất'
        
    # Fields
    maHoKhoanDiaChat = models.CharField(max_length=50, verbose_name='Mã hố khoan')
    tenHoKhoanDiaChat = models.CharField(max_length=255, verbose_name='Tên')
    motaHoKhoanDiaChat = models.CharField(max_length=500, null=True, blank=True, verbose_name='Mô tả')
    dosauHoKhoanDiaChat = models.FloatField(verbose_name='Độ sâu')
    hinhanhHoKhoanDiaChat = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Hình ảnh')
    ghichuHoKhoanDiaChat = models.CharField(max_length=500, null=True, blank=True, verbose_name='Ghi chú')
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 15. Số liệu hố khoan địa chất
class SoLieuHKDC(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name = 'Số liệu hố khoan địa chất'
        verbose_name_plural = 'Số liệu hố khoan địa chất'
        
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
class MatCatDienHinh(DiaChat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Mặt cắt điển hình địa chất'
        verbose_name_plural = 'Mặt cắt điển hình địa chất'
        
    # Fields
    maMCDienHinh = models.CharField(max_length=50, verbose_name='Mã mặt cắt')
    ten = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tên')
    hinhAnh = models.ImageField(upload_to='images/', verbose_name='Hình ảnh')
    moTa = models.CharField(max_length=500, verbose_name='Mô tả')
    tyLeDung = models.FloatField(verbose_name='Tỷ lệ đứng')
    tyLeNgang = models.FloatField(verbose_name='Tỷ lệ ngang')
    ghiChu = models.CharField(max_length=500, null=True, blank=True, verbose_name='Ghi chú')
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 17. Loại Địa chất
class LoaiDiaChat(DiaChat):
    class Meta:
        ordering = ['id']
        verbose_name = 'Loại Địa chất'
        verbose_name_plural = 'Loại Địa chất'
        
    # Fields
    maLoaiDC = models.CharField(max_length=50, verbose_name='Mã loại địa chất')
    phanHeThachHoc = models.CharField(max_length=255, verbose_name='Phân hệ thạch học')
    kieuThachHoc = models.CharField(max_length=255, verbose_name='Kiểu thạch học')
    kieuDiaChatCongTrinh = models.CharField(max_length=255, verbose_name='Kiểu địa chất công trình')
    tuoiDiaChatCongTrinh = models.FloatField(verbose_name='Tuổi địa chất công trình')
    kyHieu = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ký hiệu')
    moTa = models.CharField(max_length=500, null=True, blank=True, verbose_name='Mô tả')
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)