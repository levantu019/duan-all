def generate_ID_MaNhanDang(*models):
    """
        * Trả về thẻ 8 ký tự cuối cùng của mã nhận dạng của đối tượng tiếp theo
        - model: lớp
    """
    model_bigest = models[0].objects.all()

    for model in models:
        item = model.objects.all()
        if len(item) > len(model_bigest):
            model_bigest = item

    if len(model_bigest) == 0:
        return '000000001'
    else:
        identifier = model_bigest.last().maNhanDang
        index = int(identifier[-8:]) + 1        
        len_index = len(str(index))

        if len_index < 8:
            return '0' * (8 - len_index) + str(index)
        
        return str(index)


def export_MaTinh(maNhanDang):
    """
        Trả về mã tỉnh được export từ mã nhận dạng
    """
    if len(maNhanDang) == 16:
        return ''
    else:
        return maNhanDang[4:6]
