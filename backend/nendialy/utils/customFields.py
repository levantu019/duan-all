from django import forms

# Mã nhận dạng
def MA_NHAN_DANG(index, scale, readonly):
    """
    + Trả về thẻ input của trường mã nhận dạng
        - scale: Phần thứ nhất gồm bốn (04) ký tự là mã cơ sở dữ liệu (010N).
        - index: Phần thứ ba gồm tám (08) chữ số của mã nhận dạng, là số thứ tự của đối
tượng cùng kiểu trong tập dữ liệu.        
    """
    return forms.TextInput(
            attrs={
                'id': 'ma-nhan-dang',
                'class': 'vTextField',
                'data-index': index,
                'data-scale': scale,
                'readonly': readonly,
            },
        )


# Mã đối tượng
def MA_DOI_TUONG(choices):
    """
    + Trả về thẻ select của trường mã đối tượng, khi click vào mã đối tượng thì sẽ tạo mã định danh
        - choices: danh sách các options của mã đối tượng.        
    """
    maDT_list = [('', '---------')] + choices

    return forms.Select(
            attrs={
                'onchange': 'set_maNhanDang_madt(this.value)'
            },
            choices=maDT_list,
        )

# Mã tỉnh
def MA_TINH(choices):
    """
    + Trả về thẻ select của trường mã tỉnh, khi click vào mã tỉnh thì sẽ tạo mã định danh
        - choices: danh sách các options của mã tỉnh.        
    """
    maTinh_list = [('', '---------')] + choices

    return forms.Select(
            attrs={
                'id': 'ma-tinh',
                'onchange': 'set_maNhanDang_matinh(this.value)'
            },
            choices=maTinh_list,
        )


# Hình ảnh
def HINH_ANH():
    return forms.ImageField(
        upload_to='images/',
        attrs={
            'multiple': True,
        }
    )