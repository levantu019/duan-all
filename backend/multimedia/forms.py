from django import forms
from .models import (
    NhomDuLieu,
    LoaiStyle,
    LopDuLieu,
    Style,
    DuLieuDaPhuongTien,
    MetaData
)

class DuLieuDaPhuongTienForm(forms.ModelForm):
    class Meta:
        model = DuLieuDaPhuongTien
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DuLieuDaPhuongTienForm, self).__init__(*args, **kwargs)

        try:
            self.initial['maLop'] = kwargs['instance'].maLop.maLop
        except:
            pass

        lopdulieu_list = [('', '---------')] + [(i.maLop, i.tenLop) for i in LopDuLieu.objects.all()]
        self.fields['maLop'].widget = forms.Select(
            attrs={
                'onchange': 'getValueFields(this.value)',
            },
            choices=lopdulieu_list,
        )

        maNhanDang_init = [('', '---------')]
        self.fields['maNhanDang'].widget = forms.Select(
            attrs={
                'id': 'dulieudaphuongtien_manhandang'
            },
            choices=maNhanDang_init,
        )
