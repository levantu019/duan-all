from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from nendialy.utils import JSONChoices

from .models import(
    NVDH,
    DiemNVDH,
    TuyenNVDH,
    VungNVDH,
    DonVi,
    NVBP,
    PhuongAnViTri,
    PhuongAnTuyen,
    PhuongAnVung,
    PheDuyetPhuongAnViTri,
    PheDuyetPhuongAnTuyen,
    PheDuyetPhuongAnVung,
    PheDuyetChungNVBP,
    GanLucLuong,
    PheDuyetPhuongAnGanLucLuong
)
from .serializers import(
    NVDHSerialiser,
    DiemNVDHSerialiser,
    TuyenNVDHSerialiser,
    VungNVDHSerialiser,
    DonViSerialiser,
    NVBPSerialiser,
    PAViTriSerialiser,
    PDPAViTriSerialiser,
    PATuyenSerialiser,
    PDPATuyenSerialiser,
    PAVungSerialiser,
    PDPAVungSerialiser,
    PDChungNVBPSerialiser,
    GanLLSerialiser,
    PDPAGanLLSerialiser
)


# 1. Nhiệm vụ điều hành
class NVDHViewSet(viewsets.ModelViewSet):
    queryset = NVDH.objects.all()
    serializer_class = NVDHSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-nvdh')
    def choices_maDoiTuong(self, request):
        try:
            choices = NVDH.kieuNVDH.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 2. Điểm NVDH
class DiemNVDHViewSet(viewsets.ModelViewSet):
    queryset = DiemNVDH.objects.all()
    serializer_class = DiemNVDHSerialiser

    
# 3. Tuyến NVDH
class TuyenNVDHViewSet(viewsets.ModelViewSet):
    queryset = TuyenNVDH.objects.all()
    serializer_class = TuyenNVDHSerialiser

    
# 4. Vùng NVDH
class VungNVDHViewSet(viewsets.ModelViewSet):
    queryset = VungNVDH.objects.all()
    serializer_class = VungNVDHSerialiser

    
# 5. Đơn vị
class DonViViewSet(viewsets.ModelViewSet):
    queryset = DonVi.objects.all()
    serializer_class = DonViSerialiser

    
# 6. Nhiệm vụ bộ phận
class NVBPViewSet(viewsets.ModelViewSet):
    queryset = NVBP.objects.all()
    serializer_class = NVBPSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-nvbp')
    def choices_maDoiTuong(self, request):
        try:
            choices = NVBP.trangThaiNVBP.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 7. Phương án vị trí
class PAViTriViewSet(viewsets.ModelViewSet):
    queryset = PhuongAnViTri.objects.all()
    serializer_class = PAViTriSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-pavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnViTri.kieuPAVT.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnViTri.trangthaiPAVT.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 8. Phê duyệt phương án vị trí
class PDPAViTriViewSet(viewsets.ModelViewSet):
    queryset = PheDuyetPhuongAnViTri.objects.all()
    serializer_class = PDPAViTriSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-cmpavt')
    def choices_maDoiTuong(self, request):
        try:
            choices = PheDuyetPhuongAnViTri.trangThaiCMPAVT.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 9. Phương án tuyến
class PATuyenViewSet(viewsets.ModelViewSet):
    queryset = PhuongAnTuyen.objects.all()
    serializer_class = PATuyenSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-pat')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnTuyen.kieuPATuyen.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pat')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnTuyen.trangThaiPATuyen.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 10. Phê duyệt phương án tuyến
class PDPATuyenViewSet(viewsets.ModelViewSet):
    queryset = PheDuyetPhuongAnTuyen.objects.all()
    serializer_class = PDPATuyenSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-cmpat')
    def choices_maDoiTuong(self, request):
        try:
            choices = PheDuyetPhuongAnTuyen.trangThaiCMPATuyen.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 11. Phương án vùng
class PAVungViewSet(viewsets.ModelViewSet):
    queryset = PhuongAnVung.objects.all()
    serializer_class = PAVungSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-pav')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnVung.kieuPAVung.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='trangthai-pav')
    def choices_maDoiTuong(self, request):
        try:
            choices = PhuongAnVung.trangThaiPAVung.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 12. Phê duyệt phương án vùng
class PDPAVungViewSet(viewsets.ModelViewSet):
    queryset = PheDuyetPhuongAnVung.objects.all()
    serializer_class = PDPAVungSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-cmpav')
    def choices_maDoiTuong(self, request):
        try:
            choices = PheDuyetPhuongAnVung.trangThaiCMPAVung.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 13. Phê duyệt chung
class PDChungNVBPViewSet(viewsets.ModelViewSet):
    queryset = PheDuyetChungNVBP.objects.all()
    serializer_class = PDChungNVBPSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-cmnvbp')
    def choices_maDoiTuong(self, request):
        try:
            choices = PheDuyetChungNVBP.trangThaiCMNVBP.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
# 14. Gán lực lượng
class GanLLViewSet(viewsets.ModelViewSet):
    queryset = GanLucLuong.objects.all()
    serializer_class = GanLLSerialiser

    
# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLViewSet(viewsets.ModelViewSet):
    queryset = PheDuyetPhuongAnGanLucLuong.objects.all()
    serializer_class = PDPAGanLLSerialiser

    @action(methods=['get'], detail=False, url_path='trangthai-cmgll')
    def choices_maDoiTuong(self, request):
        try:
            choices = PheDuyetPhuongAnGanLucLuong.trangThaiCMGanLL.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
