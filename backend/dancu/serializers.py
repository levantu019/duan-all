from rest_framework_gis import serializers

from .import meta


# 1.Khu dân cư
class KDCSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.KDCMeta


# 2. Nhà
class Surface_NSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_NMeta

class Point_NSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_NMeta


# 3. Công trình phụ trợ
class Surface_CTPTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTPTMeta

class Curve_CTPTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_CTPTMeta


# 4. Khối nhà
class KNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.KhoiNhaMeta


# 5. Địa danh dân cư
class DDDCSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDDCMeta


# 6. Hạ tầng kỹ thuật khác
class Surface_HTKTKSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_HTKTKMeta

class Point_HTKTKSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_HTKTKMeta


# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.TKTTVQGMeta


# 8. Trạm quan trắc môi trường
class TQTMTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.TQTMTMeta


# 9. Trạm quan trắc tài nguyên nước
class TQTTNNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.TQTTNNMeta


# 10. Đường dây tải điện
class DDTDSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDTDMeta


# 11. Cột điện
class CotDienSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.CotDienMeta


# 12. Đường ống dẫn
class DODSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.DODMeta

# 13. Ranh giới
class RanhGioiSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.RGMeta


# 14. Công trình y tế
class Surface_CTYTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTYTMeta

class Point_CTYTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTYTMeta


# 15. Công trình giáo dục
class Surface_CTGDSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTGDMeta

class Point_CTGDSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTGDMeta


# 16. Công trình thể thao
class Surface_CTTTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTTTMeta

class Point_CTTTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTTTMeta


# 17. Công trình văn hoá
class Surface_CTVHSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTVHMeta

class Point_CTVHSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTVHMeta


# 18. Công trình thương mại dịch vụ
class Surface_CTTMDVSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTTMDVMeta

class Point_CTTMDVSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTTMDVMeta


# 19. Công trình tôn giáo tín ngưỡng
class Surface_CTTGTNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTTGTNMeta


class Point_CTTGTNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTTGTNMeta


# 20. Trụ sở cơ quan nhà nước
class Surface_TSCQNNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_TSCQNNMeta

class Point_TSCQNNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_TSCQNNMeta


# 21. Công trình công nghiệp
class Surface_CTCNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTCNMeta

class Curve_CTCNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_CTCNMeta

class Point_CTCNSerializer(serializers.GeoFeatureModelSerializer):
    c__metaclass__ = meta.Point_CTCNMeta


# 22. Cơ sở sản xuất nông lâm nghiệp
class Surface_CSSXNLNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CSSXNLNMeta

class Point_CSSXNLNSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CSSXNLNMeta


# 23. Khu chức năng đặc thù
class KCNDTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.KCNDTMeta


# 24. Công trình xử lý chất thải
class Surface_CTXLCTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTXLCTMeta

class Point_CTXLCTSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTXLCTMeta


# 25. Công trình an ninh
class Surface_CTANSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTANMeta

class Point_CTANSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTANMeta


# 26. Công trình quốc phòng
class Surface_CTQPSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_CTQPMeta

class Point_CTQPSerializer(serializers.GeoFeatureModelSerializer):
    __metaclass__ = meta.Point_CTQPMeta


