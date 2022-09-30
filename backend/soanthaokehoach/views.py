from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from jwtauth.permissions import (
    IsSuperUser,
    IsAdminData,
    IsUserLevel1,
    IsUserLevel2,
    IsuserLevel3
)

from .utils import jsonData
from . import models, serializers


# 1. Nhiệm vụ điều hành
class NVDHViewSet(viewsets.ModelViewSet):
    queryset = models.NVDH.objects.all()
    serializer_class = serializers.NVDHSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='kieu-nvdh')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.NVDH.kieuNVDH.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 2. Điểm NVDH
class DiemNVDHViewSet(viewsets.ModelViewSet):
    queryset = models.DiemNVDH.objects.all()
    serializer_class = serializers.DiemNVDHSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    
# 3. Tuyến NVDH
class TuyenNVDHViewSet(viewsets.ModelViewSet):
    queryset = models.TuyenNVDH.objects.all()
    serializer_class = serializers.TuyenNVDHSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    
# 4. Vùng NVDH
class VungNVDHViewSet(viewsets.ModelViewSet):
    queryset = models.VungNVDH.objects.all()
    serializer_class = serializers.VungNVDHSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    
# # 5. Đơn vị
# class DonViViewSet(viewsets.ModelViewSet):
#     queryset = models.DonVi.objects.all()
#     serializer_class = serializers.DonViSerializer

    
# 6. Nhiệm vụ bộ phận
class NVBPViewSet(viewsets.ModelViewSet):
    queryset = models.NVBP.objects.all()
    serializer_class = serializers.NVBPSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trang-thai-nvbp')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.NVBP.trangThaiNVBP.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 7. Phương án vị trí
class PAViTriViewSet(viewsets.ModelViewSet):
    queryset = models.PhuongAnViTri.objects.all()
    serializer_class = serializers.PAViTriSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='kieu-pavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnViTri.kieuPAVT.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnViTri.trangthaiPAVT.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 8. Phê duyệt phương án vị trí
class PDPAViTriViewSet(viewsets.ModelViewSet):
    queryset = models.PheDuyetPhuongAnViTri.objects.all()
    serializer_class = serializers.PDPAViTriSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trangthai-cmpavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PheDuyetPhuongAnViTri.trangThaiCMPAVT.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 9. Phương án tuyến
class PATuyenViewSet(viewsets.ModelViewSet):
    queryset = models.PhuongAnTuyen.objects.all()
    serializer_class = serializers.PATuyenSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='kieu-pat')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnTuyen.kieuPATuyen.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pat')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnTuyen.trangThaiPATuyen.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 10. Phê duyệt phương án tuyến
class PDPATuyenViewSet(viewsets.ModelViewSet):
    queryset = models.PheDuyetPhuongAnTuyen.objects.all()
    serializer_class = serializers.PDPATuyenSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trangthai-cmpat')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PheDuyetPhuongAnTuyen.trangThaiCMPATuyen.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 11. Phương án vùng
class PAVungViewSet(viewsets.ModelViewSet):
    queryset = models.PhuongAnVung.objects.all()
    serializer_class = serializers.PAVungSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='kieu-pav')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnVung.kieuPAVung.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pav')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PhuongAnVung.trangThaiPAVung.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 12. Phê duyệt phương án vùng
class PDPAVungViewSet(viewsets.ModelViewSet):
    queryset = models.PheDuyetPhuongAnVung.objects.all()
    serializer_class = serializers.PDPAVungSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trangthai-cmpav')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PheDuyetPhuongAnVung.trangThaiCMPAVung.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 13. Phê duyệt chung
class PDChungNVBPViewSet(viewsets.ModelViewSet):
    queryset = models.PheDuyetChungNVBP.objects.all()
    serializer_class = serializers.PDChungNVBPSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trangthai-cmnvbp')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PheDuyetChungNVBP.trangThaiCMNVBP.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 14. Gán lực lượng
class GanLLViewSet(viewsets.ModelViewSet):
    queryset = models.GanLucLuong.objects.all()
    serializer_class = serializers.GanLLSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    
# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLViewSet(viewsets.ModelViewSet):
    queryset = models.PheDuyetPhuongAnGanLucLuong.objects.all()
    serializer_class = serializers.PDPAGanLLSerializer
    permission_classes = [IsSuperUser|IsUserLevel1|IsUserLevel2]

    @action(methods=['get'], detail=False, url_path='trangthai-cmgll')
    def choices_maDoiTuong(self, request):
        try:
            choices = models.PheDuyetPhuongAnGanLucLuong.trangThaiCMGanLL.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
