from . import models

# 1. Cây độc lập
class CayDocLapMeta:
    model = models.CayDocLap
    fields = '__all__'
    geo_field = 'GM_Point'

    
# 2. Ranh giới phủ bề mặt
class RGPBMMeta:
    model = models.RanhGioiPhuBeMat
    fields = '__all__'
    geo_field = 'GM_Curve'


# 3. Bề mặt công trình
class BMCTMeta:
    model = models.BeMatCongTrinh
    fields = '__all__'
    geo_field = 'GM_Surface'


# 4. Bề mặt khu dân cư
class BMKDCMeta:
    model = models.BeMatKhuDanCu
    fields = '__all__'
    geo_field = 'GM_Surface'


# 5. Đất trống
class DatTrongMeta:
    model = models.DatTrong
    fields = '__all__'
    geo_field = 'GM_Surface'


# 6. Nước mặt 
class NuocMatMeta:
    model = models.NuocMat
    fields = '__all__'
    geo_field = 'GM_Surface'


# 7. Thực vật đáy biển
class TVDBMeta:
    model = models.ThucVatDayBien
    fields = '__all__'
    geo_field = 'GM_Surface'
