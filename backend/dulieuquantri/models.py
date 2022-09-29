from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
from eav.decorators import register_eav
from .utils import choices as dlqt
from dancu.models import Point_CongTrinhQuocPhong
from multimedia.utils import choices
from jwtauth.utils import funcs


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
class DonVi(models.Model):
    class Meta:
        verbose_name = 'Đơn vị'
        verbose_name_plural = 'Đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã đơn vị')
    tenDonVi = models.CharField(max_length=100, verbose_name='Tên đơn vị')
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
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)
    CTQP = models.ForeignKey(Point_CongTrinhQuocPhong, on_delete=models.CASCADE, verbose_name='Công trình quốc phòng', blank=True, null=True)

    # 
    def __str__(self):
        return self.tenDonVi

### Auth
# Nhóm tài khoản
class NhomTaiKhoan(models.Model):
    class Meta:
        verbose_name = 'Tuỳ chọn'
        verbose_name_plural = 'Tuỳ chọn'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    group = models.OneToOneField('auth.Group', unique=True, on_delete=models.CASCADE)
    role = models.IntegerField(choices=dlqt.GROUP_LEVEL_CHOICES, default=dlqt.OPTIONAL, verbose_name='Các nhóm mặc định', help_text='Tuỳ chọn các nhóm được xây dựng sẵn')
    moTa = models.TextField(max_length=500, verbose_name='Mô tả', blank=True, null=True)
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.group.name)

# Người dùng
class NguoiDung(AbstractUser):
    class Meta:
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Người dùng'

    # Fields
    anhdaidien = models.ImageField(upload_to='images/avatar/', verbose_name='Ảnh đại diện', null=True, blank=True)
    donVi = models.ForeignKey(DonVi, on_delete=models.CASCADE, related_name='fk_user_donvi', verbose_name='Đơn vị', null=True, blank=True)


### Trang thiết bị
# Loại trang bị
@register_eav()
class LoaiTrangBiKhiTai(models.Model):
    class Meta:
        verbose_name = 'Loại trang bị'
        verbose_name_plural = 'Loại trang bị'
        
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
class TinhTrangTrangBi(models.Model):
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

# Biên chế trang bị
@register_eav()
class BienCheTrangBi(models.Model):
    class Meta:
        verbose_name = 'Biên chế trang bị'
        verbose_name_plural = 'Biên chế trang bị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã nhận dạng')
    donVi = models.ForeignKey(DonVi, on_delete=models.CASCADE, verbose_name='Đơn vị')
    tenTrangBi = models.CharField(max_length=50, verbose_name='Tên trang bị')
    donViTinh = models.CharField(max_length=20, verbose_name='Đơn vị tính')
    soLuong = models.PositiveIntegerField(default=0, verbose_name='Số lượng')
    soHieuTrangBi = models.CharField(max_length=30, verbose_name='Số hiệu trang bị', blank=True, null=True)
    loaiTrangBiKhiTai = models.ForeignKey(LoaiTrangBiKhiTai, on_delete=models.CASCADE, verbose_name='Loại trang bị')
    xuatXu = models.ForeignKey(XuatXu, on_delete=models.CASCADE, verbose_name='Xuất xứ')
    namSanXuat = models.IntegerField(choices=dlqt.YEAR_CHOICES, verbose_name='Năm sản xuất', null=True, blank=True)
    tinhTrangTrangBi = models.ForeignKey(TinhTrangTrangBi, on_delete=models.CASCADE, verbose_name='Tình trạng trang bị', null=True, blank=True)
    phanCapChatLuong = models.IntegerField(choices=dlqt.BCTB_PCCL_CHOICES, verbose_name='Phân cấp chất lượng')
    phanBoTrangBi = models.IntegerField(choices=dlqt.BCTB_PBTB_CHOICES, verbose_name='Phân bổ trang bị')
    deNghi = models.CharField(max_length=50, choices=dlqt.BCTB_DN_CHOICES, verbose_name='Đề nghị', blank=True, null=True)
    chucNangTrangBi = models.CharField(max_length=100, verbose_name='Chức năng trang bị', blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.tenTrangBi

# Phụ kiện thiết bị
@register_eav()
class ThietBiKhiTai(models.Model):
    class Meta:
        verbose_name = 'Thiết bị khí tài'
        verbose_name_plural = 'Thiết bị khí tài'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã phụ kiện')
    bienCheTB = models.ForeignKey(BienCheTrangBi, on_delete=models.SET_NULL, related_name='fk_tbkt_bctb', null=True, blank=True, verbose_name='Biên chế trang bị')
    tenPhuKien = models.CharField(max_length=50, verbose_name='Tên phụ kiện')
    donViTinh = models.CharField(max_length=20, verbose_name='Đơn vị tính')
    soLuong = models.PositiveIntegerField(default=0, verbose_name='Số lượng')
    dongBo = models.BooleanField(verbose_name='Đồng bộ')
    # tinhTrang = models.CharField(max_length=20, choices=dlqt.PKTB_TT_CHOICES, verbose_name='Tình trạng')
    namSanXuat = models.IntegerField(choices=dlqt.YEAR_CHOICES, verbose_name='Năm sản xuất')
    phanCapChatLuong = models.IntegerField(choices=dlqt.BCTB_PCCL_CHOICES, verbose_name='Phân cấp chất lượng')
    loaiTrangBiKhiTai = models.ForeignKey(LoaiTrangBiKhiTai, on_delete=models.SET_NULL, related_name='fk_tbkt_bctb', null=True, blank=True, verbose_name='Loại trang bị khí tài')
    xuatXu = models.ForeignKey(XuatXu, on_delete=models.SET_NULL, related_name='fk_tbkt_xx', blank=True, null=True, verbose_name='Xuất xứ')
    tinhTrangTrangBi = models.ForeignKey(TinhTrangTrangBi, on_delete=models.SET_NULL, related_name='fk_tbkt_tttb', blank=True, null=True, verbose_name='Tình trạng trang bị')


    # 
    def __str__(self):
        return  self.tenPhuKien


