from rest_framework_gis import serializers

from .import meta


# 1. Điểm gốc đo đạc quốc gia
class DGDDQGSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DGDDQGMeta


# 2. Điểm đo đạc quốc gia
class DDDQGSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDDQGMeta


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.TDVVTQGMeta