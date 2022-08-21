from django.contrib.gis.db import models as models_gis
from django.db import models
from nendialy.choices import SoanThaoKeHoach as stkh

# 1. Bảng Nhiệm vụ điều hành
class NVDH(models_gis.Model):
    class Meta:
        ordering = ['maNVDH']
        verbose_name = 'Nhiệm vụ điều hành'
        verbose_name_plural = 'Nhiệm vụ điều hành'

    # Fields
    maNVDH = models_gis.AutoField(primary_key=True, verbose_name='Mã NVDH')
    tenNVDH = models_gis.CharField(verbose_name = 'Tên NVDH', max_length=100)
    moTaNV = models_gis.TextField(verbose_name='Mô tả NVDH', max_length=1000, null=True, blank=True)
    chihuyNVDH = models_gis.CharField(verbose_name='Chỉ huy NVDH', max_length=50)
    ngayBDNVDH = models_gis.DateField(verbose_name='Ngày bắt đầu NVDH', null=True, blank=True)
    ngayKTNVDH = models_gis.DateField(verbose_name='Ngày kết thúc NVDH', null=True, blank=True)
    vanbanNVDH = models.FileField(verbose_name='Văn bản NVDH', upload_to='files/', null=True, blank=True)
    kieuNVDH = models_gis.IntegerField(verbose_name='Kiểu NVDH', choices=stkh.NVDH_KIEU_CHOICES)

    # 
    def __str__(self):
        return self.tenNVDH


# 2. Bảng Điểm NVDH
class DiemNVDH(models_gis.Model):
    class Meta:
        ordering = ['maDiem']
        verbose_name = 'Điểm NVDH'
        verbose_name_plural = 'Điểm NVDH'

    # Fields
    maDiem = models_gis.AutoField(verbose_name='Mã điểm', primary_key=True)
    tenDiem = models_gis.CharField(verbose_name='Tên điểm', max_length=100)
    moTaDiem = models_gis.TextField(verbose_name='Mô tả điểm', max_length=500, null=True, blank=True)
    ngayDiem = models_gis.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoDiem = models_gis.PointField(verbose_name='Điểm', srid=4756)
    nvdh = models_gis.ForeignKey(NVDH, on_delete=models_gis.CASCADE, related_name='fk_diemnvdh_nvdh', verbose_name='Nhiệm vụ điều hành')


# 3. Bảng Tuyến NVDH
class TuyenNVDH(models_gis.Model):
    class Meta:
        ordering = ['maTuyen']
        verbose_name = 'Tuyến NVDH'
        verbose_name_plural = 'Tuyến NVDH'

    # Fields
    maTuyen = models_gis.AutoField(verbose_name='Mã tuyến', primary_key=True)
    tenTuyen = models_gis.CharField(max_length=100)
    moTaTuyen = models_gis.TextField(verbose_name='Mô tả tuyến', max_length=500, null=True, blank=True)
    ngayTuyen = models_gis.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoTuyen = models_gis.LineStringField(verbose_name='Tuyến', srid=4756)
    nvdh = models_gis.ForeignKey(NVDH, on_delete=models_gis.CASCADE, related_name='fk_tuyennvdh_nvdh', verbose_name='Nhiệm vụ điều hành')


# 4. Bảng Vùng NVDH
class VungNVDH(models_gis.Model):
    class Meta:
        ordering = ['maVung']
        verbose_name = 'Vùng NVDH'
        verbose_name_plural = 'Vùng NVDH'

    # Fields
    maVung = models_gis.AutoField(verbose_name='Mã vùng', primary_key=True)
    tenVung = models_gis.CharField(max_length=100)
    moTaVung = models_gis.TextField(verbose_name='Mô tả vùng', max_length=500, null=True, blank=True)
    ngayVung = models_gis.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoVung = models_gis.PolygonField(verbose_name='Vùng', srid=4756)
    nvdh = models_gis.ForeignKey(NVDH, on_delete=models_gis.CASCADE, related_name='fk_vungnvdh_nvdh', verbose_name='Nhiệm vụ điều hành')


# 5. Bảng đơn vị
class DonVi(models_gis.Model):
    class Meta:
        ordering = ['maDV']
        verbose_name = 'Đơn vị'
        verbose_name_plural = 'Đơn vị'

    # Fields
    maDV = models_gis.AutoField(verbose_name='Mã đơn vị', primary_key=True)
    tenDV = models_gis.CharField(verbose_name='Tên đơn vị', max_length=100)
    quanSoDV = models_gis.IntegerField(verbose_name='Quân số đơn vị', null=True, blank=True)
    chucNangDV = models_gis.TextField(verbose_name='Chức năng', max_length=500, null=True, blank=True)
    diaChi = models_gis.CharField(verbose_name='Địa chỉ', max_length=100, null=True, blank=True)
    geoDV = models_gis.PointField(verbose_name='Vị trí', srid=4756)

    # 
    def __str__(self):
        return self.tenDV


# 6. Bảng Nhiệm vụ bộ phận
class NVBP(models_gis.Model):
    class Meta:
        ordering = ['maNVBP']
        verbose_name = 'Nhiệm vụ bộ phận'
        verbose_name_plural = 'Nhiệm vụ bộ phận'

    # Fields
    maNVBP = models_gis.AutoField(verbose_name='Mã NVBP', primary_key=True)
    tenNVBP = models_gis.CharField(verbose_name='Tên NVBP', max_length=100)
    moTaNVBP = models_gis.TextField(verbose_name='Mô tả NVBP', max_length=5000)
    ngayBDNVBP = models_gis.DateField(verbose_name='Ngày bắt đầu', null=True, blank=True)
    ngayKTNVBP = models_gis.DateField(verbose_name='Ngày kết thúc', null=True, blank=True)
    trangThaiNVBP = models_gis.IntegerField(verbose_name='Trạng thái nhiệm vụ', choices=stkh.NVBP_TT_CHOICES)
    maNVDH = models_gis.ForeignKey(NVDH, on_delete=models_gis.CASCADE, related_name='fk_nvbp_nvdh', verbose_name='Nhiệm vụ điều hành')
    maDV = models_gis.ForeignKey(DonVi, on_delete=models_gis.CASCADE, related_name='fk_nvbp_dv', verbose_name='Đơn vị')

    # 
    def __str__(self):
        return self.tenNVBP


# 7. Bảng Phương án vị trí
class PhuongAnViTri(models_gis.Model):
    class Meta:
        ordering = ['maPAVT']
        verbose_name = 'Phương án vị trí'
        verbose_name_plural = 'Phương án vị trí'

    # Fields
    maPAVT = models_gis.AutoField(verbose_name='Mã phương án', primary_key=True)
    tenPAVT = models_gis.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPAVT = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPAVT = models_gis.CharField(verbose_name='Người thực hiện', max_length=50, null=True, blank=True)
    ngayPAVT = models_gis.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPAVT = models_gis.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAVT_KIEU_CHOICES)
    trangthaiPAVT = models_gis.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPAVT = models_gis.PointField(verbose_name='Vị trí', srid=4756)
    nvbp = models_gis.ForeignKey(NVBP, on_delete=models_gis.CASCADE, related_name='fk_pavt_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def __str__(self):
        return self.tenPAVT


# 8. Bảng phê duyệt phương án vị trí
class PheDuyetPhuongAnViTri(models_gis.Model):
    class Meta:
        ordering = ['maCMPAVT']
        verbose_name = 'Phê duyệt phương án vị trí'
        verbose_name_plural = 'Phê duyệt phương án vị trí'

    # Fields
    maCMPAVT = models_gis.AutoField(verbose_name='Mã phê duyệt', primary_key=True)
    moTaCMPAVT = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPAVT = models_gis.CharField(verbose_name='Người phê duyệt', max_length=50, null=True, blank=True)
    ngayCMPAVT = models_gis.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPAVT = models_gis.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPAVT = models_gis.PointField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paViTri = models_gis.ForeignKey(PhuongAnViTri, on_delete=models_gis.CASCADE, related_name='fk_pdpavt_pavt', verbose_name='Phương án vị trí')


# 9. Bảng Phương án tuyến
class PhuongAnTuyen(models_gis.Model):
    class Meta:
        ordering = ['maPATuyen']
        verbose_name = 'Phương án tuyến'
        verbose_name_plural = 'Phương án tuyến'

    # Fields
    maPATuyen = models_gis.AutoField(verbose_name='Mã phương án', primary_key=True)
    tenPATuyen = models_gis.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPATuyen = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPATuyen = models_gis.CharField(verbose_name='Người thực hiện', max_length=50, null=True, blank=True)
    ngayPATuyen = models_gis.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPATuyen = models_gis.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAT_KIEU_CHOICES)
    trangThaiPATuyen = models_gis.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPATuyen = models_gis.LineStringField(verbose_name='Tuyến đường', srid=4756)
    nvbp = models_gis.ForeignKey(NVBP, on_delete=models_gis.CASCADE, related_name='fk_pat_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def __str__(self):
        return self.tenPATuyen


# 10. Bảng phê duyệt phương án tuyến
class PheDuyetPhuongAnTuyen(models_gis.Model):
    class Meta:
        ordering = ['maCMPATuyen']
        verbose_name = 'Phê duyệt phương án tuyến'
        verbose_name_plural = 'Phê duyệt phương án tuyến'

    # Fields
    maCMPATuyen = models_gis.AutoField(verbose_name='Mã phê duyệt', primary_key=True)
    moTaCMPATuyen = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPATuyen = models_gis.CharField(verbose_name='Người phê duyệt', max_length=50, null=True, blank=True)
    ngayCMPATuyen = models_gis.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPATuyen = models_gis.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPATuyen = models_gis.LineStringField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paTuyen = models_gis.ForeignKey(PhuongAnTuyen, on_delete=models_gis.CASCADE, related_name='fk_pdpat_pavt', verbose_name='Phương án tuyến')


# 11. Bảng Phương án vùng
class PhuongAnVung(models_gis.Model):
    class Meta:
        ordering = ['maPAVung']
        verbose_name = 'Phương án vùng'
        verbose_name_plural = 'Phương án vùng'

    # Fields
    maPAVung = models_gis.AutoField(verbose_name='Mã phương án', primary_key=True)
    tenPAVung = models_gis.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPAVung = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPAVung = models_gis.CharField(verbose_name='Người thực hiện', max_length=50, null=True, blank=True)
    ngayPAVung = models_gis.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPAVung = models_gis.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAV_KIEU_CHOICES)
    trangThaiPAVung = models_gis.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPAVung = models_gis.PolygonField(verbose_name='Tuyến đường', srid=4756)
    nvbp = models_gis.ForeignKey(NVBP, on_delete=models_gis.CASCADE, related_name='fk_pav_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def __str__(self):
        return self.tenPAVung


# 12. Bảng phê duyệt phương án vùng
class PheDuyetPhuongAnVung(models_gis.Model):
    class Meta:
        ordering = ['maCMPAVung']
        verbose_name = 'Phê duyệt phương án vùng'
        verbose_name_plural = 'Phê duyệt phương án vùng'

    # Fields
    maCMPAVung = models_gis.AutoField(verbose_name='Mã phê duyệt', primary_key=True)
    moTaCMPAVung = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPAVung = models_gis.CharField(verbose_name='Người phê duyệt', max_length=50, null=True, blank=True)
    ngayCMPAVung = models_gis.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPAVung = models_gis.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPAVung = models_gis.PolygonField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paVung = models_gis.ForeignKey(PhuongAnVung, on_delete=models_gis.CASCADE, related_name='fk_pdpav_pavt', verbose_name='Phương án vùng')


# 13. Bảng phê duyệt chung
class PheDuyetChungNVBP(models_gis.Model):
    class Meta:
        ordering = ['maCMNVBP']
        verbose_name = 'Phê duyệt chung NVBP'
        verbose_name_plural = 'Phê duyệt chung NVBP'

    # Fields
    maCMNVBP = models_gis.AutoField(verbose_name='Mã phê duyệt', primary_key=True)
    tenCMNVBP = models_gis.CharField(verbose_name='Tên phê duyệt', max_length=50)
    moTaCMNVBP = models_gis.TextField(verbose_name='Mô tả', max_length=1000, null=True, blank=True)
    nguoiCMNVBP = models_gis.TextField(verbose_name='Người phê duyệt', max_length=50, null=True, blank=True)
    ngayCMNVBP = models_gis.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMNVBP = models_gis.IntegerField(verbose_name='Trạng thái', choices=stkh.PDCNVBP_TT_CHOICES)
    nvbp = models_gis.ForeignKey(NVBP, on_delete=models_gis.CASCADE, related_name='fk_pdcnvbp_nvbp', verbose_name='Nhiệm vụ bộ phận')


# 14. Bảng Gán lực lượng
class GanLucLuong(models_gis.Model):
    class Meta:
        ordering = ['maGanLL']
        verbose_name = 'Gán lực lượng'
        verbose_name_plural = 'Gán lực lượng'

    # Fields
    maGanLL = models_gis.AutoField(verbose_name='Mã phương án bố trí lực lượng', primary_key=True)
    tenGanLL = models_gis.CharField(verbose_name='Tên phương án bố trí lực lượng', max_length=100)
    noiDungNhiemVuGanLL = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    quanSoGanLL = models_gis.IntegerField(verbose_name='Quân số', null=True, blank=True)
    donViGanLL = models_gis.CharField(verbose_name='Tổ chức, biên chế của lực lượng', max_length=50)
    thoiGianBDau = models_gis.DateTimeField(verbose_name='Thời gian bắt đầu', null=True, blank=True)
    thoiGianKThuc = models_gis.DateTimeField(verbose_name='Thời gian kết thúc', null=True, blank=True)
    trangThaiLL = models_gis.IntegerField(verbose_name='Trạng thái lực lượng', choices=stkh.PA_TT_CHOICES)
    pavt = models_gis.ForeignKey(PhuongAnViTri, on_delete=models_gis.CASCADE, related_name='fk_ganll_pavt', verbose_name='Phương án vị trí')
    pat = models_gis.ForeignKey(PhuongAnTuyen, on_delete=models_gis.CASCADE, related_name='fk_ganll_pat', verbose_name='Phương án tuyến')
    pav = models_gis.ForeignKey(PhuongAnVung, on_delete=models_gis.CASCADE, related_name='fk_ganll_pav', verbose_name='Phương án vùng')

    # 
    def __str__(self):
        return self.tenGanLL


# 15. Bảng Phê duyệt phương án gán lực lượng
class PheDuyetPhuongAnGanLucLuong(models_gis.Model):
    class Meta:
        ordering = ['maCMGanLL']
        verbose_name = 'Phê duyệt phương án gán lực lượng'
        verbose_name_plural = 'Phê duyệt phương án gán lực lượng'

    # Fields
    maCMGanLL = models_gis.AutoField(verbose_name='Mã phê duyệt', primary_key=True)
    cmNoiDungNhiemVuGanLL = models_gis.TextField(verbose_name='Mô tả', max_length=1000)
    cmQuanSoGanLL = models_gis.IntegerField(verbose_name='Quân số', null=True, blank=True)
    cmDonViGanLL = models_gis.TextField(verbose_name='Phê duyệt biên chế lực lượng', max_length=500)
    cmThoiGianBDau = models_gis.DateField(verbose_name='Thời gian bắt đầu', null=True, blank=True)
    cmThoiGianKThuc = models_gis.DateField(verbose_name='Thời gian kết thúc', null=True, blank=True)
    trangThaiCMGanLL = models_gis.IntegerField(verbose_name='Trạng thái phê duyệt phương án', choices=stkh.PDPA_TT_CHOICES)
    ganLL = models_gis.ForeignKey(GanLucLuong, on_delete=models_gis.CASCADE, related_name='fk_pdpagll_ganll', verbose_name='Phương án bố trí lực lượng')



