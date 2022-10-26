from django.contrib.gis.db import models
from eav.decorators import register_eav
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
    ten = models.CharField(max_length=50, verbose_name='Tên loại đơn vị')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.ten

# Cấp đơn vị
@register_eav()
class CapDonVi(models.Model):
    class Meta:
        verbose_name = 'Cấp đơn vị'
        verbose_name_plural = 'Cấp đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã cấp đơn vị')
    ten = models.CharField(max_length=100, verbose_name='Tên cấp')
    KHQS = models.CharField(max_length=100, verbose_name='Kí hiệu quân sự', blank=True, null=True)
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.ten

# Đơn vị
@register_eav()
class DonVi(NenDiaLy2N5N10N):
    class Meta:
        verbose_name = 'Đơn vị'
        verbose_name_plural = 'Đơn vị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    ten = models.CharField(max_length=100, verbose_name='Tên đơn vị')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Đơn vị chính', blank=True, null=True)
    phienHieuDonVi = models.CharField(max_length=20, verbose_name='Phiên hiệu đơn vị', blank=True, null=True)
    capDonVi = models.ForeignKey(CapDonVi, on_delete=models.CASCADE, verbose_name='Cấp đơn vị', blank=True, null=True)
    loaiDonVi = models.ForeignKey(LoaiDonVi, on_delete=models.CASCADE, verbose_name='Loại đơn vị', blank=True, null=True)
    diaChiDonVi = models.CharField(max_length=100, verbose_name='Địa chỉ đơn vị', blank=True, null=True)
    sdtQSDonVi = models.CharField(max_length=12, verbose_name='SĐT quân sự', blank=True, null=True)
    emailDonVi = models.CharField(max_length=30, verbose_name='Email đơn vị', blank=True, null=True)
    chucNangDonVi = models.CharField(max_length=100, verbose_name='Chức năng đơn vị', blank=True, null=True)
    nhiemVuDonVi = models.CharField(max_length=100, verbose_name='Nhiệm vụ đơn vị', blank=True, null=True)
    chiHuyTruongDonVi = models.CharField(max_length=30, verbose_name='Chỉ huy trưởng', blank=True, null=True)
    tongQSDonVi = models.PositiveIntegerField(default=0, verbose_name='Tổng quân số')
    order = models.PositiveIntegerField(default=0, verbose_name='Order')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)
    geo = models.PointField(blank=True, null=True, verbose_name='Vị trí đơn vị')
    congBo = models.BooleanField(default=False, verbose_name='Công bố')

    # 
    def __str__(self):
        return self.ten