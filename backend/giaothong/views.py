from rest_framework import viewsets, generics, status

from .import models, serializers


# 1. Đường bộ
class DuongBoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongBo.objects.all()
    serializer_class = serializers.DBSerializer


# 2. Cống giao thông
class Curve_CGTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_CongGiaoThong.objects.all()
    serializer_class = serializers.Curve_CGTSerializer

class Point_CGTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CongGiaoThong.objects.all()
    serializer_class = serializers.Point_CGTSerializer


# 3. Đường băng
class DBANGViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongBang.objects.all()
    serializer_class = serializers.DBANGSerializer


# 4. Bãi đáp trực thăng
class BDTTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaiDapTrucThang.objects.all()
    serializer_class = serializers.BDTTSerializer


# 5. Báo hiệu hàng hải AIS
class BHHHAISViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaoHieuHangHaiAIS.objects.all()
    serializer_class = serializers.BHHHAISSerializer


# 6. Bến cảng
class BenCangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BenCang.objects.all()
    serializer_class = serializers.BenCangSerializer


# 7. Cầu tàu
class Surface_CTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CauTau.objects.all()
    serializer_class = serializers.Surface_CauTauSerializer

class Curve_CTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_CauTau.objects.all()
    serializer_class = serializers.Curve_CauTauSerializer


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BHDLHHDTViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaoHieuDanLuongHangHaiDuongThuy.objects.all()
    serializer_class = serializers.BHDLHHDTSerializer


# 9. Các đối tượng hàng hải hải văn
class Surface_CDTHHHVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_CacDoiTuongHangHaiHaiVan.objects.all()
    serializer_class = serializers.Surface_CDTHHHVSerializer

class Point_CDTHHHVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Point_CacDoiTuongHangHaiHaiVan.objects.all()
    serializer_class = serializers.Point_CDTHHHVSerializer


# 10. Nhóm Âu tàu
class Surface_NATViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Surface_NhomAuTau.objects.all()
    serializer_class = serializers.Surface_NATSerializer

class Curve_NATViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curve_NhomAuTau.objects.all()
    serializer_class = serializers.Curve_NATSerializer
