from rest_framework_gis import serializers

from .import meta


# 1. Vùng biển
class VBSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.VBMeta


# 2. Địa phận hành chính trên biển
class DPHCTBSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DPHCTBMeta


# 3. Đường ranh giới hành chính trên biển
class DRGHCTBSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DRGHCTBMeta


# 4. Địa phận hành chính trên đất liền
class DPHCTDLSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DPHCTDLMeta