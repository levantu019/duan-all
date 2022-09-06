from . import models

# 1. Cây độc lập
class CayDocLapMeta:
    class Meta:
        model = models.CayDocLap
        fields = '__all__'
        geo_field = 'GM_Point'

    
# 2. Ranh giới phủ bề mặt
class RGPBMMeta:
    class Meta:
        model = models.RanhGioiPhuBeMat
        fields = '__all__'
        geo_field = 'GM_Curve'


# 3. Bề mặt công trình
class BMCTMeta:
    class Meta:
        model = models.BeMatCongTrinh
        fields = '__all__'
        geo_field = 'GM_Surface'


# 4. Bề mặt khu dân cư
class BMKDCMeta:
    class Meta:
        model = models.BeMatKhuDanCu
        fields = '__all__'
        geo_field = 'GM_Surface'


# 5. Đất trống
class DatTrongMeta:
    class Meta:
        model = models.DatTrong
        fields = '__all__'
        geo_field = 'GM_Surface'


# 6. Nước mặt 
class NuocMatMeta:
    class Meta:
        model = models.NuocMat
        fields = '__all__'
        geo_field = 'GM_Surface'


# 7. Thực vật đáy biển
class TVDBMeta:
    class Meta:
        model = models.ThucVatDayBien
        fields = '__all__'
        geo_field = 'GM_Surface'
