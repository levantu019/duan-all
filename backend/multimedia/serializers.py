from rest_framework import serializers

from .models import (
    NhomDuLieu,
    LoaiStyle,
    LopDuLieu,
    Style,
    DuLieuDaPhuongTien,
    MetaData
)

# 1. Nhóm dữ liệu
class NhomDuLieuSerialiser(serializers.ModelSerializer):
    class Meta:
        model = NhomDuLieu
        fields = '__all__'

# 2. Loại Style
class LoaiStyleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = LoaiStyle
        fields = '__all__'

# 3. Lớp dữ liệu
class LopDuLieuSerialiser(serializers.ModelSerializer):
    class Meta:
        model = LopDuLieu
        fields = '__all__'

# 4. Style
class StyleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

# 5. Dữ liệu đa phương tiện
class MultiMediaSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DuLieuDaPhuongTien
        fields = '__all__'

# 6. MetaData
class MetaDataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = '__all__'