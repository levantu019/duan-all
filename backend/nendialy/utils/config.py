from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from . import media

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