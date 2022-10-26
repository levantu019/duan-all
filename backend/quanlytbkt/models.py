from django.contrib.gis.db import models
from eav.decorators import register_eav
from .utils import choices as dlqt
from core.utils import handleString
from multimedia.utils import choices, funcs
from quanlydonvi.models import DonVi


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
    ten = models.CharField(max_length=50, verbose_name='Tên loại trang bị')
    ghiChu = models.TextField(max_length=100, null=True, blank=True, verbose_name='Ghi chú')

    # 
    def __str__(self):
        return self.ten

# Xuất xứ
@register_eav()
class XuatXu(models.Model):
    class Meta:
        verbose_name = 'Xuất xứ'
        verbose_name_plural = 'Xuất xứ'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.SlugField(primary_key=True, max_length=30, verbose_name='Mã xuất xứ')
    ten = models.CharField(max_length=50, verbose_name='Tên xuất xứ')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        self.maNhanDang = handleString.generate_slug(self.ten)
        self.full_clean()
        super(XuatXu, self).save(*args, **kwargs)

# Tình trạng trang bị
@register_eav()
class TinhTrang(models.Model):
    class Meta:
        verbose_name = 'Tình trạng trang bị'
        verbose_name_plural = 'Tình trạng trang bị'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã tình trạng TB')
    ten = models.CharField(max_length=50, verbose_name='Tên tình trạng TB')
    ghiChu = models.TextField(max_length=100, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.ten

# Phân cấp chất lượng
class PhanCapChatLuong(models.Model):
    class Meta:
        verbose_name = 'Phân cấp chất lượng'
        verbose_name_plural = 'Phân cấp chất lượng'
        
    type_model = choices.LDL_KIEU_KHAC

    maNhanDang = models.CharField(primary_key=True, max_length=20, verbose_name='Mã phân cấp chất lượng')
    ten = models.CharField(max_length=255, verbose_name='Tên')
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)

    # 
    def __str__(self):
        return self.ten

# Trang bị khí tài
@register_eav()
class TrangBiKhiTai(models.Model):
    class Meta:
        verbose_name = 'Trang bị khí tài'
        verbose_name_plural = 'Trang bị khí tài'
        
    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name='Mã nhận dạng')
    ten = models.CharField(max_length=50, verbose_name='Tên trang bị')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Trang bị chính', blank=True, null=True)
    soHieuTrangBi = models.CharField(max_length=30, verbose_name='Số hiệu trang bị', blank=True, null=True)
    loaiTrangBiKhiTai = models.ForeignKey(LoaiTrangBiKhiTai, on_delete=models.SET_NULL, verbose_name='Loại trang bị', blank=True, null=True)
    xuatXu = models.ForeignKey(XuatXu, on_delete=models.SET_NULL, verbose_name='Xuất xứ', blank=True, null=True)
    namSanXuat = models.IntegerField(choices=dlqt.YEAR_CHOICES, verbose_name='Năm sản xuất', null=True, blank=True)
    tinhTrang = models.ForeignKey(TinhTrang, on_delete=models.SET_NULL, verbose_name='Tình trạng trang bị', null=True, blank=True)
    phanCapChatLuong = models.ForeignKey(PhanCapChatLuong, on_delete=models.SET_NULL, verbose_name='Phân cấp chất lượng', null=True, blank=True)
    chucNangTrangBi = models.CharField(max_length=100, verbose_name='Chức năng trang bị', blank=True, null=True)
    phanBoTrangBi = models.IntegerField(choices=dlqt.BCTB_PBTB_CHOICES, default=1, verbose_name='Phân bổ trang bị')
    deNghi = models.CharField(max_length=50, choices=dlqt.BCTB_DN_CHOICES, verbose_name='Đề nghị', blank=True, null=True)
    soLuong = models.PositiveIntegerField(verbose_name='Số lượng', default=1)
    link = models.CharField(max_length=100, blank=True, null=True)
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)
    donVi = models.ForeignKey(DonVi, on_delete=models.SET_NULL, verbose_name='Đơn vị', blank=True, null=True)
    congBo = models.BooleanField(default=False, verbose_name='Công bố')
    thaoTacNhap = models.CharField(max_length=50, choices=dlqt.TBKT_TT_NHAP, default=dlqt.TT_NHAP_NEW, verbose_name='Trạng thái dữ liệu')
    thongBao = models.TextField(max_length=500, blank=True, null=True, verbose_name='Thông báo')
    
    # 
    def __str__(self):
        return self.maNhanDang + '-' + self.ten

# Dữ liệu đa phương tiện
class DuLieuDaPhuongTien(models.Model):
    class Meta:
        verbose_name = "Dữ liệu đa phương tiện"
        verbose_name_plural = "Dữ liệu đa phương tiện"

    type_model = choices.LDL_KIEU_KHAC

    # Fields
    maNhanDang = models.CharField(max_length=20, primary_key=True, verbose_name="Mã dữ liệu")
    trangBiKhiTai = models.ForeignKey(TrangBiKhiTai, on_delete=models.CASCADE, verbose_name='Trang bị khí tài')
    ten = models.CharField(max_length=100, verbose_name="Tên dữ liệu", blank=True, null=True)
    path = models.FileField(upload_to=funcs.multimedia_upload_to, verbose_name="File dữ liệu")
    dinhDang = models.CharField(max_length=100, verbose_name="Định dạng", blank=True, null=True)
    ghiChu = models.TextField(max_length=255, verbose_name='Ghi chú', blank=True, null=True)

    #  