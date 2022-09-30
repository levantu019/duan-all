from django.contrib import admin
from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from . import models, forms, meta
from .utils import constants, form, media, handleString
from .utils.config import ENABLE_EAV, AdminCommon, enable_eav_cls


#
NhomDL_cfg = enable_eav_cls(ENABLE_EAV.NhomDL)
LoaiStyle_cfg = enable_eav_cls(ENABLE_EAV.LoaiStyle)
LopDL_cfg = enable_eav_cls(ENABLE_EAV.LopDL)
Style_cfg = enable_eav_cls(ENABLE_EAV.Style)
MultiMedia_cfg = enable_eav_cls(ENABLE_EAV.MultiMedia)
MetaData_cfg = enable_eav_cls(ENABLE_EAV.MetaData)


# 1. Nhóm dữ liệu
class NhomDLAdmin(AdminCommon, NhomDL_cfg.BASE_ADMIN):
    form = forms.NhomDuLieuForm
    list_display = ("maNhanDang", "tenNhom",)
    exclude = ("tenNhom",)

    #
    def save_model(self, request, obj, form, change):
        obj.tenNhom = apps.get_app_config(obj.maNhanDang).verbose_name
        super().save_model(request, obj, form, change)


# 2. Loại Style
class LoaiStyleAdmin(AdminCommon, LoaiStyle_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(
        LoaiStyle_cfg.BASE_FORM, meta.LoaiStyleMeta, models.LoaiStyle, constants.LOAI_STYLE
    )
    list_display = ("maNhanDang", "tenLoaiStyle",)

    #
    def save_model(self, request, obj, form, change):
        obj.maNhanDang = handleString.generate_MaNhanDang(models.LoaiStyle, constants.LOAI_STYLE)
        super().save_model(request, obj, form, change)


# 3. Lớp dữ liệu
class LopDLAdmin(AdminCommon, LopDL_cfg.BASE_ADMIN):
    exclude = ("content_type",)

    form = forms.LopDuLieuForm
    list_display = ("maNhanDang", "tenHienThiLop",)

    #
    def save_model(self, request, obj, form, change):
        model = ContentType.objects.get(model=obj.maNhanDang)
        obj.content_type = model

        if obj.kieuLop is None or obj.kieuLop == "":
            self.kieuLop = model.model_class().type_model

        if obj.tenHienThiLop is None or obj.tenHienThiLop == "":
            obj.tenHienThiLop = obj.content_type.name

        super().save_model(request, obj, form, change)


# 4. Style
class StyleAdmin(AdminCommon, Style_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(Style_cfg.BASE_FORM, meta.StyleMeta, models.Style, constants.STYLE)
    list_display = ("maNhanDang", "tenStyle", "kieuDinhDang",)

    #
    def save_model(self, request, obj, form, change):
        obj.maNhanDang = handleString.generate_MaNhanDang(models.Style, constants.STYLE)

        super().save_model(request, obj, form, change)

    @admin.display(description="Kiểu định dạng")
    def kieuDinhDang(self, obj):
        return obj.get_kieuDinhDangStyle_display()


# 5. Dữ liệu đa phương tiện
class DuLieuDaPhuongTienAdmin(AdminCommon, MultiMedia_cfg.BASE_ADMIN):
    form = forms.DuLieuDaPhuongTienForm
    list_display = ("maNhanDang", "tenDuLieu", "ngayDuLieu", "lopDL", "maNhanDangObj",)

    # 
    def save_model(self, request, obj, form, change):
        obj.maNhanDang = handleString.generate_MaNhanDang(models.DuLieuDaPhuongTien, constants.DL_MULTIMEDIA)

        super().save_model(request, obj, form, change)

# 6. Meta data
class MetaDataAdmin(AdminCommon, MetaData_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(MetaData_cfg.BASE_FORM, meta.MetaDataMeta, models.MetaData, constants.METADATA)
    list_display = ( "maNhanDang", "tenMetaData",)


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
