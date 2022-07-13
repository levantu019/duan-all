from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    BienDao,
    Dao,
    BaiBoi,
    BaiDaDuoiNuoc,
    NguonNuoc,
    DiemDoCaoMucNuoc,
    DuongBoNuoc,
    DuongMepNuoc,
    RanhGioiNuocMatQuyUoc,
    BoKeBoCap,
    KenhMuong,
    TramThuThapKTTV,
    ThamSoKTTV,
    SongGioDongChay,
    ThamSoNuoc
)


# 1. Biển đảo
class BDSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BienDao
        fields = '__all__'

        
# 2. Đảo
class DSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = Dao
        fields = '__all__'


# 3. Bãi bồi
class BBSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BaiBoi
        fields = '__all__'


# 4. Bãi đá dưới nước
class BDDNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BaiDaDuoiNuoc
        fields = '__all__'


# 5. Nguồn nước
class NNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = NguonNuoc
        fields = '__all__'


# 6. Điểm độ cao mực nước
class DDCMNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiemDoCaoMucNuoc
        fields = '__all__'


# 7. Đường bờ nước
class DBNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongBoNuoc
        fields = '__all__'


# 8. Đường mép nước
class DMNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongMepNuoc
        fields = '__all__'


# 9. Ranh giới nước mặt quy ước
class RGNMQUSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = RanhGioiNuocMatQuyUoc
        fields = '__all__'


# 10. Bờ kè bờ cạp
class BKBCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BoKeBoCap
        fields = '__all__'


# 11. Kênh mương
class KMSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = KenhMuong
        fields = '__all__'


# 12. Trạm thu thập TTTV
class TTTTTTVSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TramThuThapKTTV
        fields = '__all__'


# 13. Tham số KTTV
class TSKTTVSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = ThamSoKTTV
        fields = '__all__'


# 14. Số liệu sóng, gió, dòng chảy
class SGDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = SongGioDongChay
        fields = '__all__'


# 15. Tham số nước
class TSNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = ThamSoNuoc
        fields = '__all__'

