from . import models

# 1. Biển đảo
class Surface_BienDaoMeta:
    model = models.BienDao
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_BienDaoMeta:
    model = models.BienDao
    fields = '__all__'
    geo_field = 'GM_Point'

    
# 2. Đảo
class Surface_DaoMeta:
    model = models.Dao
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_DaoMeta:
    model = models.Dao
    fields = '__all__'
    geo_field = 'GM_Point'


# 3. Bãi bồi
class Surface_BaiBoiMeta:
    model = models.BaiBoi
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_BaiBoiMeta:
    model = models.BaiBoi
    fields = '__all__'
    geo_field = 'GM_Point'


# 4. Bãi đá dưới nước
class Surface_BDDNMeta:
    model = models.BaiDaDuoiNuoc
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_BDDNMeta:
    model = models.BaiDaDuoiNuoc
    fields = '__all__'
    geo_field = 'GM_Point'


# 5. Nguồn nước
class Surface_NguonNuocMeta:
    model = models.NguonNuoc
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_NguonNuocMeta:
    model = models.NguonNuoc
    fields = '__all__'
    geo_field = 'GM_Point'


# 6. Điểm độ cao mực nước
class DDCMNMeta:
    model = models.DiemDoCaoMucNuoc
    fields = '__all__'
    geo_field = 'GM_Point'


# 7. Đường bờ nước
class DBNMeta:
    model = models.DuongBoNuoc
    fields = '__all__'
    geo_field = 'GM_Curve'


# 8. Đường mép nước
class DMNMeta:
    model = models.DuongMepNuoc
    fields = '__all__'
    geo_field = 'GM_Curve'


# 9. Ranh giới nước mặt quy ước
class RGNMQUMeta:
    model = models.RanhGioiNuocMatQuyUoc
    fields = '__all__'
    geo_field = 'GM_Curve'


# 10. Bờ kè bờ cạp
class BKBCMeta:
    model = models.BoKeBoCap
    fields = '__all__'
    geo_field = 'GM_Curve'


# 11. Kênh mương
class Surface_KenhMuongMeta:
    model = models.KenhMuong
    fields = '__all__'
    geo_field = 'GM_Surface'
class Curve_KenhMuongMeta:
    model = models.KenhMuong
    fields = '__all__'
    geo_field = 'GM_Curve'


# 12. Trạm thu thập TTTV
class TTTTTTVMeta:
    model = models.TramThuThapKTTV
    fields = '__all__'
    geo_field = 'GM_Point'


# 13. Tham số KTTV
class TSKTTVMeta:
    model = models.ThamSoKTTV
    fields = '__all__'


# 14. Số liệu sóng, gió, dòng chảy
class SGDCMeta:
    model = models.SongGioDongChay
    fields = '__all__'


# 15. Tham số nước
class TSNMeta:
    model = models.ThamSoNuoc
    fields = '__all__'

