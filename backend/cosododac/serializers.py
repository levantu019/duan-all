from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    DiemGocDoDacQuocGia,
    DiemDoDacQuocGia,
    TramDinhViVeTinhQuocGia
)


# 1. Điểm gốc đo đạc quốc gia
class DGDDQGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiemGocDoDacQuocGia
        fields = '__all__'


# 2. Điểm đo đạc quốc gia
class DDDQGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiemDoDacQuocGia
        fields = '__all__'


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TramDinhViVeTinhQuocGia
        fields = '__all__'