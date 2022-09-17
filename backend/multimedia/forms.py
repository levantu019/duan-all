from django import forms

from .models import (
    LopDuLieu,
    DuLieuDaPhuongTien,
)
from .utils.config import ENABLE_EAV, enable_eav_cls

class DuLieuDaPhuongTienForm(enable_eav_cls(ENABLE_EAV.MultiMedia).BASE_FORM):
    class Meta:
        model = DuLieuDaPhuongTien
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DuLieuDaPhuongTienForm, self).__init__(*args, **kwargs)

        id_html_maNhanDang = 'dulieudaphuongtien_manhandang'
        lopdulieu_list = [('', '---------')] + [(i.maLop, i.tenLop) for i in LopDuLieu.objects.all()]
        self.fields['maLop'].widget = forms.Select(
            attrs={
                'onchange': "getValueFields(this.value, '{}')".format(id_html_maNhanDang),
            },
            choices=lopdulieu_list,
        )

        maNhanDang_init = [('', '---------')]
        self.fields['maNhanDang'].widget = forms.Select(
            attrs={
                'id': id_html_maNhanDang
            },
            choices=maNhanDang_init,
        )
