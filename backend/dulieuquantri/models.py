from django.contrib.gis.db import models
from eav.decorators import register_eav
from .utils import choices as dlqt
from multimedia.utils import choices, funcs
from nendialy.models import NenDiaLy2N5N10N


### Đơn vị
# Loại đơn vị
@register_eav()
class LoaiDonVi(models.Model):
    class Meta:
        verbose_name = 'Loại đơn vị'
        verbose_name_plural = 'Loại đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã loại đơn vị')
    tenLoaiDonVi = models.CharField(max_length=50, verbose_name='Tên loại đơn vị')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.tenLoaiDonVi

# Cấp đơn vị
@register_eav()
class CapDonVi(models.Model):
    class Meta:
        verbose_name = 'Cấp đơn vị'
        verbose_name_plural = 'Cấp đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã cấp đơn vị')
    tenCap = models.CharField(max_length=100, verbose_name='Tên cấp')
    KHQS = models.CharField(max_length=100, verbose_name='Kí hiệu quân sự', blank=True, null=True)
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.tenCap

# Đơn vị
@register_eav()
class DonVi(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đơn vị'
        verbose_name_plural = 'Đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    tenDonVi = models.CharField(max_length=100, verbose_name='Tên đơn vị')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Nút cha', blank=True, null=True)
    phienHieuDonVi = models.CharField(max_length=20, verbose_name='Phiên hiệu đơn vị', blank=True, null=True)
    capDonVi = models.ForeignKey(CapDonVi, on_delete=models.CASCADE, verbose_name='Cấp đơn vị', blank=True, null=True)
    loaiDonVi = models.ForeignKey(LoaiDonVi, on_delete=models.CASCADE, verbose_name='Loại đơn vị', blank=True, null=True)
    diaChiDonVi = models.CharField(max_length=100, verbose_name='Địa chỉ đơn vị', blank=True, null=True)
    sdtQSDonVi = models.CharField(max_length=12, verbose_name='SĐT quân sự', blank=True, null=True)
    emailDonVi = models.CharField(max_length=30, verbose_name='Email đơn vị', blank=True, null=True)
    chucNangDonVi = models.CharField(max_length=100, verbose_name='Chức năng đơn vị', blank=True, null=True)
    nhiemVuDonVi = models.CharField(max_length=100, verbose_name='Nhiệm vụ đơn vị', blank=True, null=True)
    chiHuyTruongDonVi = models.CharField(max_length=30, verbose_name='Chỉ huy trưởng', blank=True, null=True)
    tongQSDonVi = models.PositiveIntegerField(verbose_name='Tổng quân số')
    order = models.PositiveIntegerField(verbose_name='Order')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)
    geo = models.PointField(blank=True, null=True, verbose_name='Vị trí đơn vị')
    congBo = models.BooleanField(blank=True, null=True, verbose_name='Công bố')

    # 
    def __str__(self):
        return self.tenDonVi

### Trang thiết bị khí tài
# Loại trang bị khí tài
@register_eav()
class LoaiTrangBiKhiTai(models.Model):
    class Meta:
        verbose_name = 'Loại trang bị khí tài'
        verbose_name_plural = 'Loại trang bị khí tài'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã loại trang bị')
    tenLoaiTrangBi = models.CharField(max_length=50, verbose_name='Tên loại trang bị')
    ghiChu = models.TextField(max_length=100, null=True, blank=True, verbose_name='Ghi chú')

    # 
    def __str__(self):
        return self.tenLoaiTrangBi

# Xuất xứ
@register_eav()
class XuatXu(models.Model):
    class Meta:
        verbose_name = 'Xuất xứ'
        verbose_name_plural = 'Xuất xứ'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã xuất xứ')
    tenXuatXu = models.CharField(max_length=50, verbose_name='Tên xuất xứ')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.tenXuatXu

# Tình trạng trang bị
@register_eav()
class TinhTrang(models.Model):
    class Meta:
        verbose_name = 'Tình trạng trang bị'
        verbose_name_plural = 'Tình trạng trang bị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã tình trạng TB')
    tenTinhTrangTB = models.CharField(max_length=50, verbose_name='Tên tình trạng TB')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.tenTinhTrangTB

# Phân cấp chất lượng
class PhanCapChatLuong(models.Model):
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã phân cấp chất lượng')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)

# Trang bị khí tài
@register_eav()
class TrangBiKhiTai(models.Model):
    class Meta:
        verbose_name = 'Trang bị khí tài'
        verbose_name_plural = 'Trang bị khí tài'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã nhận dạng')
    tenTrangBi = models.CharField(max_length=50, verbose_name='Tên trang bị')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Nút cha', blank=True, null=True)
    soHieuTrangBi = models.CharField(max_length=30, verbose_name='Số hiệu trang bị', blank=True, null=True)
    loaiTrangBiKhiTai = models.ForeignKey(LoaiTrangBiKhiTai, on_delete=models.SET_NULL, verbose_name='Loại trang bị', blank=True, null=True)
    xuatXu = models.ForeignKey(XuatXu, on_delete=models.SET_NULL, verbose_name='Xuất xứ', blank=True, null=True)
    namSanXuat = models.IntegerField(choices=dlqt.YEAR_CHOICES, verbose_name='Năm sản xuất', null=True, blank=True)
    tinhTrang = models.ForeignKey(TinhTrang, on_delete=models.SET_NULL, verbose_name='Tình trạng trang bị', null=True, blank=True)
    phanCapChatLuong = models.ForeignKey(PhanCapChatLuong, on_delete=models.SET_NULL, verbose_name='Tình trạng trang bị', null=True, blank=True)
    chucNangTrangBi = models.CharField(max_length=100, verbose_name='Chức năng trang bị', blank=True, null=True)
    phanBoTrangBi = models.IntegerField(choices=dlqt.BCTB_PBTB_CHOICES, verbose_name='Phân bổ trang bị')
    deNghi = models.CharField(max_length=50, choices=dlqt.BCTB_DN_CHOICES, verbose_name='Đề nghị', blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)
    donVi = models.ForeignKey(DonVi, on_delete=models.SET_NULL, verbose_name='Đơn vị', blank=True, null=True)
    congBo = models.BooleanField(blank=True, null=True, verbose_name='Công bố')

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.tenTrangBi

# Dữ liệu đa phương tiện
class DuLieuDaPhuongTien(models.Model):
    class Meta:
        verbose_name = "Dữ liệu đa phương tiện"
        verbose_name_plural = "Dữ liệu đa phương tiện"

    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã dữ liệu")
    trangBiKhiTai = models.ForeignKey(TrangBiKhiTai, on_delete=models.CASCADE, verbose_name='Trang bị khí tài')
    tenDuLieu = models.CharField(max_length=100, verbose_name="Tên dữ liệu", blank=True, null=True)
    pathDuLieu = models.FileField(upload_to=funcs.multimedia_upload_to, verbose_name="File dữ liệu")
    dinhDang = models.CharField(max_length=100, verbose_name="Định dạng", blank=True, null=True)
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)
