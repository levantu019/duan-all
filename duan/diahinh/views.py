from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

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
from .serializers import (
    DDCSerializer,
    DBDSerializer,
    CHATDAYSerializer,
    DDSSerializer,
    DBDSSerializer,
    DHDBDBSerializer,
    DMSerializer,
    DEMGLPSerializer,
    DEMGLLSerializer,
    DEMGLASerializer,
    DEMDLVBTSerializer,
    LTGBQTSerializer,
    RSTSerializer,
    HKDCSerializer,
    SLHKDCSerializer,
    MCDHSerializer,
    LDCSerializer
)
from nendialy.decorators import http_methods_disable


# 1. Điểm độ cao
@http_methods_disable('post', 'put', 'patch', 'delete')
class DDCViewSet(viewsets.ModelViewSet):
    queryset = DiemDoCao.objects.all()
    serializer_class = DDCSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiemDoCao.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Đường bình độ
@http_methods_disable('post', 'put', 'patch', 'delete')
class DBDViewSet(viewsets.ModelViewSet):
    queryset = DuongBinhDo.objects.all()
    serializer_class = DBDSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongBinhDo.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaidbd')
    def choices_loaiDuongBinhDo(self, request):
        try:
            choices = DuongBinhDo.loaiDuongBinhDo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaikcd')
    def choices_loaiKhoangCaoDeu(self, request):
        try:
            choices = DuongBinhDo.loaiKhoangCaoDeu.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Chất đáy
@http_methods_disable('post', 'put', 'patch', 'delete')
class CDViewSet(viewsets.ModelViewSet):
    queryset = ChatDay.objects.all()
    serializer_class = CHATDAYSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = ChatDay.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaichatday')
    def choices_loaiChatDay(self, request):
        try:
            choices = ChatDay.loaiChatDay.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 4. Điểm độ sâu
@http_methods_disable('post', 'put', 'patch', 'delete')
class DDSViewSet(viewsets.ModelViewSet):
    queryset = DiemDoSau.objects.all()
    serializer_class = DDSSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiemDoSau.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 5. Đường bình độ sâu
@http_methods_disable('post', 'put', 'patch', 'delete')
class DBDSViewSet(viewsets.ModelViewSet):
    queryset = DuongBinhDoSau.objects.all()
    serializer_class = DBDSSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DuongBinhDoSau.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaidbd')
    def choices_loaiDuongBinhDo(self, request):
        try:
            choices = DuongBinhDoSau.loaiDuongBinhDo.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='loaikcd')
    def choices_loaiKhoangCaoDeu(self, request):
        try:
            choices = DuongBinhDoSau.loaiKhoangCaoDeu.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 6. Địa hình đặc biệt đáy biển
@http_methods_disable('post', 'put', 'patch', 'delete')
class DHDBDBViewSet(viewsets.ModelViewSet):
    queryset = DiaHinhDacBietDayBien.objects.all()
    serializer_class = DHDBDBSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DiaHinhDacBietDayBien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 7. Địa mạo
@http_methods_disable('post', 'put', 'patch', 'delete')
class DMViewSet(viewsets.ModelViewSet):
    queryset = DiaMao.objects.all()
    serializer_class = DMSerializer


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPViewSet(viewsets.ModelViewSet):
    queryset = MoHinhSoDoCaoGocLopDiem.objects.all()
    serializer_class = DEMGLPSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = MoHinhSoDoCaoGocLopDiem.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 9. Mô hình số độ cao gốc lớp đường
@http_methods_disable('post', 'put', 'patch', 'delete')
class DEMGLLViewSet(viewsets.ModelViewSet):
    queryset = MoHinhSoDoCaoGocLopDuong.objects.all()
    serializer_class = DEMGLLSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = MoHinhSoDoCaoGocLopDuong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 10. Mô hình số độ cao gốc lớp vùng
@http_methods_disable('post', 'put', 'patch', 'delete')
class DEMGLAViewSet(viewsets.ModelViewSet):
    queryset = MoHinhSoDoCaoGocLopVung.objects.all()
    serializer_class = DEMGLASerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = MoHinhSoDoCaoGocLopVung.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 11. Mô hình số độ cao gốc lớp vùng biển tập
@http_methods_disable('post', 'put', 'patch', 'delete')
class DEMDLVBTViewSet(viewsets.ModelViewSet):
    queryset = MoHinhSoDoCaoGocLopVungBienTap.objects.all()
    serializer_class = DEMDLVBTSerializer

    @action(methods=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = MoHinhSoDoCaoGocLopVungBienTap.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 12. Lớp lưới tam giác bất quy tắc (TIN)
@http_methods_disable('post', 'put', 'patch', 'delete')
class LTGBQTViewSet(viewsets.ModelViewSet):
    queryset = LopLuoiTamGiacBatQuyTac.objects.all()
    serializer_class = LTGBQTSerializer


# 13. Lớp Raster
@http_methods_disable('post', 'put', 'patch', 'delete')
class RSTViewSet(viewsets.ModelViewSet):
    queryset = LopRaster.objects.all()
    serializer_class = RSTSerializer


# 14. Hố khoan địa chất
@http_methods_disable('post', 'put', 'patch', 'delete')
class HKDCViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = HoKhoanDiaChat.objects.all()
    serializer_class = HKDCSerializer
    parser_classes = [MultiPartParser, ]


# 15. Số liệu hố khoan địa chất
@http_methods_disable('post', 'put', 'patch', 'delete')
class SLHKDCViewSet(viewsets.ModelViewSet):
    queryset = SoLieuHKDC.objects.all()
    serializer_class = SLHKDCSerializer


# 16. Mặt cắt điển hình địa chất
@http_methods_disable('post', 'put', 'patch', 'delete')
class MCDHViewSet(viewsets.ModelViewSet):
    queryset = MatCatDienHinh.objects.all()
    serializer_class = MCDHSerializer


# 17. Loại Địa chất
@http_methods_disable('post', 'put', 'patch', 'delete')
class LDCSerializer(viewsets.ModelViewSet):
    queryset = LoaiDiaChat.objects.all()
    serializer_class = LDCSerializer


