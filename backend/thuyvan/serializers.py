from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .import meta


# 1. Biển đảo
class Surface_BienDaoSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_BienDaoMeta

class Point_BienDaoSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_BienDaoMeta

        
# 2. Đảo
class Surface_DaoSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_DaoMeta

class Point_DaoSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_DaoMeta


# 3. Bãi bồi
class Surface_BaiBoiSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_BaiBoiMeta
    
class Point_BaiBoiSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_BaiBoiMeta


# 4. Bãi đá dưới nước
class Surface_BDDNSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_BDDNMeta

class Point_BDDNSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_BDDNMeta


# 5. Nguồn nước
class Surface_NguonNuocSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_NguonNuocMeta

class Point_NguonNuocSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_NguonNuocMeta


# 6. Điểm độ cao mực nước
class DDCMNSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDCMNMeta


# 7. Đường bờ nước
class DBNSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DBNMeta


# 8. Đường mép nước
class DMNSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DMNMeta


# 9. Ranh giới nước mặt quy ước
class RGNMQUSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.RGNMQUMeta


# 10. Bờ kè bờ cạp
class BKBCSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.BKBCMeta


# 11. Kênh mương
class Surface_KenhMuongSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_KenhMuongMeta
class Curve_KenhMuongSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_KenhMuongMeta


# 12. Trạm thu thập TTTV
class TTTTTTVSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.TTTTTTVMeta


# 13. Tham số KTTV
class TSKTTVSerializer(serializers.ModelSerializer):
    __metaclass__ = meta.TSKTTVMeta


# 14. Số liệu sóng, gió, dòng chảy
class SGDCSerializer(serializers.ModelSerializer):
    __metaclass__ = meta.SGDCMeta


# 15. Tham số nước
class TSNSerializer(serializers.ModelSerializer):
    __metaclass__ = meta.TSNMeta

