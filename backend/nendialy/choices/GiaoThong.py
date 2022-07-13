# ---------------------------------------------------------
# -------------------- 5. Giao thông --------------------------
# ---------------------------------------------------------
### Bảng Đường bộ
# Đối tượng Đường bộ
DB_DCD = 'GK01'
DB_DDT = 'GK02'
DB_DH = 'GK03'
DB_DQL = 'GK04'
DB_DT = 'GK05'
DB_DX = 'GK06'
DB_CHOICES = [
    (DB_DCD, 'Đường chuyên dùng'),
    (DB_DDT, 'Đường đô thị'),
    (DB_DH, 'Đường huyện'),
    (DB_DQL, 'Đường quốc lộ'),
    (DB_DT, 'Đường tỉnh'),
    (DB_DX, 'Đường xã'),
]

# Loại đường bộ
DB_LOAI_DC = 1
DB_LOAI_DD = 2
DB_LOAI_DG = 3
DB_LOAI_DN = 4
DB_LOAI_CHOICES = [
    (DB_LOAI_DC, 'Đường chính'),
    (DB_LOAI_DD, 'Đường dẫn'),
    (DB_LOAI_DG, 'Đường gom'),
    (DB_LOAI_DN, 'Đường nhánh'),
]

# Cấp kỹ thuật
DB_CKT_CAOTOC = 1
DB_CKT_CAPKHAC = 2
DB_CKT_CHOICES = [
    (DB_CKT_CAOTOC, 'Cao tốc'),
    (DB_CKT_CAPKHAC, 'Cấp khác'),
]

# Loại chất liệu trải mặt
DB_LOAICLTM_BT = 1
DB_LOAICLTM_N = 2
DB_LOAICLTM_DS = 3
DB_LOAICLTM_G = 4
DB_LOAICLTM_D = 5
DB_LOAICLTM_KHAC = 6
DB_LOAICLTM_CHOICES = [
    (DB_LOAICLTM_BT, 'Bê tông'),
    (DB_LOAICLTM_N, 'Nhựa'),
    (DB_LOAICLTM_DS, 'Đá, sỏi'),
    (DB_LOAICLTM_G, 'Gạch'),
    (DB_LOAICLTM_D, 'Đất'),
    (DB_LOAICLTM_KHAC, 'Khác'),
]

# Loại hiện trạng sử dụng
DB_LOAIHTSD_DSD = 1
DB_LOAIHTSD_DXD = 2
DB_LOAIHTSD_KSD = 3
DB_LOAIHTSD_CHOICES = [
    (DB_LOAIHTSD_DSD, 'Đang sử dụng'),
    (DB_LOAIHTSD_DXD, 'Đang xây dựng'),
    (DB_LOAIHTSD_KSD, 'Không sử dụng'),
]

# Chiều xe chạy
DB_CHIEUXECHAY_1 = 1
DB_CHIEUXECHAY_2 = 2
DB_CHIEUXECHAY_CHOICES = [
    (DB_CHIEUXECHAY_1, 'Một chiều'),
    (DB_CHIEUXECHAY_2, 'Hai chiều'),
]

# Vị trí
DB_VITRI_TMD = 1
DB_VITRI_TCM1 = 2
DB_VITRI_TCM2 = 3
DB_VITRI_TCM3 = 4
DB_VITRI_TCM4 = 5
DB_VITRI_TCM5 = 6
DB_VITRI_NM1 = 7
DB_VITRI_NM2 = 8
DB_VITRI_CHOICES = [
    (DB_VITRI_TMD, 'Trên mặt đất'),
    (DB_VITRI_TCM1, 'Trên cao mức 1'),
    (DB_VITRI_TCM2, 'Trên cao mức 2'),
    (DB_VITRI_TCM3, 'Trên cao mức 3'),
    (DB_VITRI_TCM4, 'Trên cao mức 4'),
    (DB_VITRI_TCM5, 'Trên cao mức 5'),
    (DB_VITRI_NM1, 'Ngầm mức 1'),
    (DB_VITRI_NM2, 'Ngầm mức 2'),
]

# Liên kết giao thông
DB_LKGT_QC = 1
DB_LKGT_QH = 2
DB_LKGT_TD = 3
DB_LKGT_QN = 4
DB_LKGT_QPDB = 5
DB_LKGT_QDO = 6
DB_LKGT_QBL = 7
DB_LKGT_QDAP = 8
DB_LKGT_KHAC = 9
DB_LKGT_CHOICES = [
    (DB_LKGT_QC, 'Qua cầu'),
    (DB_LKGT_QH, 'Qua hầm'),
    (DB_LKGT_TD, 'Trên đê'),
    (DB_LKGT_QN, 'Qua ngầm'),
    (DB_LKGT_QPDB, 'Qua phà đường bộ'),
    (DB_LKGT_QDO, 'Qua đò'),
    (DB_LKGT_QBL, 'Qua bến lội'),
    (DB_LKGT_QDAP, 'Qua đập'),
    (DB_LKGT_KHAC, 'Khác'),
]

### Bảng Cống giao thông
# Đối tượng Cống giao thông
CGT_ = 'GG06'
CGT_CHOICES = [
    (CGT_, CGT_),
]

### Bảng Đường băng
# Đối tượng Đường băng
DBANG_ = 'GN04'
DBANG_CHOICES = [
    (DBANG_, DBANG_),
]

### Bảng Bãi đáp trực thăng
# Đối tượng Bãi đáp trực thăng
BDTT_ = 'GN01'
BDTT_CHOICES = [
    (BDTT_, BDTT_),
]

# Vị trí bãi đáp
BDTT_VTBD_TMD = 1
BDTT_VTBD_TNN = 2
BDTT_VTBD_CHOICES = [
    (BDTT_VTBD_TMD, 'Trên mặt đất'),
    (BDTT_VTBD_TNN, 'Trên nóc nhà'),
]

### Bảng Báo hiệu hàng hải AIS
# Đối tượng Báo hiệu hàng hải AIS
BHHHAIS_ = 'GM02'
BHHHAIS_CHOICES = [
    (BHHHAIS_, BHHHAIS_),
]

### Bảng Bến cảng
# Đối tượng Bến cảng
BC_ = 'GM03'
BC_CHOICES = [
    (BC_, BC_),
]

### Bảng Cầu tàu
# Đối tượng Cầu tàu
CT_ = 'GM08'
CT_CHOICES = [
    (CT_, CT_),
]

# Loại cầu tàu
CT_LOAI_KCCD = 1
CT_LOAI_KCN = 2
CT_LOAI_CHOICES = [
    (CT_LOAI_KCCD, 'Kết cấu cố định'),
    (CT_LOAI_KCN, 'Kết cấu nổi'),
]

### Bảng Báo hiệu dẫn luồng hàng hải đường thuỷ
# Đối tượng Báo hiệu dẫn luồng hàng hải đường thuỷ
BHDLHHDT_CT = 'GA01'
BHDLHHDT_DT = 'GA02'
BHDLHHDT_PBH = 'GA03'
BHDLHHDT_TBH = 'GA04'
BHDLHHDT_CHOICES = [
    (BHDLHHDT_CT, 'Chập tiêu'),
    (BHDLHHDT_DT, 'Đăng tiêu'),
    (BHDLHHDT_PBH, 'Phao báo hiệu'),
    (BHDLHHDT_TBH, 'Tiêu báo hiệu'),
]

# Hướng báo hiệu
BHDLHHDT_HUONGBH_T = 1
BHDLHHDT_HUONGBH_P = 2
BHDLHHDT_HUONGBH_CHT = 3
BHDLHHDT_HUONGBH_CHP = 4
BHDLHHDT_HUONGBH_KHAC = 5
BHDLHHDT_HUONGBH_CHOICES = [
    (BHDLHHDT_HUONGBH_T, 'Trái'),
    (BHDLHHDT_HUONGBH_P, 'Phải'),
    (BHDLHHDT_HUONGBH_CHT, 'Chuyển hướng trái'),
    (BHDLHHDT_HUONGBH_CHP, 'Chuyển hướng Phải'),
    (BHDLHHDT_HUONGBH_KHAC, 'Khác'),
]

# Hình dạng
BHDLHHDT_HINHDANG_HTHAP = 1
BHDLHHDT_HINHDANG_HTRU = 2
BHDLHHDT_HINHDANG_HCAU = 3
BHDLHHDT_HINHDANG_HCOT = 4
BHDLHHDT_HINHDANG_HTRUCQUAY = 5
BHDLHHDT_HINHDANG_HTHUNG = 6
BHDLHHDT_HINHDANG_HTHAPLUOI = 7
BHDLHHDT_HINHDANG_HKHAC = 8
BHDLHHDT_HINHDANG_KXD = 9
BHDLHHDT_HINHDANG_CHOICES = [
    (BHDLHHDT_HINHDANG_HTHAP, 'Hình tháp'),
    (BHDLHHDT_HINHDANG_HTRU, 'Hình trụ'),
    (BHDLHHDT_HINHDANG_HCAU, 'Hình cầu'),
    (BHDLHHDT_HINHDANG_HCOT, 'Hình cột'),
    (BHDLHHDT_HINHDANG_HTRUCQUAY, 'Hình trục quay'),
    (BHDLHHDT_HINHDANG_HTHUNG, 'Hình thùng'),
    (BHDLHHDT_HINHDANG_HTHAPLUOI, 'Hình tháp lưới'),
    (BHDLHHDT_HINHDANG_HKHAC, 'Hình khác'),
    (BHDLHHDT_HINHDANG_KXD, 'Không xác định'),
]

# Màu sắc
BHDLHHDT_MAUSAC_TRANG = 1
BHDLHHDT_MAUSAC_DEN = 2
BHDLHHDT_MAUSAC_DO = 3
BHDLHHDT_MAUSAC_XANHLC = 4
BHDLHHDT_MAUSAC_XANHDT = 5
BHDLHHDT_MAUSAC_VANG = 6
BHDLHHDT_MAUSAC_XAM = 7
BHDLHHDT_MAUSAC_NAU = 8
BHDLHHDT_MAUSAC_HOPHACH = 9
BHDLHHDT_MAUSAC_TIM = 10
BHDLHHDT_MAUSAC_CAM = 11
BHDLHHDT_MAUSAC_DOTUOI = 12
BHDLHHDT_MAUSAC_HONG = 13
BHDLHHDT_MAUSAC_RGR = 14
BHDLHHDT_MAUSAC_GRG = 15
BHDLHHDT_MAUSAC_RGW = 16
BHDLHHDT_MAUSAC_RW = 17
BHDLHHDT_MAUSAC_KXD = 18
BHDLHHDT_MAUSAC_CHOICES = [
    (BHDLHHDT_MAUSAC_TRANG, 'Trắng'),
    (BHDLHHDT_MAUSAC_DEN, 'Đen'),
    (BHDLHHDT_MAUSAC_DO, 'Đỏ'),
    (BHDLHHDT_MAUSAC_XANHLC, 'Xanh lá cây'),
    (BHDLHHDT_MAUSAC_XANHDT, 'Xanh da trời'),
    (BHDLHHDT_MAUSAC_VANG, 'Vàng'),
    (BHDLHHDT_MAUSAC_XAM, 'Xám'),
    (BHDLHHDT_MAUSAC_NAU, 'Nâu'),
    (BHDLHHDT_MAUSAC_HOPHACH, 'Hổ phách'),
    (BHDLHHDT_MAUSAC_TIM, 'Tím'),
    (BHDLHHDT_MAUSAC_CAM, 'Cam'),
    (BHDLHHDT_MAUSAC_DOTUOI, 'Đỏ tươi'),
    (BHDLHHDT_MAUSAC_HONG, 'Hồng'),
    (BHDLHHDT_MAUSAC_RGR, 'Đỏ, xanh, đỏ'),
    (BHDLHHDT_MAUSAC_GRG, 'Xanh, đỏ, xanh'),
    (BHDLHHDT_MAUSAC_RGW, 'Đỏ, xanh, trắng'),
    (BHDLHHDT_MAUSAC_RW, 'Đỏ trắng'),
    (BHDLHHDT_MAUSAC_KXD, 'Không xác định'),
]

# Phối hợp màu sắc
BHDLHHDT_PHMS_KN = 1
BHDLHHDT_PHMS_KD = 2
BHDLHHDT_PHMS_KC = 3
BHDLHHDT_PHMS_KOV = 4
BHDLHHDT_PHMS_KKRH = 5
BHDLHHDT_PHMS_KV = 6
BHDLHHDT_PHMS_KXD = 7
BHDLHHDT_PHMS_CHOICES = [
    (BHDLHHDT_PHMS_KN, 'Kẻ ngang'),
    (BHDLHHDT_PHMS_KD, 'Kẻ dọc'),
    (BHDLHHDT_PHMS_KC, 'Kẻ chéo'),
    (BHDLHHDT_PHMS_KOV, 'Kẻ ô vuông'),
    (BHDLHHDT_PHMS_KKRH, 'Kẻ không rõ hướng'),
    (BHDLHHDT_PHMS_KV, 'Kẻ viền'),
    (BHDLHHDT_PHMS_KXD, 'Không xác định'),
]

### Bảng Các đối tượng hàng hải hải văn
# Đối tượng ...
CDTHHHV_CDKNK = 'GC01'
CDTHHHV_CBTT = 'GC02'
CDTHHHV_DBC = 'GC03'
CDTHHHV_DENBIEN = 'GC04'
CDTHHHV_KND = 'GC05'
CDTHHHV_KTB = 'GC06'
CDTHHHV_KVATVTHH = 'GC07'
CDTHHHV_KVBTTNTB = 'GC08'
CDTHHHV_KVDC = 'GC09'
CDTHHHV_KVDHT = 'GC10'
CDTHHHV_KVNV = 'GC11'
CDTHHHV_KVNCKS = 'GC12'
CDTHHHV_KVNH = 'GC13'
CDTHHHV_KVQLC = 'GC14'
CDTHHHV_KVQS = 'GC15'
CDTHHHV_KVTCHH = 'GC16'
CDTHHHV_KVVNAT = 'GC17'
CDTHHHV_KVXTLS = 'GC18'
CDTHHHV_LBNTTHS = 'GC19'
CDTHHHV_NHAGIAN = 'GC20'
CDTHHHV_NHATB = 'GC21'
CDTHHHV_TRAMCN = 'GC22'
CDTHHHV_TRAMNT = 'GC23'
CDTHHHV_TUYENHH = 'GC24'
CDTHHHV_VUNGCAM = 'GC25'
CDTHHHV_XACTAUDAM = 'GC26'
CDTHHHV_CHOICES = [
    (CDTHHHV_CDKNK, 'Cảng dầu khí ngoài khơi'),
    (CDTHHHV_CBTT, 'Cọc buộc tàu thuyền'),
    (CDTHHHV_DBC, 'Đăng, chắn đánh bắt cá ổn định'),
    (CDTHHHV_DENBIEN, 'Đèn biển'),
    (CDTHHHV_KND, 'Khu neo đậu'),
    (CDTHHHV_KTB, 'Khu tránh bão'),
    (CDTHHHV_KVATVTHH, 'Khu vực an toàn viện trợ hàng hải'),
    (CDTHHHV_KVBTTNTB, 'Khu vực bảo tồn thiên nhiên trên biển'),
    (CDTHHHV_KVDC, 'Khu vực đánh cá'),
    (CDTHHHV_KVDHT, 'Khu vực đợi hoa tiêu'),
    (CDTHHHV_KVNV, 'Khu vực nạo vét'),
    (CDTHHHV_KVNCKS, 'Khu vực nghiên cứu, khảo sát'),
    (CDTHHHV_KVNH, 'Khu vực nguy hiểm'),
    (CDTHHHV_KVQLC, 'Khu vực quản lý cảng'),
    (CDTHHHV_KVQS, 'Khu vực quân sự'),
    (CDTHHHV_KVTCHH, 'Khu vực trung chuyển hàng hóa'),
    (CDTHHHV_KVVNAT, 'Khu vực vùng nước an toàn'),
    (CDTHHHV_KVXTLS, 'Khu vực xác tàu lịch sử'),
    (CDTHHHV_LBNTTHS, 'Lồng bè nuôi trồng thủy hải sản'),
    (CDTHHHV_NHAGIAN, 'Nhà giàn'),
    (CDTHHHV_NHATB, 'Nhà trên biển'),
    (CDTHHHV_TRAMCN, 'Trạm cứu nạn'),
    (CDTHHHV_TRAMNT, 'Trạm nghiệm triều'),
    (CDTHHHV_TUYENHH, 'Tuyến hàng hải'),
    (CDTHHHV_VUNGCAM, 'Vùng cấm'),
    (CDTHHHV_XACTAUDAM, 'Xác tàu đắm'),
]

### Bảng Nhom âu tàu
# Đối tượng Bảng Nhom âu tàu
NAT_AT = 'GM01'
NAT_BXAT = 'GM05'
NAT_CAT = 'GM09'
NAT_CHOICES = [
    (NAT_AT, 'Âu tàu'),
    (NAT_BXAT, 'Bờ xây âu tàu'),
    (NAT_CAT, 'Cửa âu tàu'),
]