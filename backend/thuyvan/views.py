from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1. Biển đảo
class Surface_BienDaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BienDao.objects.all()
    serializer_class = serializers.Surface_BienDaoSerializer


class Point_BienDaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BienDao.objects.all()
    serializer_class = serializers.Point_BienDaoSerializer

    
# 2. Đảo
class Surface_DaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Dao.objects.all()
    serializer_class = serializers.Surface_DaoSerializer

class Point_DaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Dao.objects.all()
    serializer_class = serializers.Point_DaoSerializer


# 3. Bãi bồi
class Surface_BaiBoiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaiBoi.objects.all()
    serializer_class = serializers.Surface_BaiBoiSerializer

class Point_BaiBoiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaiBoi.objects.all()
    serializer_class = serializers.Point_BaiBoiSerializer


# 4. Bãi đá dưới nước
class Surface_BDDNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaiDaDuoiNuoc.objects.all()
    serializer_class = serializers.Surface_BDDNSerializer

class Point_BDDNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BaiDaDuoiNuoc.objects.all()
    serializer_class = serializers.Point_BDDNSerializer


# 5. Nguồn nước
class Surface_NguonNuocViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.NguonNuoc.objects.all()
    serializer_class = serializers.Surface_NguonNuocSerializer

class Point_NguonNuocViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.NguonNuoc.objects.all()
    serializer_class = serializers.Point_NguonNuocSerializer


# 6. Điểm độ cao mực nước
class DDCMNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiemDoCaoMucNuoc.objects.all()
    serializer_class = serializers.DDCMNSerializer


# 7. Đường bờ nước
class DBNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongBoNuoc.objects.all()
    serializer_class = serializers.DBNSerializer


# 8. Đường mép nước
class DMNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuongMepNuoc.objects.all()
    serializer_class = serializers.DMNSerializer


# 9. Ranh giới nước mặt quy ước
class RGNMQUViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RanhGioiNuocMatQuyUoc.objects.all()
    serializer_class = serializers.RGNMQUSerializer


# 10. Bờ kè bờ cạp
class BKBCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BoKeBoCap.objects.all()
    serializer_class = serializers.BKBCSerializer


# 11. Kênh mương
class Surface_KenhMuongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.KenhMuong.objects.all()
    serializer_class = serializers.Surface_KenhMuongSerializer

class Curve_KenhMuongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.KenhMuong.objects.all()
    serializer_class = serializers.Curve_KenhMuongSerializer


# 12. Trạm thu thập TTTV
class TTTTTTVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TramThuThapKTTV.objects.all()
    serializer_class = serializers.TTTTTTVSerializer


# 13. Tham số KTTV
class TSKTTVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ThamSoKTTV.objects.all()
    serializer_class = serializers.TSKTTVSerializer


# 14. Số liệu sóng, gió, dòng chảy
class SGDCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SongGioDongChay.objects.all()
    serializer_class = serializers.SGDCSerializer


# 15. Tham số nước
class TSNViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ThamSoNuoc.objects.all()
    serializer_class = serializers.TSNSerializer

