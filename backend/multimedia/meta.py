from . import models


# 1. Nhóm dữ liệu
class NhomDuLieuMeta:
    class Meta:
        model = models.NhomDuLieu
        fields = '__all__'

# 2. Loại Style
class LoaiStyleMeta:
    class Meta:
        model = models.LoaiStyle
        fields = '__all__'

# 3. Lớp dữ liệu
class LopDuLieuMeta:
    class Meta:
        model = models.LopDuLieu
        fields = '__all__'

# 4. Style
class StyleMeta:
    class Meta:
        model = models.Style
        fields = '__all__'

# 5. Dữ liệu đa phương tiện
class MultiMediaMeta:
    class Meta:
        model = models.DuLieuDaPhuongTien
        fields = '__all__'

# 6. MetaData
class MetaDataMeta:
    class Meta:
        model = models.MetaData
        fields = '__all__'