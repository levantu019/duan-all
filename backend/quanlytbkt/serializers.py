from rest_framework import serializers

from . import meta


# 4. Loại trang bị
class LoaiTBKTSerializer(meta.LoaiTBMeta, serializers.ModelSerializer):
    pass

# 5. Xuất xứ
class XuatXuSerializer(meta.XuatXuMeta, serializers.ModelSerializer):
    pass

# 6. Tình trạng trang bị
class TinhTrangTBSerializer(meta.TinhTrangTBMeta, serializers.ModelSerializer):
    pass

# 7. Trang bị khí tài
class TBKTSerializer(meta.TBKTMeta, serializers.ModelSerializer):
    pass
