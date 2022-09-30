from rest_framework import serializers

from . import meta


# 1. Nhóm dữ liệu
class NhomDuLieuSerialiser(meta.NhomDuLieuMeta, serializers.ModelSerializer):
    pass

# 2. Loại Style
class LoaiStyleSerialiser(meta.LoaiStyleMeta, serializers.ModelSerializer):
    pass

# 3. Lớp dữ liệu
class LopDuLieuSerialiser(meta.LopDuLieuMeta, serializers.ModelSerializer):
    pass

# 4. Style
class StyleSerialiser(meta.StyleMeta, serializers.ModelSerializer):
    pass

# 5. Dữ liệu đa phương tiện
class MultiMediaSerialiser(meta.MultiMediaMeta, serializers.ModelSerializer):
    pass

# 6. MetaData
class MetaDataSerialiser(meta.MetaDataMeta, serializers.ModelSerializer):
    pass
