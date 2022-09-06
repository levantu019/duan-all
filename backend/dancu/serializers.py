from rest_framework_gis import serializers

from .import meta


# 1.Khu dân cư
class KDCSerializer(meta.KDCMeta, serializers.GeoFeatureModelSerializer):
    pass


# 2. Nhà
class Surface_NSerializer(meta.Surface_NMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_NSerializer(meta.Point_NMeta, serializers.GeoFeatureModelSerializer):
    pass


# 3. Công trình phụ trợ
class Surface_CTPTSerializer(meta.Surface_CTPTMeta, serializers.GeoFeatureModelSerializer):
    pass

class Curve_CTPTSerializer(meta.Curve_CTPTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 4. Khối nhà
class KNSerializer(meta.KhoiNhaMeta, serializers.GeoFeatureModelSerializer):
    pass


# 5. Địa danh dân cư
class DDDCSerializer(meta.DDDCMeta, serializers.GeoFeatureModelSerializer):
    pass


# 6. Hạ tầng kỹ thuật khác
class Surface_HTKTKSerializer(meta.Surface_HTKTKMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_HTKTKSerializer(meta.Point_HTKTKMeta, serializers.GeoFeatureModelSerializer):
    pass


# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGSerializer(meta.TKTTVQGMeta, serializers.GeoFeatureModelSerializer):
    pass


# 8. Trạm quan trắc môi trường
class TQTMTSerializer(meta.TQTMTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 9. Trạm quan trắc tài nguyên nước
class TQTTNNSerializer(meta.TQTTNNMeta, serializers.GeoFeatureModelSerializer):
    pass


# 10. Đường dây tải điện
class DDTDSerializer(meta.DDTDMeta, serializers.GeoFeatureModelSerializer):
    pass


# 11. Cột điện
class CotDienSerializer(meta.CotDienMeta, serializers.GeoFeatureModelSerializer):
    pass


# 12. Đường ống dẫn
class DODSerializer(meta.DODMeta, serializers.GeoFeatureModelSerializer):
    pass

# 13. Ranh giới
class RanhGioiSerializer(meta.RanhGioiMeta, serializers.GeoFeatureModelSerializer):
    pass


# 14. Công trình y tế
class Surface_CTYTSerializer(meta.Surface_CTYTMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTYTSerializer(meta.Point_CTYTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 15. Công trình giáo dục
class Surface_CTGDSerializer(meta.Surface_CTGDMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTGDSerializer(meta.Point_CTGDMeta, serializers.GeoFeatureModelSerializer):
    pass


# 16. Công trình thể thao
class Surface_CTTTSerializer(meta.Surface_CTTTMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTTTSerializer(meta.Point_CTTTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 17. Công trình văn hoá
class Surface_CTVHSerializer(meta.Surface_CTVHMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTVHSerializer(meta.Point_CTVHMeta, serializers.GeoFeatureModelSerializer):
    pass


# 18. Công trình thương mại dịch vụ
class Surface_CTTMDVSerializer(meta.Surface_CTTMDVMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTTMDVSerializer(meta.Point_CTTMDVMeta, serializers.GeoFeatureModelSerializer):
    pass


# 19. Công trình tôn giáo tín ngưỡng
class Surface_CTTGTNSerializer(meta.Surface_CTTGTNMeta, serializers.GeoFeatureModelSerializer):
    pass


class Point_CTTGTNSerializer(meta.Point_CTTGTNMeta, serializers.GeoFeatureModelSerializer):
    pass


# 20. Trụ sở cơ quan nhà nước
class Surface_TSCQNNSerializer(meta.Surface_TSCQNNMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_TSCQNNSerializer(meta.Point_TSCQNNMeta, serializers.GeoFeatureModelSerializer):
    pass


# 21. Công trình công nghiệp
class Surface_CTCNSerializer(meta.Surface_CTCNMeta, serializers.GeoFeatureModelSerializer):
    pass

class Curve_CTCNSerializer(meta.Curve_CTCNMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTCNSerializer(meta.Point_CTCNMeta, serializers.GeoFeatureModelSerializer):
    pass


# 22. Cơ sở sản xuất nông lâm nghiệp
class Surface_CSSXNLNSerializer(meta.Surface_CSSXNLNMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CSSXNLNSerializer(meta.Point_CSSXNLNMeta, serializers.GeoFeatureModelSerializer):
    pass


# 23. Khu chức năng đặc thù
class KCNDTSerializer(meta.KCNDTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 24. Công trình xử lý chất thải
class Surface_CTXLCTSerializer(meta.Surface_CTXLCTMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTXLCTSerializer(meta.Point_CTXLCTMeta, serializers.GeoFeatureModelSerializer):
    pass


# 25. Công trình an ninh
class Surface_CTANSerializer(meta.Surface_CTANMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTANSerializer(meta.Point_CTANMeta, serializers.GeoFeatureModelSerializer):
    pass


# 26. Công trình quốc phòng
class Surface_CTQPSerializer(meta.Surface_CTQPMeta, serializers.GeoFeatureModelSerializer):
    pass

class Point_CTQPSerializer(meta.Point_CTQPMeta, serializers.GeoFeatureModelSerializer):
    pass


