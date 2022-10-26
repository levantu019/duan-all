from . import models

# 4. Loại trang bị
class LoaiTBMeta:
    class Meta:
        model = models.LoaiTrangBiKhiTai
        fields = '__all__'
        read_only_fields = ['maNhanDang']

# 5. Xuất xứ
class XuatXuMeta:
    class Meta:
        model = models.XuatXu
        fields = '__all__'
        read_only_fields = ['maNhanDang']

# 6. Tình trạng trang bị
class TinhTrangTBMeta:
    class Meta:
        model = models.TinhTrang
        fields = '__all__'
        read_only_fields = ['maNhanDang']

# 7. Biên chế trang bị
class TBKTMeta:
    class Meta:
        model = models.TrangBiKhiTai
        fields = '__all__'
        read_only_fields = ['maNhanDang']