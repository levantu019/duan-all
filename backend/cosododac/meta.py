from . import models

# 1. Điểm gốc đo đạc quốc gia
class DGDDQGMeta:
    model = models.DiemGocDoDacQuocGia
    fields = '__all__'
    geo_field = 'GM_Point'


# 2. Điểm đo đạc quốc gia
class DDDQGMeta:
    model = models.DiemDoDacQuocGia
    fields = '__all__'
    geo_field = 'GM_Point'


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGMeta:
    model = models.TramDinhViVeTinhQuocGia
    fields = '__all__'
    geo_field = 'GM_Point'