from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    DiemDoCao,
    DuongBinhDo,
    ChatDay,
    DiemDoSau,
    DuongBinhDoSau,
    DiaHinhDacBietDayBien,
    DiaMao,
    MoHinhSoDoCaoGocLopDiem,
    MoHinhSoDoCaoGocLopDuong,
    MoHinhSoDoCaoGocLopVung,
    MoHinhSoDoCaoGocLopVungBienTap,
    LopLuoiTamGiacBatQuyTac,
    LopRaster,
    HoKhoanDiaChat,
    SoLieuHKDC,
    MatCatDienHinh,
    LoaiDiaChat
)

# 1. Điểm độ cao
class DDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiemDoCao
        fields = '__all__'


# 2. Đường bình độ
class DBDSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongBinhDo
        fields = '__all__'


# 3. Chất đáy
class CHATDAYSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = ChatDay
        fields = '__all__'


# 4. Điểm độ sâu
class DDSSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiemDoSau
        fields = '__all__'


# 5. Đường bình độ sâu
class DBDSSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongBinhDoSau
        fields = '__all__'


# 6. Địa hình đặc biệt đáy biển
class DHDBDBSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiaHinhDacBietDayBien
        fields = '__all__'


# 7. Địa mạo
class DMSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiaMao
        fields = '__all__'


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = MoHinhSoDoCaoGocLopDiem
        fields = '__all__'


# 9. Mô hình số độ cao gốc lớp đường
class DEMGLLSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = MoHinhSoDoCaoGocLopDuong
        fields = '__all__'


# 10. Mô hình số độ cao gốc lớp vùng
class DEMGLASerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = MoHinhSoDoCaoGocLopVung
        fields = '__all__'


# 11. Mô hình số độ cao gốc lớp vùng biển tập
class DEMDLVBTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = MoHinhSoDoCaoGocLopVungBienTap
        fields = '__all__'


# 12. Lớp lưới tam giác bất quy tắc (TIN)
class LTGBQTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = LopLuoiTamGiacBatQuyTac
        fields = '__all__'


# 13. Lớp Raster
class RSTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = LopRaster
        fields = '__all__'


# 14. Hố khoan địa chất
class HKDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = HoKhoanDiaChat
        fields = '__all__'


# 15. Số liệu hố khoan địa chất
class SLHKDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = SoLieuHKDC
        fields = '__all__'


# 16. Mặt cắt điển hình địa chất
class MCDHSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = MatCatDienHinh
        fields = '__all__'


# 17. Loại Địa chất
class LDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = LoaiDiaChat
        fields = '__all__'