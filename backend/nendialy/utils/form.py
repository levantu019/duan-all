from django import forms

from nendialy.choices import NenDiaLy
from . import constants, handleString, customFields


# 
def base_form(meta, maDoiTuong, *models):
    """
        Create a base form from meta and models
    """
    class form(forms.ModelForm):
        maTinh = forms.IntegerField(required=False, label='Mã tỉnh')
        __metaclass__ = meta

        def __init__(self, *args, **kwargs):
            super(form, self).__init__(*args, **kwargs)

            index = handleString.generate_ID_MaNhanDang(*models)

            self.fields['maTinh'].widget = customFields.MA_TINH(NenDiaLy.MATINH_CHOICES)
            self.fields['maDoiTuong'].widget = customFields.MA_DOI_TUONG(maDoiTuong)
            self.fields['maNhanDang'].widget = customFields.MA_NHAN_DANG(index, constants.PREFIX_IDENTIFIER, True)
    
    return form
