from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin


# 
class ENABLE_EAV:
    LoaiDVi = True
    CapDVi = True
    DonVi = True
    Group = True
    User = True
    LoaiTB = True
    XuatXu = True
    TinhTrangTB = True
    BienCheTB = True
    PhuKienTB = True


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


# 1. Loại đơn vi

# 2. Cấp đơn vị

# 3. Đơn vị

# 4. Loại trang bị

# 5. Xuất xứ

# 6. Tình trạng trang bị

# 7. Biên chế trang bị

# 8. Phụ kiện thiết bị
