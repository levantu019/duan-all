from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from jwtauth.utils import funcs
from django.apps import apps

from . import models, forms
from .utils import choices

# Register your models here.
### Auth
# Nhóm tài khoản
class GroupInline(admin.StackedInline):
    model = models.NhomTaiKhoan
    can_delete = False
    formset = forms.NhomTaiKhoanForm

class CustomGroupAdmin(GroupAdmin):
    list_filter = ()
    list_display = ('name',)
    inlines = (GroupInline, )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        formset.save()
        for f in formset.forms:
            obj = f.instance 
            if change:
                obj.group.permissions.clear()
            
            if obj.role == choices.ADMIN:
                perms = funcs.perm_type_app()
                obj.group.permissions.add(*perms)
            elif obj.role == choices.ADMIN_DATA:
                perms = funcs.perm_type_app('nendialy')
                for perm in perms:
                    obj.group.permissions.add(*perm)
            else:
                pass
            
            obj.save()

    # More setup
    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    change_list_template = "admin/change_list_custom.html"
    search_fields = ('ten',)
    def changelist_view(self, request, extra_context=None):  
        extra_tools = []   
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": True, "extra_tools": extra_tools}
        return super(CustomGroupAdmin, self).changelist_view(request, extra_context=extra_context)



# Người dùng
class CustomUserAdmin(UserAdmin):
    list_filter = ()
    search_fields = ()
    readonly_fields = ('avatar',)
    list_display = ('username', 'hoten', 'is_staff', 'avatar', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'anhDaiDien', 'avatar', 'donVi',)}),
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

    # More setup
    class Media:
        js = ('extra/js/jquery-1.12.4.min.js', 'extra/js/treetable.js', 'extra/js/multiMedia.js', 'extra/js/popper.min.js', )
        css = {
            'all': ('extra/css/treetable.css',)
        }

    change_list_template = "admin/change_list_custom.html"
    search_fields = ('username', )
    def changelist_view(self, request, extra_context=None):  
        extra_tools = [
            {
                "type": "filter",
                "text": "Lọc",
                "link": "#",
                "icon": "fa fa-filter",
                "use": True,
                "template": "admin/modal_templates/filter_user.html",
                "action": "/quanlytaikhoan/nguoidung/",
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
                "use": False,
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
        extra_context = {"model_is_tree": False, "btn_default": True, "btn_delete": True, "extra_tools": extra_tools}
        return super(CustomUserAdmin, self).changelist_view(request, extra_context=extra_context)


from .apps import QuanlytaikhoanConfig
apps.get_model('auth', 'Group')._meta.app_label = QuanlytaikhoanConfig.name
apps.get_model('auth', 'Group')._meta.verbose_name = 'Nhóm tài khoản'
apps.get_model('auth', 'Group')._meta.verbose_name_plural = 'Nhóm tài khoản'

# Unregister
admin.site.unregister(Group)

# Register
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(models.NguoiDung, CustomUserAdmin)