# ---------------------------------------------------------
# -------------------- 7. Thuỷ văn --------------------------
# ---------------------------------------------------------
### Bảng Biển đảo
# Đối tượng Biển đảo
BD_BIEN = 'KA01'
BD_DQD = 'KA02'
BD_PHA = 'KA03'
BD_VV = 'KA04'
BD_CHOICES = [
    (BD_BIEN, 'Biển'),
    (BD_DQD, 'Đảo, quần đảo'),
    (BD_PHA, 'Phá'),
    (BD_VV, 'Vịnh, vũng'),
]

### Bảng Đảo
# Đối tượng Đảo
DAO_CHOICES = [
    ('DAO0', 'DAO0',)
]

# Loại Trạng thái xuất lô
DAO_LOAITTXL_CHIM = 1
DAO_LOAITTXL_NOI = 2
DAO_LOAITTXL_NCNN = 3
DAO_LOAITTXL_CHOICES = [
    (DAO_LOAITTXL_CHIM, 'Chìm'),
    (DAO_LOAITTXL_NOI, 'Nổi'),
    (DAO_LOAITTXL_NCNN, 'Nửa chìm, nửa nổi'),
]

### Bảng Bãi bồi
# Đối tượng Bãi bồi
BB_ = 'KB01'
BB_CHOICES = [
    (BB_, BB_),
]

# Loại Bãi bồi
BB_LOAI_CAT = 1
BB_LOAI_BUN = 2
BB_LOAI_KHAC = 3
BB_LOAI_CHOICES = [
    (BB_LOAI_CAT, 'Cát'),
    (BB_LOAI_BUN, 'Bùn'),
    (BB_LOAI_KHAC, 'Loại khác'),
]

# Trạng thái xuất lô
BB_TTXL_CHIM = 1
BB_TTXL_NOI = 2
BB_TTXL_LCLN = 3
BB_TTXL_KXD = 4
BB_TTXL_CHOICES = [
    (BB_TTXL_CHIM, 'Chìm'),
    (BB_TTXL_NOI, 'Nổi'),
    (BB_TTXL_LCLN, 'Lúc nổi, lúc chìm'),
    (BB_TTXL_KXD, 'Không xác định'),
]

### Bảng Bãi đá dưới nước
# Đối tượng Bãi đá dưới nước
BDDN_BDDN = 'KC01'
BDDN_DTB = 'KC02'
BDDN_SH = 'KC03'
BDDN_CHOICES = [
    (BDDN_BDDN, 'Bãi đá dưới nước'),
    (BDDN_DTB, 'Đá trên biển'),
    (BDDN_SH, 'San hô'),
]

# Trạng thái xuất lô
BDDN_TTXL_CHIM = 1
BDDN_TTXL_NOI = 2
BDDN_TTXL_LCLN = 3
BDDN_TTXL_KXD = 4
BDDN_TTXL_CHOICES = [
    (BDDN_TTXL_CHIM, 'Chìm'),
    (BDDN_TTXL_NOI, 'Nổi'),
    (BDDN_TTXL_LCLN, 'Lúc nổi, lúc chìm'),
    (BDDN_TTXL_KXD, 'Không xác định'),
]

### Bảng Nguồn nước
# Đối tượng Nguồn nước
NN_GN = 'KM01'
NN_MN = 'KM02'
NN_CHOICES = [
    (NN_GN, 'Giếng nước'),
    (NN_MN, 'Mạch nước'),
]

# Loại nguồn nước
NN_LOAI_KHOANG = 1
NN_LOAI_NONG = 2
NN_LOAI_THUONG = 3
NN_LOAI_CHOICES = [
    (NN_LOAI_KHOANG, 'Khoáng'),
    (NN_LOAI_NONG, 'Nóng'),
    (NN_LOAI_THUONG, 'Thường'),
]

### Bảng Điểm độ cao mực nước
# Đối tượng Điểm độ cao mực nước
DDCMN_ = 'KE01'
DDCMN_CHOICES = [
    (DDCMN_, DDCMN_),
]

### Bảng Đường bờ nước
# Đối tượng Đường bờ nước
DBN_ = 'KE03'
DBN_CHOICES = [
    (DBN_, DBN_),
]

# Loại trạng thái đường bờ nước
DBN_LOAITT_RR = 1
DBN_LOAITT_KXD = 2
DBN_LOAITT_DBSSCNTM = 3
DBN_LOAITT_CHOICES = [
    (DBN_LOAITT_RR, 'Rõ ràng'),
    (DBN_LOAITT_KXD, 'Khó xác định'),
    (DBN_LOAITT_DBSSCNTM, 'Đường bờ sông suối có nước theo mùa'),
]

# Loại đường bờ nước
DBN_LOAI_AHD = 1
DBN_LOAI_PHA = 2
DBN_LOAI_KM = 3
DBN_LOAI_HC = 4
DBN_LOAI_SS = 5
DBN_LOAI_BIEN = 6
DBN_LOAI_CHOICES = [
    (DBN_LOAI_AHD, 'Ao, hồ, đầm'),
    (DBN_LOAI_PHA, 'Phá'),
    (DBN_LOAI_KM, 'Kênh, mương'),
    (DBN_LOAI_HC, 'Hồ chứa'),
    (DBN_LOAI_SS, 'Sông, suối'),
    (DBN_LOAI_BIEN, 'Biển'),
]

### Bảng Đường mép nước
# Đối tượng Đường mép nước
DMN_= 'KE05'
DMN_CHOICES = [
    (DMN_, DMN_),
]

# Loại đường mép nước
DMN_LOAI_AHD = 1
DMN_LOAI_PHA = 2
DMN_LOAI_KM = 3
DMN_LOAI_HC = 4
DMN_LOAI_SS = 5
DMN_LOAI_BIEN = 6
DMN_LOAI_TK = 7
DMN_LOAI_CHOICES = [
    (DMN_LOAI_AHD, 'Ao, hồ, đầm'),
    (DMN_LOAI_PHA, 'Phá'),
    (DMN_LOAI_KM, 'Kênh, mương'),
    (DMN_LOAI_HC, 'Hồ chứa'),
    (DMN_LOAI_SS, 'Sông, suối'),
    (DMN_LOAI_BIEN, 'Biển'),
    (DMN_LOAI_TK, 'Triều kiệt'),
]

### Bảng Ranh giới nước mặt quy ước
# Đối tượng Ranh giới nước mặt quy ước
RGNMQU_ = 'KE06'
RGNMQU_CHOICES = [
    (RGNMQU_, RGNMQU_),
]

# Loại ranh giới nước mặt quy ước
RGNMQU_LOAI_PCLNM = 1
RGNMQU_LOAI_KVNM = 2
RGNMQU_LOAI_CHOICES = [
    (RGNMQU_LOAI_PCLNM, 'Phân chia loại nước mặt'),
    (RGNMQU_LOAI_KVNM, 'Khép vùng nước mặt'),
]

### Bảng Bờ kè bờ cạp
# Đối tượng Bờ kè bờ cạp
BKBC_ = 'KG01'
BKBC_CHOICES = [
    (BKBC_, BKBC_),
]

# Loại chất liệu
BKBC_LOAICL_BT = 1
BKBC_LOAICL_DS = 2
BKBC_LOAICL_KHAC = 3
BKBC_LOAICL_CHOICES = [
    (BKBC_LOAICL_BT, 'Bê tông'),
    (BKBC_LOAICL_DS, 'Đá sỏi'),
    (BKBC_LOAICL_KHAC, 'Khác'),
]

# Loại thành phần
BKBC_LOAITP_CHAN = 1
BKBC_LOAITP_DINH = 2
BKBC_LOAITP_CHOICES = [
    (BKBC_LOAITP_CHAN, 'Chân'),
    (BKBC_LOAITP_DINH, 'Đỉnh'),
]

### Bảng Kênh mương
# Đối tượng Kênh mương
KM_ = 'KG05'
KM_CHOICES = [
    (KM_, KM_),
]

# Loại hiện trạng sử dụng
KM_LOAIHTSD_DSD = 1
KM_LOAIHTSD_DXD = 2
KM_LOAIHTSD_KSD = 3
KM_LOAIHTSD_CHOICES = [
    (KM_LOAIHTSD_DSD, 'Đang sử dụng'),
    (KM_LOAIHTSD_DXD, 'Đang xây dựng'),
    (KM_LOAIHTSD_KSD, 'Không sử dụng'),
]

### Bảng Trạm thu thập TTTV
# Đối tượng Trạm thu thập TTTV
TTTKTTV_ = 'CR20'
TTTKTTV_CHOICES = [
    (TTTKTTV_, TTTKTTV_),
]

# Loại Trạm thu thậP TTTV
TTTKTTV_LOAI_TKTBM = 1
TTTKTTV_LOAI_TKTTC = 2
TTTKTTV_LOAI_TRDTT = 3
TTTKTTV_LOAI_TKTNN = 4
TTTKTTV_LOAI_TTV = 5
TTTKTTV_LOAI_THV = 6
TTTKTTV_LOAI_TDVS = 7
TTTKTTV_LOAI_TGSBDKH = 8
TTTKTTV_LOAI_TCD = 9
TTTKTTV_LOAI_CHOICES = [
    (TTTKTTV_LOAI_TKTBM, 'Trạm khí tượng bề mặt'),
    (TTTKTTV_LOAI_TKTTC, 'Trạm khí tượng trên cao'),
    (TTTKTTV_LOAI_TRDTT, 'Trạm ra đa thời tiết'),
    (TTTKTTV_LOAI_TKTNN, 'Trạm khí tượng nông nghiệp'),
    (TTTKTTV_LOAI_TTV, 'Trạm thủy văn'),
    (TTTKTTV_LOAI_THV, 'Trạm hải văn'),
    (TTTKTTV_LOAI_TDVS, 'Trạm định vị sét'),
    (TTTKTTV_LOAI_TGSBDKH, 'Trạm giám sát biến đổi khí hậu'),
    (TTTKTTV_LOAI_TCD, 'Trạm chuyên đề'),
]

# Kiểu thu thập KTTV
TTTKTTV_KTT_TCD = 1
TTTKTTV_KTT_TDD = 2
TTTKTTV_KTT_CHOICES = [
    (TTTKTTV_KTT_TCD, 'Trạm cố định'),
    (TTTKTTV_KTT_TDD, 'Trạm di động'),
]

### Bảng Tham số KTTV
# Đối tượng Tham số KTTV
TSKTTV_ = 'TS01'
TSKTTV_CHOICES = [
    (TSKTTV_, TSKTTV_),
]

# Tham số
TSKTTV_TS_NDKK = 1
TSKTTV_TS_DAKK = 2
TSKTTV_TS_ASKK = 3
TSKTTV_TS_LM = 4
TSKTTV_TS_MN = 5
TSKTTV_TS_CHOICES = [
    (TSKTTV_TS_NDKK, 'Nhiệt độ không khí'),
    (TSKTTV_TS_DAKK, 'Độ ẩm không khí'),
    (TSKTTV_TS_ASKK, 'Áp suất không khí'),
    (TSKTTV_TS_LM, 'Lượng mưa'),
    (TSKTTV_TS_MN, 'Mực nước'),
]

### Bảng Sóng gió dòng chảy
# Đối tượng Sóng gió dòng chảy
SGDC_ = 'TS02'
SGDC_CHOICES = [
    (SGDC_, SGDC_),
]

# Hướng
SGDC_HUONG_N = 'N'
SGDC_HUONG_NNE = 'NNE'
SGDC_HUONG_NE = 'NE'
SGDC_HUONG_ENE = 'ENE'
SGDC_HUONG_E = 'E'
SGDC_HUONG_ESE = 'ESE'
SGDC_HUONG_SE = 'SE'
SGDC_HUONG_SSE = 'SSE'
SGDC_HUONG_S = 'S'
SGDC_HUONG_SSW = 'SSW'
SGDC_HUONG_SW = 'SW'
SGDC_HUONG_WSW = 'WSW'
SGDC_HUONG_W = 'W'
SGDC_HUONG_WNW = 'WNW'
SGDC_HUONG_NW = 'NW'
SGDC_HUONG_NWN = 'NWN'
SGDC_HUONG_CHOICES = [
    (SGDC_HUONG_N, 'Hướng Bắc'),
    (SGDC_HUONG_NNE, 'Bắc-Đông Bắc'),
    (SGDC_HUONG_NE, 'Đông Bắc'),
    (SGDC_HUONG_ENE, 'Đông-Đông Bắc'),
    (SGDC_HUONG_E, 'Hướng Đông'),
    (SGDC_HUONG_ESE, 'Đông-Đông Nam'),
    (SGDC_HUONG_SE, 'Đông Nam'),
    (SGDC_HUONG_SSE, 'Nam-Đông Nam'),
    (SGDC_HUONG_S, 'Hướng Nam'),
    (SGDC_HUONG_SSW, 'Nam-Tây Nam'),
    (SGDC_HUONG_SW, 'Tây Nam'),
    (SGDC_HUONG_WSW, 'Tây-Tây Nam'),
    (SGDC_HUONG_W, 'Hướng Tây'),
    (SGDC_HUONG_WNW, 'Tây-Tây Bắc'),
    (SGDC_HUONG_NW, 'Tây Bắc'),
    (SGDC_HUONG_NWN, 'Bắc-Tây Bắc'),
]

# Tham số
SGDC_TS_GIO = 1
SGDC_TS_DONGCHAY = 2
SGDC_TS_SONG = 3
SGDC_TS_CHOICES = [
    (SGDC_TS_GIO, 'Gió'),
    (SGDC_TS_DONGCHAY, 'Dòng chảy'),
    (SGDC_TS_SONG, 'Sóng'),
]

### Bảng Tham số nước
# Đối tượng Tham số nước
TSN_ = 'TS03'
TSN_CHOICES = [
    (TSN_, TSN_),
]

# Tầng độ sâu
TSN_TDS_TM = 1
TSN_TDS_T15M = 2
TSN_TDS_T30M = 3
TSN_TDS_TD = 4
TSN_TDS_CHOICES = [
    (TSN_TDS_TM, 'Tầng mặt'),
    (TSN_TDS_T15M, 'Tầng 15m'),
    (TSN_TDS_T30M, 'Tầng 30m'),
    (TSN_TDS_TD, 'Tầng đáy'),
]

# Tham số
TSN_TS_NDN = 1
TSN_TS_DMN = 2
TSN_TS_CA = 3
TSN_TS_CL = 4
TSN_TS_SO4 = 5
TSN_TS_HCO3 = 6
TSN_TS_MG = 7
TSN_TS_NAK = 8
TSN_TS_CHOICES = [
    (TSN_TS_NDN, 'Nhiệt độ nước'),
    (TSN_TS_DMN, 'Độ mặn nước'),
    (TSN_TS_CA, 'Ca'),
    (TSN_TS_CL, 'Cl'),
    (TSN_TS_SO4, 'SO4'),
    (TSN_TS_HCO3, 'HCO3'),
    (TSN_TS_MG, 'MG'),
    (TSN_TS_NAK, 'NAK'),
]