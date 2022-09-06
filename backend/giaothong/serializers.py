from rest_framework_gis import serializers

from .import meta


# 1. Đường bộ
class DBSerializer(meta.DuongBoMeta, serializers.GeoFeatureModelSerializer):
    pass


# 2. Cống giao thông
class Curve_CGTSerializer(meta.Curve_CongGTMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CGTSerializer(meta.Point_CongGTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 3. Đường băng
class DBANGSerializer(meta.DBANGMeta, serializers.GeoFeatureModelSerializer):
    pass


# 4. Bãi đáp trực thăng
class BDTTSerializer(meta.BDTTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 5. Báo hiệu hàng hải AIS
class BHHHAISSerializer(meta.BHHHAISMeta, serializers.GeoFeatureModelSerializer):
    pass


# 6. Bến cảng
class BenCangSerializer(meta.BenCangMeta, serializers.GeoFeatureModelSerializer):
    pass


# 7. Cầu tàu
class Surface_CauTauSerializer(meta.Surface_CauTauMeta, serializers.GeoFeatureModelSerializer):
    pass

class Curve_CauTauSerializer(meta.Curve_CauTauMeta, serializers.GeoFeatureModelSerializer):
    pass


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BHDLHHDTSerializer(meta.BHDLHHDTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 9. Các đối tượng hàng hải hải văn
class Surface_CDTHHHVSerializer(meta.Surface_CDTHHHVMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CDTHHHVSerializer(meta.Point_CDTHHHVMeta, serializers.GeoFeatureModelSerializer):
    pass


# 10. Nhóm Âu tàu
class Surface_NATSerializer(meta.Surface_NhomAuTauMeta, serializers.GeoFeatureModelSerializer):
    pass

class Curve_NATSerializer(meta.Curve_NhomAuTauMeta, serializers.GeoFeatureModelSerializer):
    pass