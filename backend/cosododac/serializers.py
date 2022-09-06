from rest_framework_gis import serializers

from .import meta


# 1. Điểm gốc đo đạc quốc gia
class DGDDQGSerializer(meta.DGDDQGMeta, serializers.GeoFeatureModelSerializer):
    pass


# 2. Điểm đo đạc quốc gia
class DDDQGSerializer(meta.DDDQGMeta, serializers.GeoFeatureModelSerializer):
    pass


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGSerializer(meta.TDVVTQGMeta, serializers.GeoFeatureModelSerializer):
    pass