from . import models

# 1. Loại đơn vi
class LoaiDVMeta:
    class Meta:
        model = models.LoaiDonVi
        fields = '__all__'
        read_only_fields = ['maNhanDang']

# 2. Cấp đơn vị
class CapDVMeta:
    class Meta:
        model = models.CapDonVi
        fields = '__all__'
        read_only_fields = ['maNhanDang']

# 3. Đơn vị
class DonViMeta: 
    class Meta:
        model = models.DonVi
        fields = '__all__'
        read_only_fields = ['maNhanDang']

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