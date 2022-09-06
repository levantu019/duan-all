from django.contrib import admin
from .models import (
    NhomDuLieu,
    LoaiStyle,
    LopDuLieu,
    Style,
    DuLieuDaPhuongTien,
    MetaData
)

from .forms import (
    DuLieuDaPhuongTienForm,
)

class DuLieuDaPhuongTienAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'extra/multiMedia.js',
        )

    form = DuLieuDaPhuongTienForm



from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
class CustomForm(BaseDynamicEntityForm):
    model = NhomDuLieu

class CustomAdmin(BaseEntityAdmin):
    form = CustomForm


# register
from django.conf import settings
from .apps import MultimediaConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(NhomDuLieu, CustomAdmin)
    admin.site.register(LoaiStyle)
    admin.site.register(LopDuLieu)
    admin.site.register(Style)
    admin.site.register(DuLieuDaPhuongTien, DuLieuDaPhuongTienAdmin)
    admin.site.register(MetaData)