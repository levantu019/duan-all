from django import forms

# Mã nhận dạng
def MA_NHAN_DANG(value, readonly):
    """
    """
    return forms.TextInput(
        attrs={
            'id': 'ma-nhan-dang',
            'class': 'vTextField',
            'value': value,
            'readonly': readonly,
            },
    )