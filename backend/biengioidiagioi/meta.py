from . import models

# 1. Vùng biển
class VBMeta:
    class Meta:
        model = models.VungBien
        fields = '__all__'
        geo_field = 'GM_Surface'

# 2. Địa phận hành chính trên biển
class DPHCTBMeta:
    class Meta:
        model = models.DiaPhanHanhChinhTrenBien
        fields = '__all__'
        geo_field = 'GM_Surface'

# 3. Đường ranh giới hành chính trên biển
class DRGHCTBMeta:
    class Meta:
        model = models.DuongRanhGioiHanhChinhTrenBien
        fields = '__all__'        
        geo_field = 'GM_Curve'

# 4. Đường ranh giới hành chính trên đất liền
class DPHCTDLMeta:
    class Meta:
        model = models.DiaPhanHanhChinhTrenDatLien
        fields = '__all__'
        geo_field = 'GM_Surface'