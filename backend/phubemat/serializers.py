from rest_framework_gis import serializers

from .import meta

# 1. Cây độc lập
class CayDocLapSerializer(meta.CayDocLapMeta, serializers.GeoFeatureModelSerializer):
    pass

        
# 2. Ranh giới phủ bề mặt
class RGPBMSerializer(meta.RGPBMMeta, serializers.GeoFeatureModelSerializer):
    pass


# 3. Bề mặt công trình
class BMCTSerializer(meta.BMCTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 4. Bề mặt khu dân cư
class BMKDCSerializer(meta.BMKDCMeta, serializers.GeoFeatureModelSerializer):
    pass


# 5. Đất trống
class DatTrongSerializer(meta.DatTrongMeta, serializers.GeoFeatureModelSerializer):
    pass


# 6. Nước mặt 
class NuocMatSerializer(meta.NuocMatMeta, serializers.GeoFeatureModelSerializer):
    pass


# 7. Thực vật đáy biển
class TVDBSerializer(meta.TVDBMeta, serializers.GeoFeatureModelSerializer):
    pass
