from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from . import meta, models


# 1. Nhiệm vụ điều hành
class NVDHSerializer(meta.NVDHMeta, serializers.ModelSerializer):
    pass


# 2. Điểm NVDH
class DiemNVDHSerializer(meta.DiemNVDHMeta.Meta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 3. Tuyến NVDH
class TuyenNVDHSerializer(meta.TuyenNVDHMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 4. Vùng NVDH
class VungNVDHSerializer(meta.VungNVDHMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 5. Đơn vị
class DonViSerializer(meta.DonViMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 6. Nhiệm vụ bộ phận
class NVBPSerializer(meta.NVBPMeta, serializers.ModelSerializer):
    pass


# 7. Phương án vị trí
class PAViTriSerializer(meta.PAViTriMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 8. Phê duyệt phương án vị trí
class PDPAViTriSerializer(meta.PDPAViTriMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 9. Phương án tuyến
class PATuyenSerializer(meta.PATuyenMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 10. Phê duyệt phương án tuyến
class PDPATuyenSerializer(meta.PDPATuyenMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 11. Phương án vùng
class PAVungSerializer(meta.PAVungMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 12. Phê duyệt phương án vùng
class PDPAVungSerializer(meta.PDPAVungMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 13. Phê duyệt chung
class PDChungNVBPSerializer(meta.PDChungNVBPMeta, serializers.ModelSerializer):
    pass


# 14. Gán lực lượng
class GanLLSerializer(meta.GanLLMeta, serializers.ModelSerializer):
    pass


# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLSerializer(meta.PDPAGanLLMeta, serializers.ModelSerializer):
    pass


