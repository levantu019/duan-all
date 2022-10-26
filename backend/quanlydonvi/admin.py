from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.apps import apps
from django.urls import path
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from nendialy.admin import CustomGeoAdmin
from jwtauth.utils import funcs
from jwtauth.permissions import (
    IsSuperUser,
)

from . import models, meta
from .utils import constants
from core.utils import form, options
from core.utils.config import ENABLE_EAV, AdminCommon, enable_eav_cls


# 
LoaiDV_cfg = enable_eav_cls(ENABLE_EAV.LoaiDVi)
CapDV_cfg = enable_eav_cls(ENABLE_EAV.CapDVi)
DonVi_cfg = enable_eav_cls(ENABLE_EAV.DonVi)



### Đơn vị
# Loại đơn vị
class LoaiDVAdmin(AdminCommon, LoaiDV_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(LoaiDV_cfg.BASE_FORM, meta.LoaiDVMeta, models.LoaiDonVi, constants.LOAI_DONVI)
    list_display = ('maNhanDang', 'ten', )

    # def get_changeform_initial_data(self, request):
    #     return {'maNhanDang': handleString.generate_MaNhanDang(models.LoaiDonVi, constants.LOAI_DONVI)}

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
                "template": "admin/modal_templates/filter_donvi.html",
                "action": "/quanlydonvi/donvi/",
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
        extra_context = {"model_is_tree": False, "btn_default": True if request.user.is_superuser else False, "btn_delete": {'use': True if request.user.is_superuser else False, 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(LoaiDVAdmin, self).changelist_view(request, extra_context=extra_context)

    #
    def save_model(self, request, obj, form, change):
        """
        """
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super().save_model(request, obj, form, change)
            messages.set_level(request, messages.SUCCESS)
            if change:
                messages.success(request, "Chỉnh sửa thành công")
            else:
                messages.success(request, "Thêm mới thành công")
    
    # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super().delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")


# Cấp đơn vị
class CapDVAdmin(AdminCommon, CapDV_cfg.BASE_ADMIN):
    form = form.form_custom_MaNhanDang(CapDV_cfg.BASE_FORM, meta.CapDVMeta, models.CapDonVi, constants.CAP_DONVI)
    list_display = ('maNhanDang', 'ten', 'KHQS', )

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
                "template": "admin/modal_templates/filter_donvi.html",
                "action": "/quanlydonvi/donvi/",
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
        extra_context = {"model_is_tree": False, "btn_default": True if request.user.is_superuser else False, "btn_delete": {'use': True if request.user.is_superuser else False, 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(CapDVAdmin, self).changelist_view(request, extra_context=extra_context)

    #
    def save_model(self, request, obj, form, change):
        """
        """
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super().save_model(request, obj, form, change)
            messages.set_level(request, messages.SUCCESS)
            if change:
                messages.success(request, "Chỉnh sửa thành công")
            else:
                messages.success(request, "Thêm mới thành công")
    
    # 
    def delete_model(self, request, obj):
        if not request.user.is_superuser:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Bạn không có quyền cho hành động này")
        else:
            super().delete_model(request, obj)
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, "Xoá thành công")


# Đơn vị
class DonViAdmin(AdminCommon, CustomGeoAdmin, DonVi_cfg.BASE_ADMIN):
    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', )
        css = {
            'all': ('extra/css/treetable.css', )
        }

    form = form.form_custom_MaNhanDang(DonVi_cfg.BASE_FORM, meta.DonViMeta, models.DonVi, constants.DONVI)
    list_display = ('maNhanDang', 'ten', 'capDonVi', 'loaiDonVi', )
    search_fields = ('maNhanDang', 'ten', )

    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_donvi.html",
                "action": "/quanlydonvi/donvi/",
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
        extra_context = {"model_is_tree": True, "btn_default": True if request.user.is_superuser else False, "btn_delete": {'use': True if request.user.is_superuser else False, 'value': 'delete_selected'}, "extra_tools": extra_tools}
        return super(DonViAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/add/', self.add_children_view, name='donvi_add_children'),
            path('map/', self.show_data_map, name='donvi_show_data_map'),
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
            messages.error(request, "Lỗi không thể thêm mới bản ghi")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def show_data_map(self, request, from_url='', extra_context=None):
        '''
            View hiển thị bảng thông tin đơn vị và bản đồ
        '''
        user = request.user

        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": False,
                "template": "admin/modal_templates/filter_tbkt.html",
                "action": "/quanlydonvi/donvi/map/",
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
        ]   
        extra_context = {"extra_tools": extra_tools}
        list_fields = ['phienHieuDonVi', 'ten', 'capDonVi__ten', 'loaiDonVi__ten']
        list_display_fields = ['STT', 'Phiên hiệu đơn vị', 'Tên đơn vị', 'Cấp đơn vị', 'Loại đơn vị']

        if user.is_superuser:
            data_request = request.GET
            if bool(data_request):
                results_query = []

                if 'q' in data_request:
                    key = data_request.get('q')
                    for item in self.search_fields:
                        results_query.append(models.DonVi.objects.filter(**{item:key}))
                else:
                    from django.db.models import Q
                    condition = True

                    for field in data_request:
                        key = data_request.get(field)
                        condition = condition & Q(**{field:key})
                    
                        
            else:
                data = models.DonVi.objects.values(*list_fields)
        else:
            dvi = user.donVi
            if dvi:
                data = [{'phienHieuDonVi': dvi.phienHieuDonVi, 'ten':dvi.ten, 'capDonVi__ten': dvi.capDonVi.ten, 'loaiDonVi__ten': dvi.loaiDonVi.ten}]
            else:
                data = []

        row_data = []

        for idx, val in enumerate(data, start=1):
            row = len(list_display_fields) * "<td style='cursor: pointer'>{}</td>"
            row = row.format(idx, *[val[i] for i in val])

            row_data.append({'info': mark_safe(row)})

        extra_context["data_wating_headers"] = list_display_fields
        extra_context["data_wating_rows"] = row_data

        extra_context = options.changelist_view(self, request, extra_context)
        request.current_app = self.admin_site.name
        # context = dict(
        #    # Include common variables for rendering the admin template.
        #    self.admin_site.each_context(request),
        #    # Anything else you want in the context...
        #    key=value,
        # )
        return TemplateResponse(request, "admin/other_templates/data_table_map.html", extra_context)

# Register
from django.conf import settings
from .apps import QuanlydonviConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.LoaiDonVi, LoaiDVAdmin)
    admin.site.register(models.CapDonVi, CapDVAdmin)
    admin.site.register(models.DonVi, DonViAdmin)
