from rest_framework import serializers

from . import meta


# 1. Loại đơn vị
class LoaiDVSerializer(meta.LoaiDVMeta, serializers.ModelSerializer):
    pass

# 2. Cấp đơn vị
class CapDVSerializer(meta.CapDVMeta, serializers.ModelSerializer):
    pass

# 3. Đơn vị
class DonViSerializer(meta.DonViMeta, serializers.ModelSerializer): 
    pass

# 4. Loại trang bị
class LoaiTBKTSerializer(meta.LoaiTBMeta, serializers.ModelSerializer):
    pass

# 5. Xuất xứ
class XuatXuSerializer(meta.XuatXuMeta, serializers.ModelSerializer):
    pass

# 6. Tình trạng trang bị
class TinhTrangTBSerializer(meta.TinhTrangTBMeta, serializers.ModelSerializer):
    pass

# 7. Biên chế trang bị
class BienCheTBSerializer(meta.BienCheTBMeta, serializers.ModelSerializer):
    pass

# 8. Phụ kiện thiết bị
class ThietBiKhiTaiSerializer(meta.ThietBiKhiTaiMeta, serializers.ModelSerializer):
    pass
