# ---------------------------------------------------------
# -------------------- 6. Phủ bề mặt --------------------------
# ---------------------------------------------------------
### Bảng Cây độc lập
# Đối tượng Cây độc lập
CDL_CDL = 'HE03'
CDL_CCDL = 'HE04'
CDL_CHOICES = [
    (CDL_CDL, 'Cây độc lập'),
    (CDL_CCDL, 'Cụm cây độc lập'),
]

### Bảng Ranh giới phủ bề mặt
# Đối tượng Ranh giới phủ bề mặt
RGPBM_ = 'HG01'
RGPBM_CHOICES = [
    (RGPBM_, RGPBM_),
]

# Loại ranh giới phủ bề mặt
RGPBM_LOAI_TV = 1
RGPBM_LOAI_KHAC = 2
RGPBM_LOAI_RGKBTTN = 3
RGPBM_LOAI_CHOICES = [
    (RGPBM_LOAI_TV, 'Thực vật'),
    (RGPBM_LOAI_KHAC, 'Khác'),
    (RGPBM_LOAI_RGKBTTN, 'Ranh giới khu bảo tồn thiên nhiên'),
]

### Bảng Bề mặt công trình
# Đối tượng Bề mặt công trình
BMCT_ = 'HA01'
BMCT_CHOICES = [
    (BMCT_, BMCT_),
]

# Thực vật
BMCT_TV_CO = 1
BMCT_TV_KHONG = 2
BMCT_TV_CHOICES = [
    (BMCT_TV_CO, 'Có thực vật che phủ'),
    (BMCT_TV_KHONG, 'Không có thực vật che phủ'),
]

### Bảng Bề mặt khu dân cư
# Đối tượng Bề mặt khu dân cư
BMKDC_ = 'HA02'
BMKDC_CHOICES = [
    (BMKDC_, BMKDC_),
]

# Thực vật
BMKDC_TV_CO = 1
BMKDC_TV_KHONG = 2
BMKDC_TV_CHOICES = [
    (BMKDC_TV_CO, 'Có thực vật che phủ'),
    (BMKDC_TV_KHONG, 'Không có thực vật che phủ'),
]

### Bảng Đất trống
# Đối tượng Đất trống
DT_ = 'HC01'
DT_CHOICES = [
    (DT_, DT_),
]

### Bảng Nước mặt
# Đối tượng Nước mặt
NM_ = 'HD01'
NM_CHOICES = [
    (NM_, NM_),
]

### Bảng Thực vật đáy biển
# Đối tượng Thực vật đáy biển
TVDB_CB = 'HK01'
TVDB_RT = 'HK02'
TVDB_TVK = 'HK03'
TVDB_CHOICES = [
    (TVDB_CB, 'Cỏ biển'),
    (TVDB_RT, 'Rong, tảo'),
    (TVDB_TVK, 'Thực vật khác'),
]