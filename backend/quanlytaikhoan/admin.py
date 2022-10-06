from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from jwtauth.utils import funcs

from . import models
from .utils import choices

# Register your models here.
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



# Người dùng
class CustomUserAdmin(UserAdmin):
    list_filter = ()
    search_fields = ()
    readonly_fields = ('avatar',)
    list_display = ('username', 'hoten', 'is_staff', 'avatar', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'anhDaiDien', 'avatar',)}),
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


# Unregister
admin.site.unregister(Group)

# Register
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(models.NguoiDung, CustomUserAdmin)