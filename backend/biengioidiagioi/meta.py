from . import models

# 1. Vùng biển
class VBMeta:
    model = models.VungBien
    fields = '__all__'
    geo_field = 'GM_Surface'

# 2. Địa phận hành chính trên biển
class DPHCTBMeta:
    model = models.DiaPhanHanhChinhTrenBien
    fields = '__all__'
    geo_field = 'GM_Surface'

# 3. Đường ranh giới hành chính trên biển
class DRGHCTBMeta:
    model = models.DuongRanhGioiHanhChinhTrenBien
    fields = '__all__'        
    geo_field = 'GM_Curve'

# 4. Đường ranh giới hành chính trên đất liền
class DPHCTDLMeta:
    model = models.DiaPhanHanhChinhTrenDatLien
    fields = '__all__'
    geo_field = 'GM_Surface'