from . import models

# 1. Đường bộ
class DuongBoMeta:
    class Meta:
        model = models.DuongBo
        fields = '__all__'
        geo_field = 'GM_Curve'


# 2. Cống giao thông
class Curve_CongGTMeta:
    class Meta:
        model = models.Curve_CongGiaoThong
        fields = '__all__'
        geo_field = 'GM_Curve'

class Point_CongGTMeta:
    class Meta:
        model = models.Point_CongGiaoThong
        fields = '__all__'
        geo_field = 'GM_Point'


# 3. Đường băng
class DBANGMeta:
    class Meta:
        model = models.DuongBang
        fields = '__all__'
        geo_field = 'GM_Surface'


# 4. Bãi đáp trực thăng
class BDTTMeta:
    class Meta:
        model = models.BaiDapTrucThang
        fields = '__all__'
        geo_field = 'GM_Surface'


# 5. Báo hiệu hàng hải AIS
class BHHHAISMeta:
    class Meta:
        model = models.BaoHieuHangHaiAIS
        fields = '__all__'
        geo_field = 'GM_Point'


# 6. Bến cảng
class BenCangMeta:
    class Meta:
        model = models.BenCang
        fields = '__all__'
        geo_field = 'GM_Surface'


# 7. Cầu tàu
class Surface_CauTauMeta:
    class Meta:
        model = models.Surface_CauTau
        fields = '__all__'
        geo_field = 'GM_Surface'

class Curve_CauTauMeta:
    class Meta:
        model = models.Curve_CauTau
        fields = '__all__'
        geo_field = 'GM_Curve'


# 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BHDLHHDTMeta:
    class Meta:
        model = models.BaoHieuDanLuongHangHaiDuongThuy
        fields = '__all__'
        geo_field = 'GM_Point'


# 9. Các đối tượng hàng hải hải văn
class Surface_CDTHHHVMeta:
    class Meta:
        model = models.Surface_CacDoiTuongHangHaiHaiVan
        fields = '__all__'
        geo_field = 'GM_Surface'

class Point_CDTHHHVMeta:
    class Meta:
        model = models.Point_CacDoiTuongHangHaiHaiVan
        fields = '__all__'
        geo_field = 'GM_Point'


# 10. Nhóm Âu tàu
class Surface_NhomAuTauMeta:
    class Meta:
        model = models.Surface_NhomAuTau
        fields = '__all__'
        geo_field = 'GM_Surface'

class Curve_NhomAuTauMeta:
    class Meta:
        model = models.Curve_NhomAuTau
        fields = '__all__'
        geo_field = 'GM_Curve'
