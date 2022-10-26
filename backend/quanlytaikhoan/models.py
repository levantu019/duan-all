from django.db import models
from django.contrib.auth.models import AbstractUser
from multimedia.utils import choices
from quanlydonvi.models import DonVi

from .utils import choices as qltk

### Auth
# Nhóm tài khoản
class NhomTaiKhoan(models.Model):
    class Meta:
        verbose_name = 'Tuỳ chọn'
        verbose_name_plural = 'Tuỳ chọn'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    group = models.OneToOneField('auth.Group', unique=True, on_delete=models.CASCADE)
    role = models.IntegerField(choices=qltk.GROUP_LEVEL_CHOICES, verbose_name='Các nhóm mặc định', help_text='Tuỳ chọn các nhóm được xây dựng sẵn')
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
    anhDaiDien = models.ImageField(upload_to='images/avatar/', verbose_name='Ảnh đại diện', null=True, blank=True)
    queQuan = models.CharField(max_length=100, blank=True, null=True, verbose_name='Quê quán')
    soDienThoai = models.CharField(max_length=11, blank=True, null=True, verbose_name='Số điện thoại')
    capBac = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cấp bậc')
    chucVu = models.CharField(max_length=50, blank=True, null=True, verbose_name='Chức vụ')
    ngaySinh = models.DateField(verbose_name='Ngày sinh', blank=True, null=True,)
    gioiTinh = models.CharField(max_length=5, choices=qltk.GT_CHOICES, default=qltk.GT_NAM, verbose_name='Giới tính')
    thoiGianKN = models.DateField(blank=True, null=True, verbose_name='Thời gian KN')
    donVi = models.ForeignKey(DonVi, on_delete=models.CASCADE, related_name='fk_user_donvi', verbose_name='Đơn vị', blank=True, null=True)
    ghiChu = models.TextField(max_length=255, blank=True, null=True, verbose_name='Ghi chú')

