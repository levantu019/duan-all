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
