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

admin.site.register(NhomDuLieu)
admin.site.register(LoaiStyle)
admin.site.register(LopDuLieu)
admin.site.register(Style)
admin.site.register(DuLieuDaPhuongTien, DuLieuDaPhuongTienAdmin)
admin.site.register(MetaData)