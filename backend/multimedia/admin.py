from django.contrib import admin

from . import models, forms, meta
from .utils import constants, form, media
from .utils.config import ENABLE_EAV, enable_eav_cls


# 
NhomDL_cfg = enable_eav_cls(ENABLE_EAV.NhomDL)
LoaiStyle_cfg = enable_eav_cls(ENABLE_EAV.LoaiStyle)
LopDL_cfg = enable_eav_cls(ENABLE_EAV.LopDL)
Style_cfg = enable_eav_cls(ENABLE_EAV.Style)
MultiMedia_cfg = enable_eav_cls(ENABLE_EAV.MultiMedia)
MetaData_cfg = enable_eav_cls(ENABLE_EAV.MetaData)


# 1. Nhóm dữ liệu
class NhomDLAdmin(NhomDL_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(NhomDL_cfg.BASE_FORM, meta.NhomDuLieuMeta, models.NhomDuLieu, constants.NHOM_DL)
    list_display = ('maNhanDang', 'tenNhom', )

# 2. Loại Style
class LoaiStyleAdmin(LoaiStyle_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(LoaiStyle_cfg.BASE_FORM, meta.LoaiStyleMeta, models.LoaiStyle, constants.LOAI_STYLE)
    list_display = ('maNhanDang', 'tenLoaiStyle', )

# 3. Lớp dữ liệu
class LopDLAdmin(LopDL_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(LopDL_cfg.BASE_FORM, meta.LopDuLieuMeta, models.LopDuLieu, constants.LOP_DL)
    list_display = ('maNhanDang', 'tenLop', 'tenHienThiLop', )

# 4. Style
class StyleAdmin(Style_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(Style_cfg.BASE_FORM, meta.StyleMeta, models.Style, constants.STYLE)
    list_display = ('maNhanDang', 'tenStyle', 'kieuDinhDang', )

    # 
    @admin.display(description = 'Kiểu định dạng')
    def kieuDinhDang(self, obj):
        return obj.get_kieuDinhDangStyle_display()

# 5. Dữ liệu đa phương tiện
class DuLieuDaPhuongTienAdmin(MultiMedia_cfg.BASE_ADMIN):
    class Media:
        js = (
            'extra/multiMedia.js',
        )

    form = forms.DuLieuDaPhuongTienForm
    list_display = ('maNhanDang', 'tenDuLieu', 'ngayDuLieu', )

# 6. Meta data
class MetaDataAdmin(MetaData_cfg.BASE_ADMIN):
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
    form = form.form_custom_MaNhanDang(MetaData_cfg.BASE_FORM, meta.MetaDataMeta, models.MetaData, constants.METADATA)
    list_display = ('maNhanDang', 'tenMetaData', )

# register
from django.conf import settings
from .apps import MultimediaConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.NhomDuLieu, NhomDLAdmin)
    admin.site.register(models.LoaiStyle, LoaiStyleAdmin)
    admin.site.register(models.LopDuLieu, LopDLAdmin)
    admin.site.register(models.Style, StyleAdmin)
    admin.site.register(models.DuLieuDaPhuongTien, DuLieuDaPhuongTienAdmin)
    admin.site.register(models.MetaData, MetaDataAdmin)