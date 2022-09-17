from django import forms

from multimedia.models import LopDuLieu

from . import models
from .utils.config import ENABLE_EAV, enable_eav_cls


# Đơn vị
class DonViForm(enable_eav_cls(ENABLE_EAV.DonVi).BASE_FORM):
    class Meta:
        model = models.DonVi
        fields = '__all__'

    maLop = forms.IntegerField(required=True, label='Lớp dữ liệu')

    def __init__(self, *args, **kwargs):
        super(DonViForm, self).__init__(*args, **kwargs)

        id_html_maNhanDangGeo = 'dulieuquantri-manhandang-geo'

        lopdulieu_list = [('', '---------')] + [(i.maLop, i.tenLop) for i in LopDuLieu.objects.all()]
        self.fields['maLop'].widget = forms.Select(
            attrs={
                'onchange': "getValueFields(this.value, '{}')".format(id_html_maNhanDangGeo),
            },
            choices=lopdulieu_list,
        )

        maNhanDang_init = [('', '---------')]
        self.fields['maNhanDang'].widget = forms.Select(
            attrs={
                'id': id_html_maNhanDangGeo
            },
            choices=maNhanDang_init,
        )
