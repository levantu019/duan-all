from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .import meta

# 1. Điểm độ cao
class DDCSerializer(meta.DDCMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 2. Đường bình độ
class DBDSerializer(meta.DBDMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 3. Chất đáy
class ChatDaySerializer(meta.ChatDayMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 4. Điểm độ sâu
class DDSSerializer(meta.DDSMeta, serializers_gis.GeoFeatureModelSerializer):
    pass


# 5. Đường bình độ sâu
class DBDSSerializer(meta.DBDSMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 6. Địa hình đặc biệt đáy biển
class Surface_DHDBDBSerializer(meta.Surface_DHDBDBMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 

class Curve_DHDBDBSerializer(meta.Curve_DHDBDBMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 7. Địa mạo
class DiaMaoSerializer(meta.DiaMaoMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPSerializer(meta.DEMGLPMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 9. Mô hình số độ cao gốc lớp đường
class DEMGLLSerializer(meta.DEMGLLMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 10. Mô hình số độ cao gốc lớp vùng
class DEMGLASerializer(meta.DEMGLAMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 11. Mô hình số độ cao gốc lớp vùng biển tập
class DEMDLVBTSerializer(meta.DEMDLVBTMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


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
class HKDCSerializer(meta.HKDCMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 15. Số liệu hố khoan địa chất
class SLHKDCSerializer(meta.SLHKDCMeta, serializers.ModelSerializer):
    pass 


# 16. Mặt cắt điển hình địa chất
class MCDHSerializer(meta.MCDHMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 


# 17. Loại Địa chất
class LDCSerializer(meta.LDCMeta, serializers_gis.GeoFeatureModelSerializer):
    pass 