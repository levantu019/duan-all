from core.utils import handleString, customFields


# 
def form_custom_MaNhanDang(base_form, meta, model, prefix_MaNhanDang, maNhanDang=None):
    """
        Create change form with maNhanDang field auto
        - meta: metaclass
        - model: object model
        - prefix_MaNhanDang: string
        - base_form: BaseDynamicEntityForm or ModelForm
    """
    class form(base_form):
        __metaclass__ = meta
        new_maNhanDang = maNhanDang

        def __init__(self, *args, **kwargs):
            super(form, self).__init__(*args, **kwargs)

            if self.new_maNhanDang is None:
                self.new_maNhanDang = handleString.generate_MaNhanDang(model, prefix_MaNhanDang)

            self.fields['maNhanDang'].widget = customFields.MA_NHAN_DANG(self.new_maNhanDang, True)

    return form