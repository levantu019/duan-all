# ---------------------------------------------------------------
# -------------------- 1. Biên giới địa giới --------------------
# ---------------------------------------------------------------
### Bảng Vùng biển
# Đối tượng Vùng biển
VB_LANHHAI = 'AB07'
VB_VUNGNOITHUY = 'AB11'
VB_VUNGNUOCLS = 'AB12'
VB_VUNGTIEPGIAPLANHHAI = 'AB13'
VB_CHOICES = [
    (VB_LANHHAI, 'Lãnh hải'),
    (VB_VUNGNOITHUY, 'Vùng nội thuỷ'),
    (VB_VUNGNUOCLS, 'Vùng nước lịch sử'),
    (VB_VUNGTIEPGIAPLANHHAI, 'Vùng tiếp giáp lãnh hải'),
]

### Bảng Địa phận hành chính trên biển
# Đối tượng Địa phận hành chính trên biển
DPHCTB_HUYEN = 'AE01'
DPHCTB_TINH = 'AE02'
DPHCTB_XA = 'AE03'
DPHCTB_CHOICES = [
    (DPHCTB_HUYEN, 'Địa phận hành chính cấp huyện trên biển'),
    (DPHCTB_TINH, 'Địa phận hành chính cấp tỉnh trên biển'),
    (DPHCTB_XA, 'Địa phận hành chính cấp xã trên biển'),
]

### Bảng Đường ranh giới hành chính trên biển
# Đối tượng Đường ranh giới hành chính trên biển
DRGHCTB_HUYEN = 'AE04'
DRGHCTB_TINH = 'AE05'
DRGHCTB_XA = 'AE06'
DRGHCTB_CHOICES = [
    (DRGHCTB_HUYEN, 'Đường ranh giới hành chính cấp huyện trên biển'),
    (DRGHCTB_TINH, 'Đường ranh giới hành chính cấp tỉnh trên biển'),
    (DRGHCTB_TINH, 'Đường ranh giới hành chính cấp xã trên biển'),
]

# Loại hiện trạng pháp lý
DRGHCTB_HTPL_DEFINED = 1
DRGHCTB_HTPL_UNDEFINED = 0
DRGHCTB_HTPL_CHOICES = [
    (DRGHCTB_HTPL_DEFINED, 'Xác định'),
    (DRGHCTB_HTPL_UNDEFINED, 'Chưa xác định'),
]

### Bảng Địa phận hành chính trên đất liền
# Đối tượng Địa phận hành chính trên đất liền
DPHCTDL_CHOICES = [
    ('AD01', 'Địa phận hành chính cấp huyện'),
    ('AD02', 'Địa phận hành chính cấp tỉnh'),
    ('AD03', 'Địa phận hành chính cấp xã'),
]

# ###### GIÁ TRỊ MẶC ĐỊNH ######
# ### Bảng Vùng biển
# # Đối tượng Vùng biển
# VB_DEFAULT = VB_LANHHAI

# ### Bảng Địa phận hành chính trên biển
# # Đối tượng Địa phận hành chính trên biển
# DPHCTB_DEFAULT = DPHCTB_HUYEN

# ### Bảng Đường ranh giới hành chính trên biển
# # Đối tượng Đường ranh giới hành chính trên biển
# DRGHCTB_DEFAULT = DRGHCTB_HUYEN

# # Loại hiện trạng pháp lý
# DRGHCTB_HTPL_DEFAULT = DRGHCTB_HTPL_DEFINED
