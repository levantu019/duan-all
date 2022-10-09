from django.contrib import admin
from django.contrib.auth.models import Group
from django.apps import apps
from django.urls import path
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from jwtauth.utils import funcs

from . import models, meta, forms
from .utils import constants, form, media, choices as dlqt
from .utils.config import ENABLE_EAV, AdminCommon, enable_eav_cls


# 
LoaiDV_cfg = enable_eav_cls(ENABLE_EAV.LoaiDVi)
CapDV_cfg = enable_eav_cls(ENABLE_EAV.CapDVi)
DonVi_cfg = enable_eav_cls(ENABLE_EAV.DonVi)
LoaiTB = enable_eav_cls(ENABLE_EAV.LoaiTB)
XuatXu = enable_eav_cls(ENABLE_EAV.XuatXu)
TinhTrangTB = enable_eav_cls(ENABLE_EAV.TinhTrangTB)
TBKT = enable_eav_cls(ENABLE_EAV.TBKT)



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
    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', )
        css = {
            'all': ('extra/css/treetable.css', )
        }

    form = form.form_custom_MaNhanDang(DonVi_cfg.BASE_FORM, meta.DonViMeta, models.DonVi, constants.DONVI)
    change_list_template = "admin/change_list_treetable.html"
    list_display = ('maNhanDang', 'tenDonVi', 'tongQSDonVi', )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/add/', self.add_children_view, name='test_model2_add_children'),
        ]

        return my_urls + urls
    
    def add_children_view(self, request, object_id, form_url='', extra_context=None):
        try:
            data = request.GET.copy()
            data["parent"] = object_id
            request.GET = data
            return super(DonViAdmin, self).add_view(
                request, form_url, extra_context
            )
        except ValidationError as e:
            # return handle_exception(self, request, e)
            pass


### Trang thiết bị
# Loại trang bị
class LoaiTBAdmin(AdminCommon, LoaiTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(LoaiTB.BASE_FORM, meta.LoaiTBMeta, models.LoaiTrangBiKhiTai, constants.LOAI_TB)
    list_display = ('maNhanDang', 'tenLoaiTrangBi',)

# Xuất xứ
class XuatXuAdmin(AdminCommon, XuatXu.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(XuatXu.BASE_FORM, meta.XuatXuMeta, models.XuatXu, constants.XUATXU)
    list_display = ('maNhanDang', 'tenXuatXu', )

# Tình trạng trang bị
class TinhTrangTBAdmin(AdminCommon, TinhTrangTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(TinhTrangTB.BASE_FORM, meta.TinhTrangTBMeta, models.TinhTrang, constants.TINHTRANG_TB)
    list_display = ('maNhanDang', 'tenTinhTrangTB', )

# Trang bị khí tài
class TBKTAdmin(AdminCommon, TBKT.BASE_ADMIN):
    class Media:
        js = media.MODAL_CHART_JS

    change_list_template = "admin/button_statistic_BCTB.html"

    form = form.form_custom_MaNhanDang(TBKT.BASE_FORM, meta.TBKTMeta, models.TrangBiKhiTai, constants.TBKT)
    list_display = ('maNhanDang', 'tenTrangBi', )

# Phụ kiện thiết bị
# class TBKhiTaiAdmin(AdminCommon, PhuKienTB.BASE_ADMIN):
#     class Media:
#         js = media.MODAL_CHART_JS

#     change_list_template = "admin/button_statistic_TBKT.html"

#     form = form.form_custom_MaNhanDang(PhuKienTB.BASE_FORM, meta.ThietBiKhiTaiMeta, models.ThietBiKhiTai, constants.PHUKIEN_TB)
#     list_display = ('maNhanDang', 'tenPhuKien', 'soLuong', 'loaiTrangBiKhiTai' )


# Register
from django.conf import settings
from .apps import DulieuquantriConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.LoaiDonVi, LoaiDVAdmin)
    admin.site.register(models.CapDonVi, CapDVAdmin)
    admin.site.register(models.DonVi, DonViAdmin)
    admin.site.register(models.LoaiTrangBiKhiTai, LoaiTBAdmin)
    admin.site.register(models.XuatXu, XuatXuAdmin)
    admin.site.register(models.TinhTrang, TinhTrangTBAdmin)
    admin.site.register(models.TrangBiKhiTai, TBKTAdmin)
    admin.site.register(models.PhanCapChatLuong)

# 
from .apps import DulieuquantriConfig
# apps.get_model('auth', 'Group')._meta.app_label = DulieuquantriConfig.name
# apps.get_model('auth', 'Group')._meta.verbose_name = 'Nhóm tài khoản'
# apps.get_model('auth', 'Group')._meta.verbose_name_plural = 'Nhóm tài khoản'