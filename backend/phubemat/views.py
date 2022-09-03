from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1. Cây độc lập
class CayDocLapViewSet(viewsets.ModelViewSet):
    queryset = models.CayDocLap.objects.all()
    serializer_class = serializers.CayDocLapSerializer


# 2. Ranh giới phủ bề mặt
class RGPBMViewSet(viewsets.ModelViewSet):
    queryset = models.RanhGioiPhuBeMat.objects.all()
    serializer_class = serializers.RGPBMSerializer


# 3. Bề mặt công trình
class BMCTViewSet(viewsets.ModelViewSet):
    queryset = models.BeMatCongTrinh.objects.all()
    serializer_class = serializers.BMCTSerializer


# 4. Bề mặt khu dân cư
class BMKDCViewSet(viewsets.ModelViewSet):
    queryset = models.BeMatKhuDanCu.objects.all()
    serializer_class = serializers.BMKDCSerializer


# 5. Đất trống
class DatTrongViewSet(viewsets.ModelViewSet):
    queryset = models.DatTrong.objects.all()
    serializer_class = serializers.DatTrongSerializer


# 6. Nước mặt 
class NuocMatViewSet(viewsets.ModelViewSet):
    queryset = models.NuocMat.objects.all()
    serializer_class = serializers.NuocMatSerializer


# 7. Thực vật đáy biển
class TVDBViewSet(viewsets.ModelViewSet):
    queryset = models.ThucVatDayBien.objects.all()
    serializer_class = serializers.TVDBSerializer
