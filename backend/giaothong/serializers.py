from rest_framework_gis import serializers

from .import meta


# 1. Đường bộ
class DBSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DuongBoMeta


# 2. Cống giao thông
class Curve_CGTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_CongGTMeta

class Point_CGTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CongGTMeta


# 3. Đường băng
class DBANGSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DBANGMeta


# 4. Bãi đáp trực thăng
class BDTTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BDTTMeta


# 5. Báo hiệu hàng hải AIS
class BHHHAISSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BHHHAISMeta


# 6. Bến cảng
class BenCangSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BenCangMeta


# 7. Cầu tàu
class Surface_CauTauSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CauTauMeta

class Curve_CauTauSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_CauTauMeta


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BHDLHHDTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.BHDLHHDTMeta


# 9. Các đối tượng hàng hải hải văn
class Surface_CDTHHHVSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CDTHHHVMeta

class Point_CDTHHHVSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CDTHHHVMeta


# 10. Nhóm Âu tàu
class Surface_NATSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_NhomAuTauMeta

class Curve_NATSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_NhomAuTauMeta