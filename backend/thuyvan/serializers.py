from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .import meta


# 1. Biển đảo
class Surface_BienDaoSerializer(meta.Surface_BienDaoMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

class Point_BienDaoSerializer(meta.Point_BienDaoMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

        
# 2. Đảo
class Surface_DaoSerializer(meta.Surface_DaoMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

class Point_DaoSerializer(meta.Point_DaoMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 3. Bãi bồi
class Surface_BaiBoiSerializer(meta.Surface_BaiBoiMeta, serializers_gis.GeoFeatureModelSerializer):
    pass
    
class Point_BaiBoiSerializer(meta.Point_BaiBoiMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 4. Bãi đá dưới nước
class Surface_BDDNSerializer(meta.Surface_BDDNMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

class Point_BDDNSerializer(meta.Point_BDDNMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 5. Nguồn nước
class Surface_NguonNuocSerializer(meta.Surface_NguonNuocMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

class Point_NguonNuocSerializer(meta.Point_NguonNuocMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 6. Điểm độ cao mực nước
class DDCMNSerializer(meta.DDCMNMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 7. Đường bờ nước
class DBNSerializer(meta.DBNMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 8. Đường mép nước
class DMNSerializer(meta.DMNMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 9. Ranh giới nước mặt quy ước
class RGNMQUSerializer(meta.RGNMQUMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 10. Bờ kè bờ cạp
class BKBCSerializer(meta.BKBCMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 11. Kênh mương
class Surface_KenhMuongSerializer(meta.Surface_KenhMuongMeta, serializers_gis.GeoFeatureModelSerializer):
    pass

class Curve_KenhMuongSerializer(meta.Curve_KenhMuongMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 12. Trạm thu thập TTTV
class TTTTTTVSerializer(meta.TTTTTTVMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 13. Tham số KTTV
class TSKTTVSerializer(meta.TSKTTVMeta, serializers.ModelSerializer):
    pass


# 14. Số liệu sóng, gió, dòng chảy
class SGDCSerializer(meta.SGDCMeta, serializers.ModelSerializer):
    pass


# 15. Tham số nước
class TSNSerializer(meta.TSNMeta, serializers.ModelSerializer):
    pass

