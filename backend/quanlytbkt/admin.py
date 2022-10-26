from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.contrib.admin import actions
from django.http import HttpResponseRedirect
from django.apps import apps
from django.urls import path
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from jwtauth.utils import funcs
from jwtauth.permissions import (
    IsSuperUser,
)

from . import models, meta
from .utils import constants, form, choices as dlqt
from .utils.config import ENABLE_EAV, AdminCommon, enable_eav_cls


# 
LoaiTB = enable_eav_cls(ENABLE_EAV.LoaiTB)
XuatXu = enable_eav_cls(ENABLE_EAV.XuatXu)
TinhTrangTB = enable_eav_cls(ENABLE_EAV.TinhTrangTB)
PCCL = enable_eav_cls(ENABLE_EAV.PCCL)
TBKT = enable_eav_cls(ENABLE_EAV.TBKT)



### Trang thiết bị
# Loại trang bị
class LoaiTBAdmin(AdminCommon, LoaiTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(LoaiTB.BASE_FORM, meta.LoaiTBMeta, models.LoaiTrangBiKhiTai, constants.LOAI_TB)
    list_display = ('maNhanDang', 'ten',)

    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    search_fields = ('maNhanDang', )
    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlytbkt/trangbikhitai/",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#filter-modal"
                    }
                ]
            },
            {
                "type": "report",
                "text": "Báo cáo",
                "link": "#",
                "icon": "fa fa-print",
                "use": True,
                "template": False,
                "data": []
            },
            {
                "type": "field",
                "text": "Thêm trường",
                "link": "#",
                "icon": "fa fa-plus-circle",
                "use": True if request.user.is_superuser else False,
                "template": "admin/modal_templates/field.html",
                "action": "",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#field-modal"
                    }
                ]
            },
        ]   
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": {'use': True if request.user.is_superuser else False , 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(LoaiTBAdmin, self).changelist_view(request, extra_context=extra_context)

        # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super(LoaiTBAdmin, self).delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")

# Xuất xứ
class XuatXuAdmin(AdminCommon, XuatXu.BASE_ADMIN):
    list_display = ('maNhanDang', 'ten', )
    prepopulated_fields = {'maNhanDang': ('ten',)}
    readonly_fields = ()

    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    search_fields = ('maNhanDang', )
    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlytbkt/trangbikhitai/",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#filter-modal"
                    }
                ]
            },
            {
                "type": "report",
                "text": "Báo cáo",
                "link": "#",
                "icon": "fa fa-print",
                "use": True,
                "template": False,
                "data": []
            },
            {
                "type": "field",
                "text": "Thêm trường",
                "link": "#",
                "icon": "fa fa-plus-circle",
                "use": True if request.user.is_superuser else False,
                "template": "admin/modal_templates/field.html",
                "action": "",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#field-modal"
                    }
                ]
            },
        ]   
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": {'use': True if request.user.is_superuser else False , 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(XuatXuAdmin, self).changelist_view(request, extra_context=extra_context)

        # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super(XuatXuAdmin, self).delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")


# Tình trạng trang bị
class TinhTrangTBAdmin(AdminCommon, TinhTrangTB.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(TinhTrangTB.BASE_FORM, meta.TinhTrangTBMeta, models.TinhTrang, constants.TINHTRANG_TB)
    list_display = ('maNhanDang', 'ten', )

    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    search_fields = ('maNhanDang', )
    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlytbkt/trangbikhitai/",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#filter-modal"
                    }
                ]
            },
            {
                "type": "report",
                "text": "Báo cáo",
                "link": "#",
                "icon": "fa fa-print",
                "use": True,
                "template": False,
                "data": []
            },
            {
                "type": "field",
                "text": "Thêm trường",
                "link": "#",
                "icon": "fa fa-plus-circle",
                "use": True if request.user.is_superuser else False,
                "template": "admin/modal_templates/field.html",
                "action": "",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#field-modal"
                    }
                ]
            },
        ]   
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": {'use': True if request.user.is_superuser else False , 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(TinhTrangTBAdmin, self).changelist_view(request, extra_context=extra_context)

        # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super(TinhTrangTBAdmin, self).delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")


# Phân cấp chất lượng
class PCCLAdmin(AdminCommon, PCCL.BASE_ADMIN):
    list_display = ('maNhanDang', 'ten', )

    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    search_fields = ('maNhanDang', )
    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlytbkt/trangbikhitai/",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#filter-modal"
                    }
                ]
            },
            {
                "type": "report",
                "text": "Báo cáo",
                "link": "#",
                "icon": "fa fa-print",
                "use": True,
                "template": False,
                "data": []
            },
            {
                "type": "field",
                "text": "Thêm trường",
                "link": "#",
                "icon": "fa fa-plus-circle",
                "use": True if request.user.is_superuser else False,
                "template": "admin/modal_templates/field.html",
                "action": "",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#field-modal"
                    }
                ]
            },
        ]   
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": {'use': True if request.user.is_superuser else False , 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(PCCLAdmin, self).changelist_view(request, extra_context=extra_context)

        # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super(PCCLAdmin, self).delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")


# Trang bị khí tài
class TBKTAdmin(AdminCommon, TBKT.BASE_ADMIN):
    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    form = form.form_custom_MaNhanDang(TBKT.BASE_FORM, meta.TBKTMeta, models.TrangBiKhiTai, constants.TBKT)
    list_display = ('ten', 'thaoTacNhap', 'tenDonVi', )
    exclude = ('congBo', 'thaoTacNhap', 'thongBao', )
    readonly_fields = ('donVi', )
    search_fields = ('maNhanDang', 'ten', )
    actions = ['custom_delete']

    @admin.display(description='Tên đơn vị')
    def tenDonVi(self, instance):
        return instance.donVi.ten if instance.donVi else '-'

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.exclude = ()
            self.readonly_fields = ()
        else:            
            self.exclude = ('congBo', 'thaoTacNhap', 'thongBao', )
            self.readonly_fields = ('donVi', )
        return super(TBKTAdmin, self).get_form(request, obj, **kwargs)

    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlytbkt/trangbikhitai/",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#filter-modal"
                    }
                ]
            },
            {
                "type": "report",
                "text": "Báo cáo",
                "link": "#",
                "icon": "fa fa-print",
                "use": True,
                "template": False,
                "data": []
            },
            {
                "type": "field",
                "text": "Thêm trường",
                "link": "#",
                "icon": "fa fa-plus-circle",
                "use": True if request.user.is_superuser else False,
                "template": "admin/modal_templates/field.html",
                "action": "",
                "data": [
                    {
                        "name": "toggle",
                        "value": "modal"
                    },
                    {
                        "name": "target",
                        "value": "#field-modal"
                    }
                ]
            },
        ]   
        extra_context = {"model_is_tree": True, "btn_default": True, "btn_delete": {'use': True , 'value': 'custom_delete'}, "extra_tools": extra_tools}
        return super(TBKTAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/<path:object_donvi>/add/', self.add_children_view, name='donvi_add_children'),
            path('<path:object_id>/accept/', self.accept_new_record, name='accept_new_record'),
        ]

        return my_urls + urls

    def add_children_view(self, request, object_id, object_donvi, form_url='', extra_context=None):
        try:
            data = request.GET.copy()
            data["parent"] = object_id
            data["donVi"] = object_donvi if object_donvi != 'None' else None
            request.GET = data
            return super(TBKTAdmin, self).add_view(
                request, form_url, extra_context
            )
        except ValidationError as e:
            messages.error(request, "Lỗi không thể thêm mới bản ghi")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    # 
    @permission_classes([IsSuperUser])
    def accept_new_record(self, request, object_id, form_url='', extra_context=None):
        try:
            obj = models.TrangBiKhiTai.objects.get(maNhanDang=object_id)
            obj.congBo = True
            obj.save()
            messages.success(request, "{} đã được chấp nhận".format(object_id))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except:
            messages.error(request, "Đã có lỗi xảy ra, vui lòng thử lại sau")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    #
    def save_model(self, request, obj, form, change):
        """
        """
        if not request.user.is_superuser:
            if change:
                obj.thaoTacNhap = dlqt.TT_NHAP_EDIT

            # Nếu thực hiện thay đổi dữ liệu, người thay đổi không phải trong đơn vị đó thì không đổi được
            if request.user.donVi != obj.donVi:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Bạn không thể thao tác với dữ liệu của đơn vị khác")
            else:             
                obj.donVi = request.user.donVi
                obj.thaoTacNhap = dlqt.TT_NHAP_NEW   
                super().save_model(request, obj, form, change)
                messages.set_level(request, messages.SUCCESS)
                if change:
                    messages.success(request, "Trang bị {} đã được sửa thành công".format(obj.maNhanDang))
                else:
                    messages.success(request, "Trang bị {} đã được thêm thành công".format(obj.maNhanDang))
        else:
            super().save_model(request, obj, form, change)
            messages.set_level(request, messages.SUCCESS)
            if change:
                messages.success(request, "Trang bị {} đã được sửa thành công".format(obj.maNhanDang))
            else:
                messages.success(request, "Trang bị {} đã được thêm thành công".format(obj.maNhanDang))
    
    # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            if request.user.donVi != obj.donVi:
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Bạn không thể xoá dữ liệu của đơn vị khác")
            else:                
                super().delete_model(request, obj)
        else:
            super().delete_model(request, obj)

    #
    @admin.action(description='Xoá')
    def custom_delete(self, request, queryset):     
        if not request.user.is_superuser:
            has_obj_not_delete = False
            objs_not_delete = []
            for object in queryset:
                if object.donVi != request.user.donVi:
                    has_obj_not_delete = True
                    objs_not_delete.append(object.ten)
            
            if has_obj_not_delete:            
                messages.set_level(request, messages.ERROR)
                messages.error(request, "Bạn không thể xoá dữ liệu của đơn vị khác: " + ", ".join(objs_not_delete))
            else:
                object.delete()         
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, "Đã xoá trang bị: {}".format(object.ten))
        else:
            queryset.delete()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Đã xoá trang bị")

    # 
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions



# Dữ liệu đa phương tiện
class MultiMediaAdmin(AdminCommon, PCCL.BASE_ADMIN):
    list_display = ('ten', 'path', 'trangBiKhiTai', )



# Register
from django.conf import settings
from .apps import QuanlytbktConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.LoaiTrangBiKhiTai, LoaiTBAdmin)
    admin.site.register(models.XuatXu, XuatXuAdmin)
    admin.site.register(models.TinhTrang, TinhTrangTBAdmin)
    admin.site.register(models.TrangBiKhiTai, TBKTAdmin)
    admin.site.register(models.PhanCapChatLuong, PCCLAdmin)
