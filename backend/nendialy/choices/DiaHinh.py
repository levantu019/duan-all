# ---------------------------------------------------------
# -------------------- 4. Địa hình --------------------------
# ---------------------------------------------------------
### Bảng Điểm độ cao
# Đối tượng Điểm độ cao
DDC_ = 'EA01'
DDC_CHOICES = [
    (DDC_, DDC_),
]

### Bảng Đường bình độ
# Đối tượng Đường bình độ
DBD_ = 'EA02'
DBD_CHOICES = [
    (DBD_, DBD_),
]

# Loại Đường bình độ
DBD_LOAI_CB = 1
DBD_LOAI_NUAKCD = 2
DBD_LOAI_PHU = 3
DBD_LOAI_NHAP = 4
DBD_LOAI_CHOICES = [
    (DBD_LOAI_CB, 'Cơ bản'),
    (DBD_LOAI_NUAKCD, 'Nửa khoảng cao đều'),
    (DBD_LOAI_PHU, 'Phụ'),
    (DBD_LOAI_NHAP, 'Nháp'),
]

# Loại Khoảng cao đều
DBD_LOAIKCD_0_5_M = 1
DBD_LOAIKCD_1_0_M = 2
DBD_LOAIKCD_2_5_M = 4
DBD_LOAIKCD_5_0_M = 5
DBD_LOAIKCD_10_0_M = 6
DBD_LOAIKCD_CHOICES = [
    (DBD_LOAIKCD_0_5_M, '0,5 m'),
    (DBD_LOAIKCD_1_0_M, '1,0 m'),
    (DBD_LOAIKCD_2_5_M, '2,5 m'),
    (DBD_LOAIKCD_5_0_M, '5,0 m'),
    (DBD_LOAIKCD_10_0_M, '10,0 m'),
]

### Bảng Chất đáy
# Đối tượng Chất đáy
CD_ = 'ED01'
CD_CHOICES = [
    (CD_, CD_),
]

# Loại Chất đáy
CD_LOAI_BUN = 1
CD_LOAI_CAT = 2
CD_LOAI_SANHO = 3
CD_LOAI_DA = 4
CD_LOAI_BUNCAT = 5
CD_LOAI_CATSANHO = 6
CD_LOAI_CATSOI = 7
CD_LOAI_DASANHO = 8
CD_LOAI_DASOI = 9
CD_LOAI_VOSOOC = 10
CD_LOAI_KHAC = 11
CD_LOAI_CHOICES = [
    (CD_LOAI_BUN, 'Bùn'),
    (CD_LOAI_CAT, 'Cát'),
    (CD_LOAI_SANHO, 'San hô'),
    (CD_LOAI_DA, 'Đá'),
    (CD_LOAI_BUNCAT, 'Bùn, cát'),
    (CD_LOAI_CATSANHO, 'Cát, san hô'),
    (CD_LOAI_CATSOI, 'Cát, sỏi'),
    (CD_LOAI_DASANHO, 'Đá, san hô'),
    (CD_LOAI_DASOI, 'Đá, sỏi'),
    (CD_LOAI_VOSOOC, 'Vỏ sò, ốc'),
    (CD_LOAI_KHAC, 'Loại khác'),
]

### Bảng Điểm độ sâu
# Đối tượng Điểm độ sâu
DDS_ = 'ED02'
DDS_CHOICES = [
    (DDS_, DDS_),
] 

### Bảng Đường bình độ sâu
# Đối tượng Đường bình độ sâu
DBDS_ = 'ED03'
DBDS_CHOICES = [
    (DBDS_, DBDS_),
]

# Loại Đường bình độ sâu
DBDS_LOAI_CB = 1
DBDS_LOAI_NUAKCD = 2
DBDS_LOAI_PHU = 3
DBDS_LOAI_NHAP = 4
DBDS_LOAI_CHOICES = [
    (DBDS_LOAI_CB, 'Cơ bản'),
    (DBD_LOAI_NUAKCD, 'Nửa khoảng cao đều'),
    (DBDS_LOAI_PHU, 'Phụ'),
    (DBDS_LOAI_NHAP, 'Nháp')
]

# Loại Khoảng cao đều
DBDS_LOAIKCD_0_5_M = 1
DBDS_LOAIKCD_1_0_M = 2
DBDS_LOAIKCD_2_0_M = 3
DBDS_LOAIKCD_2_5_M = 4
DBDS_LOAIKCD_5_0_M = 5
DBDS_LOAIKCD_10_0_M = 6
DBDS_LOAIKCD_CHOICES = [
    (DBDS_LOAIKCD_0_5_M, '0,5 m'),
    (DBDS_LOAIKCD_1_0_M, '1,0 m'),
    (DBDS_LOAIKCD_2_0_M, '2,0 m'),
    (DBDS_LOAIKCD_2_5_M, '2,5 m'),
    (DBDS_LOAIKCD_5_0_M, '5,0 m'),
    (DBDS_LOAIKCD_10_0_M, '10,0 m'),
]

### Bảng Địa hình đặc biệt đáy biển
# Đối tượng Địa hình đặc biệt đáy biển
DHDBDB_KRMN = 'ED04'
DHDBDB_NLDB = 'ED05'
DHDBDB_SDNDD = 'ED06'
DHDBDB_CHOICES = [
    (DHDBDB_KRMN, 'Khe rãnh máng ngầm'),
    (DHDBDB_NLDB, 'Núi lửa dưới biển'),
    (DHDBDB_SDNDD, 'Sườn đất ngầm dốc đứng'),
]

### Bảng Địa mạo
# Đối tượng Địa mạo
DIAMAO_CHOICES = [
    ('DM00', 'DM00'),
]

### Bảng Mô hình số độ cao gốc lớp điểm
# Đối tượng Mô hình số độ cao gốc lớp điểm
DEMGLP_DDC = 'EA01'
DEMGLP_DDS = 'ED02'
DEMGLP_KDLIDAR = 'EE01'
DEMGLP_KDDOSAU = 'EE02'
DEMGLP_KD = 'EE03'
DEMGLP_CHOICES = [
    (DEMGLP_DDC, 'Điểm độ cao'),
    (DEMGLP_DDS, 'Điểm độ sâu'),
    (DEMGLP_KDLIDAR, 'Khối điểm Lidar'),
    (DEMGLP_KDDOSAU, 'Khối điểm đo sâu'),
    (DEMGLP_KD, 'Khối điểm'),
]

### Bảng Mô hình số độ cao gốc lớp đường
# Đối tượng Mô hình số độ cao gốc lớp đường
DEMGLL_DBD = 'EA02'
DEMGLL_BDTN = 'EC01'
DEMGLL_DONGDA = 'EC02'
DEMGLL_DHBT = 'EC03'
DEMGLL_DHCXNT = 'EC04'
DEMGLL_KRXM = 'EC05'
DEMGLL_SDG = 'EC06'
DEMGLL_SSL = 'EC07'
DEMGLL_VACHDUNG = 'EC08'
DEMGLL_DBDS = 'ED03'
DEMGLL_KRMN = 'ED04'
DEMGLL_SDNDD = 'ED06'
DEMGLL_DMTDTDH = 'EE04'
DEMGLL_DBN = 'KE03'
DEMGLL_DMN = 'KE05'
DEMGLL_CHOICES = [
    (DEMGLL_DBD, 'Đường bình độ'),
    (DEMGLL_BDTN, 'Bờ dốc tự nhiên'),
    (DEMGLL_DONGDA, 'Dòng đá'),
    (DEMGLL_DHBT, 'Địa hình bậc thang'),
    (DEMGLL_DHCXNT, 'Địa hình cắt xẻ nhân tạo'),
    (DEMGLL_KRXM, 'Khe rãnh xói mòn'),
    (DEMGLL_SDG, 'Sườn đứt gãy'),
    (DEMGLL_SSL, 'Sườn sụt lở'),
    (DEMGLL_VACHDUNG, 'Vách đứng'),
    (DEMGLL_DBDS, 'Đường bình độ sâu'),
    (DEMGLL_KRMN, 'Khe rãnh máng ngầm'),
    (DEMGLL_SDNDD, 'Sườn đất ngầm dốc đứng'),
    (DEMGLL_DMTDTDH, 'Đường mô tả đặc trưng địa hình'),
    (DEMGLL_DBN, 'Đường bờ nước'),
    (DEMGLL_DMN, 'Đường mép nước'),
]

### Bảng Mô hình số độ cao gốc lớp vùng
# Đối tượng Mô hình số độ cao gốc lớp vùng
DEMGLA_VB = 'EE05'
DEMGLA_VMNTL = 'EE06'
DEMGLA_CHOICES = [
    (DEMGLA_VB, 'Vùng biển'),
    (DEMGLA_VMNTL, 'Vùng mặt nước tĩnh lặng'),
]

### Bảng Mô hình số độ cao gốc lớp vùng biển tập
# Đối tượng Mô hình số độ cao gốc lớp vùng biển tập
DEMGLVBT_KVBCK = 'EE07'
DEMGLVBT_KVTLDEM = 'EE08'
DEMGLVBT_CHOICES = [
    (DEMGLVBT_KVBCK, 'Khu vực bị che khuất'),
    (DEMGLVBT_KVTLDEM, 'Phạm vi khu vực thành lập mô hình số độ cao'),
]

### Bảng Hố khoan địa chất
# Đối tượng Hố khoan địa chất
HKDC_CHOICES = [
    ('HKDC', 'HKDC'),
]

### Bảng Mặt cắt điển hình địa chất
# Đối tượng Mặt cắt điển hình địa chất
MCDHDC_CHOICES = [
    ('MCDH', 'MCDH'),
]

### Bảng Địa chất
# Đối tượng Địa chất
DIACHAT_CHOICES = [
    ('DC00', 'DC00'),
]