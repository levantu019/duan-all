from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1. Cây độc lập
class CayDocLapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CayDocLap.objects.all()
    serializer_class = serializers.CayDocLapSerializer


# 2. Ranh giới phủ bề mặt
class RGPBMViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RanhGioiPhuBeMat.objects.all()
    serializer_class = serializers.RGPBMSerializer


# 3. Bề mặt công trình
class BMCTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BeMatCongTrinh.objects.all()
    serializer_class = serializers.BMCTSerializer


# 4. Bề mặt khu dân cư
class BMKDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BeMatKhuDanCu.objects.all()
    serializer_class = serializers.BMKDCSerializer


# 5. Đất trống
class DatTrongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DatTrong.objects.all()
    serializer_class = serializers.DatTrongSerializer


# 6. Nước mặt 
class NuocMatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.NuocMat.objects.all()
    serializer_class = serializers.NuocMatSerializer


# 7. Thực vật đáy biển
class TVDBViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ThucVatDayBien.objects.all()
    serializer_class = serializers.TVDBSerializer
