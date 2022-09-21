from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.apps import apps
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.safestring import mark_safe

from . import models, meta
from .utils import constants, form, media
from .utils.config import ENABLE_EAV, AdminCommon, enable_eav_cls


# 
LoaiDV_cfg = enable_eav_cls(ENABLE_EAV.LoaiDVi)
CapDV_cfg = enable_eav_cls(ENABLE_EAV.CapDVi)
DonVi_cfg = enable_eav_cls(ENABLE_EAV.DonVi)
LoaiTB = enable_eav_cls(ENABLE_EAV.LoaiTB)
XuatXu = enable_eav_cls(ENABLE_EAV.XuatXu)
TinhTrangTB = enable_eav_cls(ENABLE_EAV.TinhTrangTB)
BienCheTB = enable_eav_cls(ENABLE_EAV.BienCheTB)
PhuKienTB = enable_eav_cls(ENABLE_EAV.PhuKienTB)


### Auth
# Nhóm tài khoản
class GroupInline(admin.StackedInline):
    model = models.NhomTaiKhoan
    can_delete = False

class CustomGroupAdmin(GroupAdmin):
    list_filter = ()
    search_fields = ()
    list_display = ('name',)
    inlines = (GroupInline, )

# Người dùng
class CustomUserAdmin(UserAdmin):
    list_filter = ()
    search_fields = ()
    readonly_fields = ('avatar',)
    list_display = ('username', 'hoten', 'is_staff', 'avatar', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'anhdaidien','avatar',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # 
    @admin.display(description = '')
    def avatar(self, obj):
        try:
            return mark_safe('<img src="{url}" width="50px" height="50px" alt="no image"/>'.format(url = obj.anhdaidien.url))
        except:
            return mark_safe('<img src="{url}" width="50px" height="50px" alt="no image" />'.format(url = ''))

    @admin.display(description = 'Họ tên')
    def hoten(self, obj):
        return '{last_name} {first_name}'.format(last_name = obj.last_name, first_name = obj.first_name)


### Đơn vị
# Loại đơn vị
class LoaiDVAdmin(AdminCommon, LoaiDV_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(LoaiDV_cfg.BASE_FORM, meta.LoaiDVMeta, models.LoaiDonVi, constants.LOAI_DONVI)
    list_display = ('maNhanDang', 'tenLoaiDonVi', )

# Cấp đơn vị
class CapDVAdmin(AdminCommon, CapDV_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(CapDV_cfg.BASE_FORM, meta.CapDVMeta, models.CapDonVi, constants.CAP_DONVI)
    list_display = ('maNhanDang', 'tenCap', 'KHQS', )

# Đơn vị
class DonViAdmin(AdminCommon, DonVi_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(DonVi_cfg.BASE_FORM, meta.DonViMeta, models.DonVi, constants.DONVI)
    list_display = ('maNhanDang', 'tenDonVi', 'tongQSDonVi', )


### Trang thiết bị
# Loại trang bị
class LoaiTBAdmin(AdminCommon, LoaiTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(LoaiTB.BASE_FORM, meta.LoaiTBMeta, models.LoaiTrangBi, constants.LOAI_TB)
    list_display = ('maNhanDang', 'tenLoaiTrangBi',)

# Xuất xứ
class XuatXuAdmin(AdminCommon, XuatXu.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(XuatXu.BASE_FORM, meta.XuatXuMeta, models.XuatXu, constants.XUATXU)
    list_display = ('maNhanDang', 'tenXuatXu', )

# Tình trạng trang bị
class TinhTrangTBAdmin(AdminCommon, TinhTrangTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(TinhTrangTB.BASE_FORM, meta.TinhTrangTBMeta, models.TinhTrangTrangBi, constants.TINHTRANG_TB)
    list_display = ('maNhanDang', 'tenTinhTrangTB', )

# Biên chế trang bị
class BienCheTBAdmin(AdminCommon, BienCheTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(BienCheTB.BASE_FORM, meta.BienCheTBMeta, models.BienCheTrangBi, constants.BIENCHE_TB)
    list_display = ('maNhanDang', 'tenTrangBi', 'soLuong', 'donViTinh', )

# Phụ kiện thiết bị
class PhuKienTBAdmin(AdminCommon, PhuKienTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(PhuKienTB.BASE_FORM, meta.PhuKienTBMeta, models.PhuKienThietBi, constants.PHUKIEN_TB)
    list_display = ('maNhanDang', 'tenPhuKien', 'soLuong', 'donViTinh', )


# Unregister
admin.site.unregister(Group)


# Register
from django.conf import settings
from .apps import DulieuquantriConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(Group, CustomGroupAdmin)
    admin.site.register(models.NguoiDung, CustomUserAdmin)
    admin.site.register(models.LoaiDonVi, LoaiDVAdmin)
    admin.site.register(models.CapDonVi, CapDVAdmin)
    admin.site.register(models.DonVi, DonViAdmin)
    admin.site.register(models.LoaiTrangBi, LoaiTBAdmin)
    admin.site.register(models.XuatXu, XuatXuAdmin)
    admin.site.register(models.TinhTrangTrangBi, TinhTrangTBAdmin)
    admin.site.register(models.BienCheTrangBi, BienCheTBAdmin)
    admin.site.register(models.PhuKienThietBi, PhuKienTBAdmin)

# 
from .apps import DulieuquantriConfig
# apps.get_model('auth', 'Group')._meta.app_label = DulieuquantriConfig.name
# apps.get_model('auth', 'Group')._meta.verbose_name = 'Nhóm tài khoản'
# apps.get_model('auth', 'Group')._meta.verbose_name_plural = 'Nhóm tài khoản'