from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .import meta

# 1. Điểm độ cao
class DDCSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDCMeta


# 2. Đường bình độ
class DBDSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DBDMeta


# 3. Chất đáy
class ChatDaySerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.ChatDayMeta


# 4. Điểm độ sâu
class DDSSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DDSMeta


# 5. Đường bình độ sâu
class DBDSSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DBDSMeta


# 6. Địa hình đặc biệt đáy biển
class Surface_DHDBDBSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Surface_DHDBDBMeta

class Curve_DHDBDBSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.Curve_DHDBDBMeta


# 7. Địa mạo
class DiaMaoSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DiaMaoMeta


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DEMGLPMeta


# 9. Mô hình số độ cao gốc lớp đường
class DEMGLLSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DEMGLLMeta


# 10. Mô hình số độ cao gốc lớp vùng
class DEMGLASerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DEMGLAMeta


# 11. Mô hình số độ cao gốc lớp vùng biển tập
class DEMDLVBTSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.DEMDLVBTMeta


# # 12. Lớp lưới tam giác bất quy tắc (TIN)
# class LTGBQTSerializer(serializers_gis.GeoFeatureModelSerializer):
#     class Meta:
#         model = LopLuoiTamGiacBatQuyTac
#         fields = '__all__'


# # 13. Lớp Raster
# class RSTSerializer(serializers_gis.GeoFeatureModelSerializer):
#     class Meta:
#         model = LopRaster
#         fields = '__all__'


# 14. Hố khoan địa chất
class HKDCSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.HKDCMeta


# 15. Số liệu hố khoan địa chất
class SLHKDCSerializer(serializers.ModelSerializer):
    __metaclass__ = meta.SLHKDCMeta


# 16. Mặt cắt điển hình địa chất
class MCDHSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.MCDHMeta


# 17. Loại Địa chất
class LDCSerializer(serializers_gis.GeoFeatureModelSerializer):
    __metaclass__ = meta.LDCMeta