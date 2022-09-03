from rest_framework_gis import serializers

from .import meta

# 1. Cây độc lập
class CayDocLapSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.CayDocLapMeta

        
# 2. Ranh giới phủ bề mặt
class RGPBMSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.RGPBMMeta


# 3. Bề mặt công trình
class BMCTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BMCTMeta


# 4. Bề mặt khu dân cư
class BMKDCSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BMKDCMeta


# 5. Đất trống
class DatTrongSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DatTrongMeta


# 6. Nước mặt 
class NuocMatSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.NuocMatMeta


# 7. Thực vật đáy biển
class TVDBSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.TVDBMeta
