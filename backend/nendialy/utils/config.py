from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from . import media
from multimedia.models import DuLieuDaPhuongTien, LopDuLieu


NENDIALY_USE_EAV = True

BASE_FORM = BaseDynamicEntityForm
BASE_ADMIN = BaseEntityAdmin

if not NENDIALY_USE_EAV:
    BASE_FORM = ModelForm
    BASE_ADMIN = ModelAdmin


class AdminCommon:
    class Media:
        js = media.JS_ADMIN_BASE

    if NENDIALY_USE_EAV:
        change_list_template = "admin/add_button_change_list.html"

    #
    def save_model(self, request, obj, form, change):
        try:
            images = request.FILES.getlist("images")
            model_name = obj.__class__._meta.model_name
            lopDL = LopDuLieu.objects.get(maNhanDang=model_name)

            if images:
                for image in images:
                    DuLieuDaPhuongTien.objects.create(pathDuLieu=image, lopDL=lopDL, maNhanDangObj=obj.maNhanDang)

        except Exception as e:
            messages.error(request, _("Can't save image because some error: {}".format(e)))

        super().save_model(request, obj, form, change)
