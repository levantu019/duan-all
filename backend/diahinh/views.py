from rest_framework import viewsets, generics, status
from rest_framework.parsers import MultiPartParser

from .import models, serializers


# 1. Điểm độ cao
class DDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiemDoCao.objects.all()
    serializer_class = serializers.DDCSerializer


# 2. Đường bình độ
class DBDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongBinhDo.objects.all()
    serializer_class = serializers.DBDSerializer


# 3. Chất đáy
class ChatDayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ChatDay.objects.all()
    serializer_class = serializers.ChatDaySerializer


# 4. Điểm độ sâu
class DDSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiemDoSau.objects.all()
    serializer_class = serializers.DDSSerializer


# 5. Đường bình độ sâu
class DBDSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongBinhDoSau.objects.all()
    serializer_class = serializers.DBDSSerializer


# 6. Địa hình đặc biệt đáy biển
class Surface_DHDBDBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_DiaHinhDacBietDayBien.objects.all()
    serializer_class = serializers.Surface_DHDBDBSerializer

class Curve_DHDBDBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_DiaHinhDacBietDayBien.objects.all()
    serializer_class = serializers.Curve_DHDBDBSerializer


# 7. Địa mạo
class DiaMaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiaMao.objects.all()
    serializer_class = serializers.DiaMaoSerializer


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MoHinhSoDoCaoGocLopDiem.objects.all()
    serializer_class = serializers.DEMGLPSerializer


# 9. Mô hình số độ cao gốc lớp đường
class DEMGLLViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MoHinhSoDoCaoGocLopDuong.objects.all()
    serializer_class = serializers.DEMGLLSerializer


# 10. Mô hình số độ cao gốc lớp vùng
class DEMGLAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MoHinhSoDoCaoGocLopVung.objects.all()
    serializer_class = serializers.DEMGLASerializer


# 11. Mô hình số độ cao gốc lớp vùng biển tập
class DEMDLVBTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MoHinhSoDoCaoGocLopVungBienTap.objects.all()
    serializer_class = serializers.DEMDLVBTSerializer


# # 12. Lớp lưới tam giác bất quy tắc (TIN)
# class LTGBQTViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = LopLuoiTamGiacBatQuyTac.objects.all()
#     serializer_class = LTGBQTSerializer


# # 13. Lớp Raster
# class RSTViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = LopRaster.objects.all()
#     serializer_class = RSTSerializer


# 14. Hố khoan địa chất
# class HKDCViewSet(viewsets.ViewSet, generics.CreateAPIView):
class HKDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HoKhoanDiaChat.objects.all()
    serializer_class = serializers.HKDCSerializer
    # parser_classes = [MultiPartParser, ]


# 15. Số liệu hố khoan địa chất
class SLHKDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SoLieuHKDC.objects.all()
    serializer_class = serializers.SLHKDCSerializer


# 16. Mặt cắt điển hình địa chất
class MCDHViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MatCatDienHinh.objects.all()
    serializer_class = serializers.MCDHSerializer


# 17. Loại Địa chất
class LDCSerializer(viewsets.ReadOnlyModelViewSet):
    queryset = models.LoaiDiaChat.objects.all()
    serializer_class = serializers.LDCSerializer


