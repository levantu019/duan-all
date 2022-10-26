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
