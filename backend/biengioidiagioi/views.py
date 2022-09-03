from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1. Vùng biển
class VBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.VungBien.objects.all()
    serializer_class = serializers.VBSerializer


# 2. Địa phận hành chính trên biển
class DPHCTBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiaPhanHanhChinhTrenBien.objects.all()
    serializer_class = serializers.DPHCTBSerializer


# 3. Đường ranh giới hành chính trên biển
class DRGHCTBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongRanhGioiHanhChinhTrenBien.objects.all()
    serializer_class = serializers.DRGHCTBSerializer


# 4. Địa phận hành chính trên đất liền
class DPHCTDLViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiaPhanHanhChinhTrenDatLien.objects.all()
    serializer_class = serializers.DPHCTDLSerializer
