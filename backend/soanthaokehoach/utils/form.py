from django import forms

from . import handleString, customFields


# 
def form_custom_MaNhanDang(meta, model, prefix_MaNhanDang):
    class form(forms.ModelForm):
        __metaclass__ = meta

        def __init__(self, *args, **kwargs):
            super(form, self).__init__(*args, **kwargs)

            new_maNhanDang = handleString.generate_MaNhanDang(model, prefix_MaNhanDang)

            self.fields['maNhanDang'].widget = customFields.MA_NHAN_DANG(new_maNhanDang, True)

    return form