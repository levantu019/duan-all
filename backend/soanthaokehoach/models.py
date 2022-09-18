from django.contrib.gis.db import models

from eav.decorators import register_eav

from .utils import choices as stkh, handleString, constants

from dulieuquantri.models import DonVi

# 1. Bảng Nhiệm vụ điều hành
@register_eav()
class NVDH(models.Model):
    class Meta:
        verbose_name = 'Nhiệm vụ điều hành'
        verbose_name_plural = 'Nhiệm vụ điều hành'

    # Fields
    maNhanDang = models.CharField(max_length=50, primary_key=True, blank=True, verbose_name='Mã NVDH')
    tenNVDH = models.CharField(verbose_name = 'Tên NVDH', max_length=100)
    moTaNV = models.TextField(verbose_name='Mô tả NVDH', max_length=1000, blank=True)
    chihuyNVDH = models.CharField(verbose_name='Chỉ huy NVDH', max_length=50)
    ngayBDNVDH = models.DateField(verbose_name='Ngày bắt đầu NVDH', null=True, blank=True)
    ngayKTNVDH = models.DateField(verbose_name='Ngày kết thúc NVDH', null=True, blank=True)
    # vanbanNVDH = models.FileField(verbose_name='Văn bản NVDH', upload_to='files/', null=True, blank=True)
    kieuNVDH = models.IntegerField(verbose_name='Kiểu NVDH', choices=stkh.NVDH_KIEU_CHOICES)

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(NVDH, constants.NVDH)
        super(NVDH, self).save(*args, **kwargs)

    def __str__(self):
        return self.maNhanDang + '-' + self.tenNVDH


# 2. Bảng Điểm NVDH
@register_eav()
class DiemNVDH(models.Model):
    class Meta:
        verbose_name = 'Điểm NVDH'
        verbose_name_plural = 'Điểm NVDH'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã điểm', primary_key=True, blank=True)
    tenDiem = models.CharField(verbose_name='Tên điểm', max_length=100)
    moTaDiem = models.TextField(verbose_name='Mô tả điểm', max_length=500, blank=True)
    ngayDiem = models.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoDiem = models.PointField(verbose_name='Điểm', srid=4756)
    nvdh = models.ForeignKey(NVDH, on_delete=models.CASCADE, related_name='fk_diemnvdh_nvdh', verbose_name='Nhiệm vụ điều hành')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(DiemNVDH, constants.DIEM_NVDH)
        super(DiemNVDH, self).save(*args, **kwargs)
        

# 3. Bảng Tuyến NVDH
@register_eav()
class TuyenNVDH(models.Model):
    class Meta:
        verbose_name = 'Tuyến NVDH'
        verbose_name_plural = 'Tuyến NVDH'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã tuyến', primary_key=True, blank=True)
    tenTuyen = models.CharField(max_length=100)
    moTaTuyen = models.TextField(verbose_name='Mô tả tuyến', max_length=500, blank=True)
    ngayTuyen = models.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoTuyen = models.LineStringField(verbose_name='Tuyến', srid=4756)
    nvdh = models.ForeignKey(NVDH, on_delete=models.CASCADE, related_name='fk_tuyennvdh_nvdh', verbose_name='Nhiệm vụ điều hành')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(TuyenNVDH, constants.TUYEN_NVDH)
        super(TuyenNVDH, self).save(*args, **kwargs)
        

# 4. Bảng Vùng NVDH
@register_eav()
class VungNVDH(models.Model):
    class Meta:
        verbose_name = 'Vùng NVDH'
        verbose_name_plural = 'Vùng NVDH'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã vùng', primary_key=True, blank=True)
    tenVung = models.CharField(max_length=100)
    moTaVung = models.TextField(verbose_name='Mô tả vùng', max_length=500, blank=True)
    ngayVung = models.DateField(verbose_name='Ngày thêm, sửa', null=True, blank=True)
    geoVung = models.PolygonField(verbose_name='Vùng', srid=4756)
    nvdh = models.ForeignKey(NVDH, on_delete=models.CASCADE, related_name='fk_vungnvdh_nvdh', verbose_name='Nhiệm vụ điều hành')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(VungNVDH, constants.VUNG_NVDH)
        super(VungNVDH, self).save(*args, **kwargs)
        

# # 5. Bảng đơn vị
# class DonVi(models.Model):
#     class Meta:
#         verbose_name = 'Đơn vị'
#         verbose_name_plural = 'Đơn vị'

#     # Fields
#     maNhanDang = models.CharField(max_length=50, verbose_name='Mã đơn vị', primary_key=True, blank=True)
#     tenDV = models.CharField(verbose_name='Tên đơn vị', max_length=100)
#     quanSoDV = models.IntegerField(verbose_name='Quân số đơn vị', null=True, blank=True)
#     chucNangDV = models.TextField(verbose_name='Chức năng', max_length=500, blank=True)
#     diaChi = models.CharField(verbose_name='Địa chỉ', max_length=100, blank=True)
#     geoDV = models.PointField(verbose_name='Vị trí', srid=4756)
# (Đã chuyển sang app dulieuquantri)

#     # 
#     def __str__(self):
#         return self.tenDV


# 6. Bảng Nhiệm vụ bộ phận
@register_eav()
class NVBP(models.Model):
    class Meta:
        verbose_name = 'Nhiệm vụ bộ phận'
        verbose_name_plural = 'Nhiệm vụ bộ phận'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã NVBP', primary_key=True, blank=True)
    tenNVBP = models.CharField(verbose_name='Tên NVBP', max_length=100)
    moTaNVBP = models.TextField(verbose_name='Mô tả NVBP', max_length=5000)
    ngayBDNVBP = models.DateField(verbose_name='Ngày bắt đầu', null=True, blank=True)
    ngayKTNVBP = models.DateField(verbose_name='Ngày kết thúc', null=True, blank=True)
    trangThaiNVBP = models.IntegerField(verbose_name='Trạng thái nhiệm vụ', choices=stkh.NVBP_TT_CHOICES)
    maNVDH = models.ForeignKey(NVDH, on_delete=models.CASCADE, related_name='fk_nvbp_nvdh', verbose_name='Nhiệm vụ điều hành')
    maDV = models.ForeignKey(DonVi, on_delete=models.CASCADE, related_name='fk_nvbp_dv', verbose_name='Đơn vị')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(NVBP, constants.NVBP)
        super(NVBP, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.tenNVBP


# 7. Bảng Phương án vị trí
@register_eav()
class PhuongAnViTri(models.Model):
    class Meta:
        verbose_name = 'Phương án vị trí'
        verbose_name_plural = 'Phương án vị trí'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phương án', primary_key=True, blank=True)
    tenPAVT = models.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPAVT = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPAVT = models.CharField(verbose_name='Người thực hiện', max_length=50, blank=True)
    ngayPAVT = models.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPAVT = models.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAVT_KIEU_CHOICES)
    trangthaiPAVT = models.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPAVT = models.PointField(verbose_name='Vị trí', srid=4756)
    nvbp = models.ForeignKey(NVBP, on_delete=models.CASCADE, related_name='fk_pavt_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PhuongAnViTri, constants.PA_VTRI)
        super(PhuongAnViTri, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.tenPAVT


# 8. Bảng phê duyệt phương án vị trí
@register_eav()
class PheDuyetPhuongAnViTri(models.Model):
    class Meta:
        verbose_name = 'Phê duyệt phương án vị trí'
        verbose_name_plural = 'Phê duyệt phương án vị trí'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phê duyệt', primary_key=True, blank=True)
    moTaCMPAVT = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPAVT = models.CharField(verbose_name='Người phê duyệt', max_length=50, blank=True)
    ngayCMPAVT = models.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPAVT = models.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPAVT = models.PointField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paViTri = models.ForeignKey(PhuongAnViTri, on_delete=models.CASCADE, related_name='fk_pdpavt_pavt', verbose_name='Phương án vị trí')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PheDuyetPhuongAnViTri, constants.PDPA_VTRI)
        super(PheDuyetPhuongAnViTri, self).save(*args, **kwargs)
        

# 9. Bảng Phương án tuyến
@register_eav()
class PhuongAnTuyen(models.Model):
    class Meta:
        verbose_name = 'Phương án tuyến'
        verbose_name_plural = 'Phương án tuyến'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phương án', primary_key=True, blank=True)
    tenPATuyen = models.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPATuyen = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPATuyen = models.CharField(verbose_name='Người thực hiện', max_length=50, blank=True)
    ngayPATuyen = models.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPATuyen = models.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAT_KIEU_CHOICES)
    trangThaiPATuyen = models.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPATuyen = models.LineStringField(verbose_name='Tuyến đường', srid=4756)
    nvbp = models.ForeignKey(NVBP, on_delete=models.CASCADE, related_name='fk_pat_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PhuongAnTuyen, constants.PA_TUYEN)
        super(PhuongAnTuyen, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.tenPATuyen


# 10. Bảng phê duyệt phương án tuyến
@register_eav()
class PheDuyetPhuongAnTuyen(models.Model):
    class Meta:
        verbose_name = 'Phê duyệt phương án tuyến'
        verbose_name_plural = 'Phê duyệt phương án tuyến'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phê duyệt', primary_key=True, blank=True)
    moTaCMPATuyen = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPATuyen = models.CharField(verbose_name='Người phê duyệt', max_length=50, blank=True)
    ngayCMPATuyen = models.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPATuyen = models.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPATuyen = models.LineStringField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paTuyen = models.ForeignKey(PhuongAnTuyen, on_delete=models.CASCADE, related_name='fk_pdpat_pavt', verbose_name='Phương án tuyến')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PheDuyetPhuongAnTuyen, constants.PDPA_TUYEN)
        super(PheDuyetPhuongAnTuyen, self).save(*args, **kwargs)
        

# 11. Bảng Phương án vùng
@register_eav()
class PhuongAnVung(models.Model):
    class Meta:
        verbose_name = 'Phương án vùng'
        verbose_name_plural = 'Phương án vùng'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phương án', primary_key=True, blank=True)
    tenPAVung = models.CharField(verbose_name='Tên phương án', max_length=100)
    moTaPAVung = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiPAVung = models.CharField(verbose_name='Người thực hiện', max_length=50, blank=True)
    ngayPAVung = models.DateField(verbose_name='Ngày lựa chọn phương án', null=True, blank=True)
    kieuPAVung = models.IntegerField(verbose_name='Kiểu phương án', choices=stkh.PAV_KIEU_CHOICES)
    trangThaiPAVung = models.IntegerField(verbose_name='Trạng thái phương án', choices=stkh.PA_TT_CHOICES)
    geoPAVung = models.PolygonField(verbose_name='Tuyến đường', srid=4756)
    nvbp = models.ForeignKey(NVBP, on_delete=models.CASCADE, related_name='fk_pav_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PhuongAnVung, constants.PDPA_VUNG)
        super(PhuongAnVung, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.tenPAVung


# 12. Bảng phê duyệt phương án vùng
@register_eav()
class PheDuyetPhuongAnVung(models.Model):
    class Meta:
        verbose_name = 'Phê duyệt phương án vùng'
        verbose_name_plural = 'Phê duyệt phương án vùng'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phê duyệt', primary_key=True, blank=True)
    moTaCMPAVung = models.TextField(verbose_name='Mô tả', max_length=1000)
    nguoiCMPAVung = models.CharField(verbose_name='Người phê duyệt', max_length=50, blank=True)
    ngayCMPAVung = models.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMPAVung = models.IntegerField(verbose_name='Trạng thái', choices=stkh.PDPA_TT_CHOICES)
    geoCMPAVung = models.PolygonField(verbose_name='Góp ý', null=True, blank=True, srid=4756)
    paVung = models.ForeignKey(PhuongAnVung, on_delete=models.CASCADE, related_name='fk_pdpav_pavt', verbose_name='Phương án vùng')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PheDuyetPhuongAnVung, constants.PDPA_VUNG)
        super(PheDuyetPhuongAnVung, self).save(*args, **kwargs)
        

# 13. Bảng phê duyệt chung
@register_eav()
class PheDuyetChungNVBP(models.Model):
    class Meta:
        verbose_name = 'Phê duyệt chung NVBP'
        verbose_name_plural = 'Phê duyệt chung NVBP'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phê duyệt', primary_key=True, blank=True)
    tenCMNVBP = models.CharField(verbose_name='Tên phê duyệt', max_length=50)
    moTaCMNVBP = models.TextField(verbose_name='Mô tả', max_length=1000, blank=True)
    nguoiCMNVBP = models.TextField(verbose_name='Người phê duyệt', max_length=50, blank=True)
    ngayCMNVBP = models.DateField(verbose_name='Ngày phê duyệt', null=True, blank=True)
    trangThaiCMNVBP = models.IntegerField(verbose_name='Trạng thái', choices=stkh.PDCNVBP_TT_CHOICES)
    nvbp = models.ForeignKey(NVBP, on_delete=models.CASCADE, related_name='fk_pdcnvbp_nvbp', verbose_name='Nhiệm vụ bộ phận')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(PheDuyetChungNVBP, constants.PD_CHUNG)
        super(PheDuyetChungNVBP, self).save(*args, **kwargs)
        

# 14. Bảng Gán lực lượng
@register_eav()
class GanLucLuong(models.Model):
    class Meta:
        verbose_name = 'Gán lực lượng'
        verbose_name_plural = 'Gán lực lượng'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phương án bố trí lực lượng', primary_key=True, blank=True)
    tenGanLL = models.CharField(verbose_name='Tên phương án bố trí lực lượng', max_length=100)
    noiDungNhiemVuGanLL = models.TextField(verbose_name='Mô tả', max_length=1000)
    quanSoGanLL = models.IntegerField(verbose_name='Quân số', null=True, blank=True)
    donViGanLL = models.CharField(verbose_name='Tổ chức, biên chế của lực lượng', max_length=50)
    thoiGianBDau = models.DateTimeField(verbose_name='Thời gian bắt đầu', null=True, blank=True)
    thoiGianKThuc = models.DateTimeField(verbose_name='Thời gian kết thúc', null=True, blank=True)
    trangThaiLL = models.IntegerField(verbose_name='Trạng thái lực lượng', choices=stkh.PA_TT_CHOICES)
    pavt = models.ForeignKey(PhuongAnViTri, on_delete=models.CASCADE, related_name='fk_ganll_pavt', verbose_name='Phương án vị trí')
    pat = models.ForeignKey(PhuongAnTuyen, on_delete=models.CASCADE, related_name='fk_ganll_pat', verbose_name='Phương án tuyến')
    pav = models.ForeignKey(PhuongAnVung, on_delete=models.CASCADE, related_name='fk_ganll_pav', verbose_name='Phương án vùng')

    # 
    def save(self, *args, **kwargs):
        if self.maNhanDang is None:
            self.maNhanDang = handleString.generate_MaNhanDang(GanLucLuong, constants.GAN_LL)
        super(GanLucLuong, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.tenGanLL


# 15. Bảng Phê duyệt phương án gán lực lượng
@register_eav()
class PheDuyetPhuongAnGanLucLuong(models.Model):
    class Meta:
        verbose_name = 'Phê duyệt phương án gán lực lượng'
        verbose_name_plural = 'Phê duyệt phương án gán lực lượng'

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã phê duyệt', primary_key=True, blank=True)
    cmNoiDungNhiemVuGanLL = models.TextField(verbose_name='Mô tả', max_length=1000)
    cmQuanSoGanLL = models.IntegerField(verbose_name='Quân số', null=True, blank=True)
    cmDonViGanLL = models.TextField(verbose_name='Phê duyệt biên chế lực lượng', max_length=500)
    cmThoiGianBDau = models.DateField(verbose_name='Thời gian bắt đầu', null=True, blank=True)
    cmThoiGianKThuc = models.DateField(verbose_name='Thời gian kết thúc', null=True, blank=True)
    trangThaiCMGanLL = models.IntegerField(verbose_name='Trạng thái phê duyệt phương án', choices=stkh.PDPA_TT_CHOICES)
    ganLL = models.ForeignKey(GanLucLuong, on_delete=models.CASCADE, related_name='fk_pdpagll_ganll', verbose_name='Phương án bố trí lực lượng')

    # 
    def save(self, *args, **kwargs):
        self.maNhanDang = handleString.generate_MaNhanDang(PheDuyetPhuongAnGanLucLuong, constants.PDPA_GANLL)
        super(PheDuyetPhuongAnGanLucLuong, self).save(*args, **kwargs)
        

