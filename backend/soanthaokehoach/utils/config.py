from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from . import media

# 
class ENABLE_EAV:
    NVDH = True
    DiemNVDH = True
    TuyenNVDH = True
    VungNVDH = True
    NVBP = True
    PhuongAnViTri = True
    PheDuyetPhuongAnViTri = True
    PhuongAnTuyen = True
    PheDuyetPhuongAnTuyen = True
    PhuongAnVung = True
    PheDuyetPhuongAnVung = True
    PheDuyetChungNVBP = True
    GanLucLuong = True
    PheDuyetPhuongAnGanLucLuong = True


# Default use eav
class USE_EAV:
    BASE_FORM = BaseDynamicEntityForm
    BASE_ADMIN = BaseEntityAdmin

class USE_DEFAULT:
    BASE_FORM = ModelForm
    BASE_ADMIN = ModelAdmin

# 
def enable_eav_cls(eav=True):
    if eav:
        return USE_EAV
    return USE_DEFAULT

# 
class AdminCommon:
    class Media:
        js = media.MODAL_JS

    change_list_template = "admin/add_button_change_list.html"
