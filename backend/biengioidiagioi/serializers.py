from rest_framework_gis import serializers

from .import meta


# 1. Vùng biển
class VBSerializer(meta.VBMeta, serializers.GeoFeatureModelSerializer):
    pass


# 2. Địa phận hành chính trên biển
class DPHCTBSerializer(meta.DPHCTBMeta, serializers.GeoFeatureModelSerializer):
    pass


# 3. Đường ranh giới hành chính trên biển
class DRGHCTBSerializer(meta.DRGHCTBMeta, serializers.GeoFeatureModelSerializer):
    pass


# 4. Địa phận hành chính trên đất liền
class DPHCTDLSerializer(meta.DPHCTDLMeta, serializers.GeoFeatureModelSerializer):
    pass