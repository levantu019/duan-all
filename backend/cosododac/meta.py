from . import models

# 1. Điểm gốc đo đạc quốc gia
class DGDDQGMeta:
    class Meta:
        model = models.DiemGocDoDacQuocGia
        fields = '__all__'
        geo_field = 'GM_Point'


# 2. Điểm đo đạc quốc gia
class DDDQGMeta:
    class Meta:
        model = models.DiemDoDacQuocGia
        fields = '__all__'
        geo_field = 'GM_Point'


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGMeta:
    class Meta:
        model = models.TramDinhViVeTinhQuocGia
        fields = '__all__'
        geo_field = 'GM_Point'