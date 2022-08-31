from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    VungBien,
    DiaPhanHanhChinhTrenBien,
    DuongRanhGioiHanhChinhTrenBien
)


# 1. Vùng biển
class VBSerializer(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = VungBien
        fields = '__all__'
        geo_field = 'GM_Surface'


# 2. Địa phận hành chính trên biển
class DPHCTBSerializer(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = DiaPhanHanhChinhTrenBien
        fields = '__all__'
        geo_field = 'GM_Surface'


# 3. Đường ranh giới hành chính trên biển
class DRGHCTBSerializer(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = DuongRanhGioiHanhChinhTrenBien
        fields = '__all__'        
        geo_field = 'GM_Curve'