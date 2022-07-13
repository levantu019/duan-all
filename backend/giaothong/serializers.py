from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import (
    DuongBo,
    CongGiaoThong,
    DuongBang,
    BaiDapTrucThang,
    BaoHieuHangHaiAIS,
    BenCang,
    CauTau,
    BaoHieuDanLuongHangHaiDuongThuy,
    CacDoiTuongHangHaiHaiVan,
    NhomAuTau
)


# 1. Đường bộ
class DBSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongBo
        fields = '__all__'


# 2. Cống giao thông
class CGTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongGiaoThong
        fields = '__all__'


# 3. Đường băng
class DBANGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongBang
        fields = '__all__'


# 4. Bãi đáp trực thăng
class BDTTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BaiDapTrucThang
        fields = '__all__'


# 5. Báo hiệu hàng hải AIS
class BHHHAISSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BaoHieuHangHaiAIS
        fields = '__all__'


# 6. Bến cảng
class BCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BenCang
        fields = '__all__'


# 7. Cầu tàu
class CTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CauTau
        fields = '__all__'


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BHDLHHDTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = BaoHieuDanLuongHangHaiDuongThuy
        fields = '__all__'


# 9. Các đối tượng hàng hải hải văn
class CDTHHHVSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CacDoiTuongHangHaiHaiVan
        fields = '__all__'


# 10. Nhóm Âu tàu
class NATSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = NhomAuTau
        fields = '__all__'