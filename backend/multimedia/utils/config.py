from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from . import media

# 
class ENABLE_EAV:
    NhomDL = True
    LoaiStyle = True
    LopDL = True
    Style = True
    MultiMedia = True
    MetaData = True


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

# 1. Loại đơn vi

# 2. Cấp đơn vị

# 3. Đơn vị

# 4. Loại trang bị

# 5. Xuất xứ

# 6. Tình trạng trang bị

# 7. Biên chế trang bị

# 8. Phụ kiện thiết bị
