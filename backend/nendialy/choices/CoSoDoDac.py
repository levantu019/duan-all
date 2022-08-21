# ---------------------------------------------------------
# -------------------- 2. Cơ sở đo đạc --------------------
# ---------------------------------------------------------
### Bảng Điểm gốc đo đạc quốc gia
# Đối tượng Điểm gốc đo đạc quốc gia
DGDDQG_DOCAO = 'BA01'
DGDDQG_TOADO = 'BA02'
DGDDQG_TRONGLUC = 'BA03'
DGDDQG_CHOICES = [
    (DGDDQG_DOCAO, 'Điểm gốc độ cao quốc gia'),
    (DGDDQG_TOADO, 'Điểm gốc toạ độ quốc gia'),
    (DGDDQG_TRONGLUC, 'Điểm gốc trọng lực quốc gia'),
]

### Bảng Điểm đo đạc quốc gia
# Đối tượng Điểm đo đạc quốc gia
DDDQG_DOCAO = 'BC01'
DDDQG_TOADO = 'BC02'
DDDQG_TOADO_DOCAO = 'BC03'
DDDQG_TRONGLUC = 'BC04'
DDDQG_CHOICES = [
    (DDDQG_DOCAO, 'Điểm độ cao quốc gia'),
    (DDDQG_TOADO, 'Điểm tọa độ quốc gia'),
    (DDDQG_TOADO_DOCAO, 'Điểm tọa độ và độ cao quốc gia'),
    (DDDQG_TRONGLUC, 'Điểm trọng lực quốc gia'),
]

# Loại mốc
DDDQG_LOAIMOC_CHON = 1
DDDQG_LOAIMOC_GAN = 2
DDDQG_LOAIMOC_KHAC = 3
DDDQG_LOAIMOC_CHOICES = [
    (DDDQG_LOAIMOC_CHON, 'Chôn'),
    (DDDQG_LOAIMOC_GAN, 'Gắn'),
    (DDDQG_LOAIMOC_KHAC, 'Khác'),
]

# Loại cấp hạng
DDDQG_LOAICAPHANG_COSO = 1
DDDQG_LOAICAPHANG_0 = 2
DDDQG_LOAICAPHANG_I = 3
DDDQG_LOAICAPHANG_II = 4
DDDQG_LOAICAPHANG_III = 5
DDDQG_LOAICAPHANG_CHOICES = [
    (DDDQG_LOAICAPHANG_COSO, 'Cấp cơ sở'),
    (DDDQG_LOAICAPHANG_0, 'Cấp 0'),
    (DDDQG_LOAICAPHANG_I, 'Hạng I'),
    (DDDQG_LOAICAPHANG_II, 'Hạng II'),
    (DDDQG_LOAICAPHANG_III, 'Hạng III'),
]

### Bảng Trạm định vị vệ tinh quốc gia
# Đối tượng Trạm định vị vệ tinh quốc gia
TDVVTQG_ = 'BD02'
TDVVTQG_CHOICES = [
    (TDVVTQG_, TDVVTQG_),
]

# Loại trạm định vị vệ tinh
TDVVTQG_LOAI_TTCCSHDLT = 1
TDVVTQG_LOAI_TTCHDLT = 2
TDVVTQG_LOAI_CHOICES = [
    (TDVVTQG_LOAI_TTCCSHDLT, 'Trạm tham chiếu cơ sở hoạt động liên tục'),
    (TDVVTQG_LOAI_TTCHDLT, 'Trạm tham chiếu hoạt động liên tục'),
]


#                                         ####### GIÁ TRỊ MẶC ĐỊNH ######
# ### Bảng Điểm gốc đo đạc quốc gia
# # Đối tượng Điểm gốc đo đạc quốc gia
# DGDDQG_DEFAULT = DGDDQG_DOCAO

# ### Bảng Điểm đo đạc quốc gia
# # Đối tượng Điểm đo đạc quốc gia
# DDDQG_DEFAULT = DDDQG_DOCAO

# # Loại mốc
# DDDQG_LOAIMOC_DEFAULT = DDDQG_LOAIMOC_CHON

# # Loại cấp hạng
# DDDQG_LOAICAPHANG_DEFAULT = DDDQG_LOAICAPHANG_COSO

# ### Bảng Trạm định vị vệ tinh quốc gia
# # Đối tượng Trạm định vị vệ tinh quốc gia
# TDVVTQG_DEFAULT = TDVVTQG_

# # Loại trạm định vị vệ tinh
# TDVVTQG_LOAI_DEFAULT = TDVVTQG_LOAI_TTCCSHDLT
