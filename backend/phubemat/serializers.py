from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    CayDocLap,
    RanhGioiPhuBeMat,
    BeMatCongTrinh,
    BeMatKhuDanCu,
    DatTrong,
    NuocMat,
    ThucVatDayBien
)

# 1. Cây độc lập
class CDLSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CayDocLap
        fields = '__all__'

        
# 2. Ranh giới phủ bề mặt
class RGPBMSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = RanhGioiPhuBeMat
        fields = '__all__'


# 3. Bề mặt công trình
class BMCTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BeMatCongTrinh
        fields = '__all__'


# 4. Bề mặt khu dân cư
class BMKDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BeMatKhuDanCu
        fields = '__all__'


# 5. Đất trống
class DTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DatTrong
        fields = '__all__'


# 6. Nước mặt 
class NMSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = NuocMat
        fields = '__all__'


# 7. Thực vật đáy biển
class TVDBSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = ThucVatDayBien
        fields = '__all__'
