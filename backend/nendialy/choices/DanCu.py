# ---------------------------------------------------------
# -------------------- 3. Dân Cư --------------------------
# ---------------------------------------------------------
### Bảng Khu dân cư
# Đối tượng Khu dân cư
KDC_ = 'CA02'
KDC_CHOICES = [
    (KDC_, KDC_),
]

# Loại khu dân cư
KDC_LOAI_DOTHI = 1
KDC_LOAI_NONGTHON = 2
KDC_LOAI_CHOICES = [
    (KDC_LOAI_DOTHI, 'Đô thị'),
    (KDC_LOAI_NONGTHON, 'Nông thôn'),
]

### Bảng Nhà
# Đối tượng Nhà
NHA_ = 'CA04'
NHA_CHOICES = [
    (NHA_, NHA_),
]

# Loại nhà
NHA_LOAI_CHUNGCU = 1
NHA_LOAI_NHARIENG = 2
NHA_LOAI_ANNINHQUOCPHONG = 3
NHA_LOAI_COQUANNHANUOC = 4
NHA_LOAI_TRUSOLAMVIEC = 5
NHA_LOAI_HONHOP = 6
NHA_LOAI_NHACONGTRINHCONGCONG = 7
NHA_LOAI_NHACONGTRINHCONGNGHIEP = 8
NHA_LOAI_NHACONGTRINHHATANGKYTHUAT = 9
NHA_LOAI_NHACSSXNONGLAMNGHIEP = 10
NHA_LOAI_NHAKHUCHUCNANGDACTHU = 11
NHA_LOAI_NHAPHUTRODANSINH = 12
NHA_LOAI_CHOICES = [
    (NHA_LOAI_CHUNGCU, 'Chung cư'),
    (NHA_LOAI_NHARIENG, 'Nhà riêng'),
    (NHA_LOAI_ANNINHQUOCPHONG, 'An ninh, Quốc phòng'),
    (NHA_LOAI_COQUANNHANUOC, 'Cơ quan nhà nước'),
    (NHA_LOAI_TRUSOLAMVIEC, 'Trụ sở làm việc'),
    (NHA_LOAI_HONHOP, 'Hỗn hợp'),
    (NHA_LOAI_NHACONGTRINHCONGCONG, 'Nhà công trình công cộng'),
    (NHA_LOAI_NHACONGTRINHCONGNGHIEP, 'Nhà công trình công nghiệp'),
    (NHA_LOAI_NHACONGTRINHHATANGKYTHUAT, 'Nhà công trình hạ tầng kỹ thuật'),
    (NHA_LOAI_NHACSSXNONGLAMNGHIEP, 'Nhà cơ sở sản xuất nông lâm nghiệp'),
    (NHA_LOAI_NHAKHUCHUCNANGDACTHU, 'Nhà khu chức năng đặc thù'),
    (NHA_LOAI_NHAPHUTRODANSINH, 'Nhà phụ trọ dân sinh'),
]

# Mức độ kiên cố
NHA_MUCDOKIENCO_KIENCO = 1
NHA_MUCDOKIENCO_BANKIENCO = 2
NHA_MUCDOKIENCO_KHONGKIENCO = 3
NHA_MUCDOKIENCO_DONSO = 4
NHA_MUCDOKIENCO_CHOICES = [
    (NHA_MUCDOKIENCO_KIENCO, 'Kiên cố'),
    (NHA_MUCDOKIENCO_BANKIENCO, 'Bán kiên cố'),
    (NHA_MUCDOKIENCO_KHONGKIENCO, 'Không kiên cố'),
    (NHA_MUCDOKIENCO_DONSO, 'Đơn sơ'),
]

### Bảng Công trình phụ trợ
# Đối tượng Công trình phụ trợ
CTPT_BACTHEM = 'CG01'
CTPT_CAUTHANGNGOAITROI = 'CG02'
CTPT_HANHLANG = 'CG03'
CTPT_LOIXUONGTANGHAM = 'CG04'
CTPT_CHOICES = [
    (CTPT_BACTHEM, 'Bậc thềm'),
    (CTPT_CAUTHANGNGOAITROI, 'Cầu thang ngoài trời'),
    (CTPT_HANHLANG, 'Hành lang'),
    (CTPT_LOIXUONGTANGHAM, 'Lối xuống tầng hầm'),
]

### Bảng Khối nhà
# Đối tượng Khối nhà
KN_ = 'CA01'
KN_CHOICES = [
    (KN_, KN_),
]

# Nhóm số tầng
KN_NHOMSOTANG_DACBIET = 1
KN_NHOMSOTANG_I = 2
KN_NHOMSOTANG_II = 3
KN_NHOMSOTANG_III = 4
KN_NHOMSOTANG_IV = 5
KN_NHOMSOTANG_CHOICES = [
    (KN_NHOMSOTANG_DACBIET, 'Đặc biệt'),
    (KN_NHOMSOTANG_I, 'Cấp I'),
    (KN_NHOMSOTANG_II, 'Cấp II'),
    (KN_NHOMSOTANG_III, 'Cấp III'),
    (KN_NHOMSOTANG_IV, 'Cấp IV'),
]

# Nhóm chiều cao
KN_NHOMCHIEUCAO_DACBIET = 1
KN_NHOMCHIEUCAO_I = 2
KN_NHOMCHIEUCAO_II = 3
KN_NHOMCHIEUCAO_III = 4
KN_NHOMCHIEUCAO_IV = 5
KN_NHOMCHIEUCAO_CHOICES = [
    (KN_NHOMCHIEUCAO_DACBIET, 'Đặc biệt'),
    (KN_NHOMCHIEUCAO_I, 'Cấp I'),
    (KN_NHOMCHIEUCAO_II, 'Cấp II'),
    (KN_NHOMCHIEUCAO_III, 'Cấp III'),
    (KN_NHOMCHIEUCAO_IV, 'Cấp IV'),
]

### Bảng Địa danh dân cư
# Đối tượng Địa danh dân cư
DD_ = 'DA02'
DD_CHOICES = [
    (DD_, DD_),
]

# Danh từ chung
DD_DANHTUCHUNG_AP = 1
DD_DANHTUCHUNG_BAN = 2
DD_DANHTUCHUNG_BUON = 3
DD_DANHTUCHUNG_CHOM = 4
DD_DANHTUCHUNG_KHUDANCU = 5
DD_DANHTUCHUNG_KHUTAPTHE = 6
DD_DANHTUCHUNG_KHUDOTHI = 7
DD_DANHTUCHUNG_LANG = 8
DD_DANHTUCHUNG_LUNG = 9
DD_DANHTUCHUNG_PLEI = 10
DD_DANHTUCHUNG_TODANPHO = 11
DD_DANHTUCHUNG_TRAI = 12
DD_DANHTUCHUNG_XOM = 13
DD_DANHTUCHUNG_THON = 27
DD_DANHTUCHUNG_CUMDANCU = 28
DD_DANHTUCHUNG_KHOM = 29
DD_DANHTUCHUNG_KHOIPHO = 30
DD_DANHTUCHUNG_KHUPHO = 31
DD_DANHTUCHUNG_TODANCU = 32
DD_DANHTUCHUNG_CHOICES = [
    (DD_DANHTUCHUNG_AP, 'Ấp'),
    (DD_DANHTUCHUNG_BAN, 'Bản'),
    (DD_DANHTUCHUNG_BUON, 'Buôn'),
    (DD_DANHTUCHUNG_CHOM, 'Chòm'),
    (DD_DANHTUCHUNG_KHUDANCU, 'Khu dân cư'),
    (DD_DANHTUCHUNG_KHUTAPTHE, 'Khu tập thể'),
    (DD_DANHTUCHUNG_KHUDOTHI, 'Khu đô thị'),
    (DD_DANHTUCHUNG_LANG, 'Làng'),
    (DD_DANHTUCHUNG_LUNG, 'Lũng'),
    (DD_DANHTUCHUNG_PLEI, 'Plei'),
    (DD_DANHTUCHUNG_TODANPHO, 'Tổ dân phố'),
    (DD_DANHTUCHUNG_TRAI, 'Trại'),
    (DD_DANHTUCHUNG_XOM, 'Xóm'),
    (DD_DANHTUCHUNG_THON, 'Thôn'),
    (DD_DANHTUCHUNG_CUMDANCU, 'Cụm dân cư'),
    (DD_DANHTUCHUNG_KHOM, 'Khóm'),
    (DD_DANHTUCHUNG_KHOIPHO, 'Khối phố'),
    (DD_DANHTUCHUNG_KHUPHO, 'Khu phố'),
    (DD_DANHTUCHUNG_TODANCU, 'Tổ dân cư'),
]

### Bảng Hạ tầng kỹ thuật khác
# Đối tượng Hạ tầng kỹ thuật khác
HTKTK_CSHOATANG = 'CR01'
HTKTK_CONGTRINHDANGXD = 'CR02'
HTKTK_CONGTRINHXULYBUN = 'CR03'
HTKTK_CONGTRINHXULYNUOCSACH = 'CR04'
HTKTK_COTDENCHIEUSANG = 'CR05'
HTKTK_HONGNUOCCHUACHAY = 'CR13'
HTKTK_MODOCLAP = 'CR14'
HTKTK_NGHIATRANG = 'CR15'
HTKTK_NGHIATRANGLIETSY = 'CR16'
HTKTK_NHAMAYNUOC = 'CR17'
HTKTK_NHATANGLE = 'CR18'
HTKTK_THAPBENUOC = 'CR19'
HTKTK_TRAMTHUPHATSONG = 'CR23'
HTKTK_CHOICES = [
    (HTKTK_CSHOATANG, 'Cơ sở hỏa táng'),
    (HTKTK_CONGTRINHDANGXD, 'Công trình đang xây dựng'),
    (HTKTK_CONGTRINHXULYBUN, 'Công trình xử lý bùn'),
    (HTKTK_CONGTRINHXULYNUOCSACH, 'Công trình xử lý nước sạch'),
    (HTKTK_COTDENCHIEUSANG, 'Cột đèn chiếu sáng'),
    (HTKTK_HONGNUOCCHUACHAY, 'Họng nước chữa cháy'),
    (HTKTK_MODOCLAP, 'Mộ độc lập'),
    (HTKTK_NGHIATRANG, 'Nghĩa trang'),
    (HTKTK_NGHIATRANGLIETSY, 'Nghĩa trang liệt sỹ'),
    (HTKTK_NHAMAYNUOC, 'Nhà máy nước'),
    (HTKTK_NHATANGLE, 'Nhà tang lễ'),
    (HTKTK_THAPBENUOC, 'Tháp nước, bể nước'),
    (HTKTK_TRAMTHUPHATSONG, 'Trạm thu phát sóng'),
]

### Bảng Trạm khí tượng thuỷ văn quốc gia
# Đối tượng Trạm khí tượng thuỷ văn quốc gia
TKTTVQG_ = 'CR20'
TKTTVQG_CHOICES = [
    (TKTTVQG_, TKTTVQG_),
]

# Loại Trạm khí tượng thuỷ văn quốc gia
TKTTVQG_LOAI_KHITUONGBEMAT = 1
TKTTVQG_LOAI_KHITUONGTRENCAO = 2
TKTTVQG_LOAI_RADATHOITIET = 3
TKTTVQG_LOAI_KHITUONGNONGNGHIEP = 4
TKTTVQG_LOAI_THUYVAN = 5
TKTTVQG_LOAI_HAIVAN = 6
TKTTVQG_LOAI_DOMUA = 7
TKTTVQG_LOAI_DINHVISET = 8
TKTTVQG_LOAI_GSBDKHIHAU = 9
TKTTVQG_LOAI_CHUYENDE = 10
TKTTVQG_LOAI_CHOICES = [
    (TKTTVQG_LOAI_KHITUONGBEMAT, 'Trạm khí tượng bề mặt'),
    (TKTTVQG_LOAI_KHITUONGTRENCAO, 'Trạm khí tượng trên cao'),
    (TKTTVQG_LOAI_RADATHOITIET, 'Trạm ra đa thời tiết'),
    (TKTTVQG_LOAI_KHITUONGNONGNGHIEP, 'Trạm khí tượng nông nghiệp'),
    (TKTTVQG_LOAI_THUYVAN, 'Trạm thủy văn'),
    (TKTTVQG_LOAI_HAIVAN, 'Trạm hải văn'),
    (TKTTVQG_LOAI_DOMUA, 'Trạm đo mưa'),
    (TKTTVQG_LOAI_DINHVISET, 'Trạm định vị sét'),
    (TKTTVQG_LOAI_GSBDKHIHAU, 'Trạm giám sát biến đổi khí hậu'),
    (TKTTVQG_LOAI_CHUYENDE, 'Trạm chuyên đề'),
]

### Bảng Trạm quan trắc môi trường
# Đối tượng Trạm quan trắc môi trường
TQTMT_ = 'CR21'
TQTMT_CHOICES = [
    (TQTMT_, TQTMT_),
]

### Bảng Trạm quan trắc tài nguyên nước
# Đối tượng Trạm quan trắc tài nguyên nước
TQTTNN_ = 'CR22'
TQTTNN_CHOICES = [
    (TQTTNN_, TQTTNN_),
]

### Bảng Đường dây tải điện
# Đối tượng Đường dây tải điện
DDTD_ = 'CR09'
DDTD_CHOICES = [
    (DDTD_, DDTD_),
]

### Bảng Cột điện
# Đối tượng Cột điện
CD_ = 'CR06'
CD_CHOICES = [
    (CD_, CD_),
]

### Bảng Đường ống dẫn
# Đối tượng Đường ống dẫn
DOD_ = 'CR11'
DOD_CHOICES = [
    (DOD_, DOD_),
]

### Loại ống dẫn
DOD_LOAI_NUOC = 1
DOD_LOAI_KHI = 2
DOD_LOAI_DAU = 3
DOD_LOAI_CHOICES = [
    (DOD_LOAI_NUOC, 'Nước'),
    (DOD_LOAI_KHI, 'Khí'),
    (DOD_LOAI_DAU, 'Dầu'),
]

### Bảng Ranh giới 
# Loại Ranh giớI
RG_LOAI_HANGRAO = 'CU01'
RG_LOAI_RGKHUCAM = 'CU02'
RG_LOAI_RGSUDUNGDAT = 'CU03'
RG_LOAI_THANHLUY = 'CU04'
RG_LOAI_TUONGVAY = 'CU05'
RG_LOAI_CHOICES = [
    (RG_LOAI_HANGRAO, 'Hàng rào'),
    (RG_LOAI_RGKHUCAM, 'Ranh giới khu cấm'),
    (RG_LOAI_RGSUDUNGDAT, 'Ranh giới sử dụng đất'),
    (RG_LOAI_THANHLUY, 'Thành lũy'),
    (RG_LOAI_TUONGVAY, 'Tường vây'),
]

### Bảng Công trình y tế
# Đối tượng Công trình y tế
CTYT_BENHVIEN = 'CP01'
CTYT_CSPHONGCHONGDICHBENH = 'CP02'
CTYT_CSYTEKHAC = 'CP03'
CTYT_NHAHOSINH = 'CP04'
CTYT_PHONGKHAM = 'CP05'
CTYT_TRAMYTE = 'CP06'
CTYT_TTDIEUDUONG = 'CP07'
CTYT_TTYTE = 'CP08'
CTYT_CHOICES = [
    (CTYT_BENHVIEN, 'Bệnh viện'),
    (CTYT_CSPHONGCHONGDICHBENH, 'Cơ sở phòng chống dịch bệnh'),
    (CTYT_CSYTEKHAC, 'Cơ sở y tế khác'),
    (CTYT_NHAHOSINH, 'Nhà hộ sinh'),
    (CTYT_PHONGKHAM, 'Phòng khám'),
    (CTYT_TRAMYTE, 'Trạm y tế'),
    (CTYT_TTDIEUDUONG, 'Trung tâm điều dưỡng'),
    (CTYT_TTYTE, 'Trung tâm y tế'),
]

# Cấp y tế
CTYT_CAPYTE_DB = 1
CTYT_CAPYTE_I = 2
CTYT_CAPYTE_II = 3
CTYT_CAPYTE_III = 4
CTYT_CAPYTE_IV = 5
CTYT_CAPYTE_CHOICES = [
    (CTYT_CAPYTE_DB, 'Hạng đặc biệt'),
    (CTYT_CAPYTE_I, 'Hạng 1'),
    (CTYT_CAPYTE_II, 'Hạng 2'),
    (CTYT_CAPYTE_III, 'Hạng 3'),
    (CTYT_CAPYTE_IV, 'Hạng 4'),
]

### Bảng Công trình giáo dục
# Đối tượng Công trình giáo dục
CTGD_TTGCTX = 'CE01'
CTGD_TTKTTHHN = 'CE02'
CTGD_TCAODANG = 'CE03'
CTGD_TDAIHOC = 'CE04'
CTGD_TDANTOCNOITRU = 'CE05'
CTGD_TDAYNGHE = 'CE06'
CTGD_TGIAODUONG = 'CE07'
CTGD_TMAMNON = 'CE08'
CTGD_TPTNHIEUCAPHOC = 'CE09'
CTGD_TPTNANGKHIEU = 'CE10'
CTGD_TTIEUHOC = 'CE11'
CTGD_TTHCS = 'CE12'
CTGD_TTHPT = 'CE13'
CTGD_CHOICES = [
    (CTGD_TTGCTX, 'Trung tâm giáo dục thường xuyên'),
    (CTGD_TTKTTHHN, 'Trung tâm kỹ thuật tổng hợp - hướng nghiệp'),
    (CTGD_TCAODANG, 'Trường cao đẳng'),
    (CTGD_TDAIHOC, 'Trường đại học'),
    (CTGD_TDANTOCNOITRU, 'Trường dân tộc nội trú'),
    (CTGD_TDAYNGHE, 'Trường dạy nghề'),
    (CTGD_TGIAODUONG, 'Trường giáo dưỡng'),
    (CTGD_TMAMNON, 'Trường mầm non'),
    (CTGD_TPTNHIEUCAPHOC, 'Trường phổ thông có nhiều cấp học'),
    (CTGD_TPTNANGKHIEU, 'Trường phổ thông năng khiếu'),
    (CTGD_TTIEUHOC, 'Trường tiểu học'),
    (CTGD_TTHCS, 'Trường trung học cơ sở'),
    (CTGD_TTHPT, 'Trường trung học phổ thông'),
]

### Bảng Công trình thể thao
# Đối tượng Công trình thể thao
CTTT_BEBOI = 'CK01'
CTTT_NHATHIDAU = 'CK02'
CTTT_SANGON = 'CK03'
CTTT_SANTHETHAO = 'CK04'
CTTT_SANVANDONG = 'CK05'
CTTT_TTTDTT = 'CK06'
CTTT_TRUONGDUABAN = 'CK07'
CTTT_CHOICES = [
    (CTTT_BEBOI, 'Bể bơi'),
    (CTTT_NHATHIDAU, 'Nhà thi đấu'),
    (CTTT_SANGON, 'Sân gôn'),
    (CTTT_SANTHETHAO, 'Sân thể thao'),
    (CTTT_SANVANDONG, 'Sân vận động'),
    (CTTT_TTTDTT, 'Trung tâm thể dục thể thao'),
    (CTTT_TRUONGDUABAN, 'Trường đua, trường bắn'),
]

### Bảng Công trình văn hoá
# Đối tượng Công trình văn hoá
CTVH_BAOTANG = 'CN01'
CTVH_CHOITHAPCAO = 'CN02'
CTVH_CONG = 'CN03'
CTVH_CTDITICH = 'CN04'
CTVH_CTVCGT = 'CN05'
CTVH_CONGVIEN = 'CN06'
CTVH_COTCO = 'CN07'
CTVH_COTDONGHO = 'CN08'
CTVH_DAIPHUNNUOC = 'CN09'
CTVH_DAITUONGNIEM = 'CN10'
CTVH_LANGTAM = 'CN11'
CTVH_LOCOT = 'CN12'
CTVH_NHAHAT = 'CN13'
CTVH_NHAVANHOA = 'CN14'
CTVH_QUANGTRUONG = 'CN15'
CTVH_RAPCHIEUPHIM = 'CN16'
CTVH_RAPXIEC = 'CN17'
CTVH_THAPCO = 'CN18'
CTVH_THUVIEN = 'CN19'
CTVH_TRIENLAM = 'CN20'
CTVH_TTHOINGHI = 'CN21'
CTVH_TUONGDAI = 'CN22'
CTVH_VUONHOA = 'CN23'
CTVH_CHOICES = [
    (CTVH_BAOTANG, 'Bảo tàng'),
    (CTVH_CHOITHAPCAO, 'Chòi cao, tháp cao'),
    (CTVH_CONG, 'Cổng'),
    (CTVH_CTDITICH, 'Công trình di tích'),
    (CTVH_CTVCGT, 'Công trình vui chơi, giải trí'),
    (CTVH_CONGVIEN, 'Công viên'),
    (CTVH_COTCO, 'Cột cờ'),
    (CTVH_COTDONGHO, 'Cột đồng hồ'),
    (CTVH_DAIPHUNNUOC, 'Đài phun nước'),
    (CTVH_DAITUONGNIEM, 'Đài tưởng niệm'),
    (CTVH_LANGTAM, 'Lăng tẩm'),
    (CTVH_LOCOT, 'Lô cốt'),
    (CTVH_NHAHAT, 'Nhà hát'),
    (CTVH_NHAVANHOA, 'Nhà văn hóa'),
    (CTVH_QUANGTRUONG, 'Quảng trường'),
    (CTVH_RAPCHIEUPHIM, 'Rạp chiếu phim'),
    (CTVH_RAPXIEC, 'Rạp xiếc'),
    (CTVH_THAPCO, 'Tháp cổ'),
    (CTVH_THUVIEN, 'Thư viện'),
    (CTVH_TRIENLAM, 'Triển lãm'),
    (CTVH_TTHOINGHI, 'Trung tâm hội nghị'),
    (CTVH_TUONGDAI, 'Tượng đài'),
    (CTVH_VUONHOA, 'Vườn hoa'),
]

# Xếp hạng di tích
CTVH_XEPHANG_QGDB = 1
CTVH_XEPHANG_QG = 2
CTVH_XEPHANG_TINH = 3
CTVH_XEPHANG_0 = 4
CTVH_XEPHANG_CHOICES = [
    (CTVH_XEPHANG_QGDB, 'Di tích cấp quốc gia đặc biệt'),
    (CTVH_XEPHANG_QG, 'Di tích cấp quốc gia'),
    (CTVH_XEPHANG_TINH, 'Di tích cấp tỉnh'),
    (CTVH_XEPHANG_0, 'Chưa xếp hạng di tích'),
]

### Bảng Công trình thương mại dịch vụ
# Đối tượng Công trình thương mại dịch vụ
CTTMDV_BAITAM = 'CL01'
CTTMDV_BUUCUC = 'CL02'
CTTMDV_BUUDIEN = 'CL03'
CTTMDV_CTDVKHAC = 'CL04'
CTTMDV_CHO = 'CL05'
CTTMDV_CUAHANG = 'CL06'
CTTMDV_BUUDIENVHXA = 'CL07'
CTTMDV_KHACHSAN = 'CL08'
CTTMDV_NGANHANG = 'CL09'
CTTMDV_NHAHANG = 'CL10'
CTTMDV_NHAKHACH = 'CL11'
CTTMDV_NHATBTT = 'CL12'
CTTMDV_SIEUTHI = 'CL13'
CTTMDV_XANGDAU = 'CL15'
CTTMDV_TTTM = 'CL16'
CTTMDV_CHOICES = [
    (CTTMDV_BAITAM, 'Bãi tắm'),
    (CTTMDV_BUUCUC, 'Bưu cục'),
    (CTTMDV_BUUDIEN, 'Bưu điện'),
    (CTTMDV_CTDVKHAC, 'Các công trình dịch vụ khác'),
    (CTTMDV_CHO, 'Chợ'),
    (CTTMDV_CUAHANG, 'Cửa hàng'),
    (CTTMDV_BUUDIENVHXA, 'Điểm bưu điện - văn hóa xã'),
    (CTTMDV_KHACHSAN, 'Khách sạn'),
    (CTTMDV_NGANHANG, 'Ngân hàng'),
    (CTTMDV_NHAHANG, 'Nhà hàng'),
    (CTTMDV_NHAKHACH, 'Nhà khách'),
    (CTTMDV_NHATBTT, 'Nhà lắp đặt thiết bị thông tin'),
    (CTTMDV_SIEUTHI, 'Siêu thị'),
    (CTTMDV_XANGDAU, 'Trạm xăng, dầu'),
    (CTTMDV_TTTM, 'Trung tâm thương mại'),
]

### Bảng Công trình tôn giáo tín ngưỡng
# Đối tượng Công trình tôn giáo tín ngưỡng
CTTGTN_CHUA = 'CM01'
CTTGTN_CSDTTG = 'CM02'
CTTGTN_CTTGKHAC = 'CM03'
CTTGTN_DEN = 'CM04'
CTTGTN_DINH = 'CM05'
CTTGTN_GACCHUONG = 'CM06'
CTTGTN_MIEU = 'CM07'
CTTGTN_NHANGUYEN = 'CM08'
CTTGTN_NHATHO = 'CM09'
CTTGTN_NIEMPHATDUONG = 'CM10'
CTTGTN_THANHDUONG = 'CM11'
CTTGTN_THANHTHAT = 'CM12'
CTTGTN_TSTCTG = 'CM13'
CTTGTN_TUDUONG = 'CM14'
CTTGTN_CHOICES = [
    (CTTGTN_CHUA, 'Chùa'),
    (CTTGTN_CSDTTG, 'Cơ sở đào tạo tôn giáo'),
    (CTTGTN_CTTGKHAC, 'Công trình tôn giáo khác'),
    (CTTGTN_DEN, 'Đền'),
    (CTTGTN_DINH, 'Đình'),
    (CTTGTN_GACCHUONG, 'Gác chuông'),
    (CTTGTN_MIEU, 'MiếU'),
    (CTTGTN_NHANGUYEN, 'Nhà nguyện'),
    (CTTGTN_NHATHO, 'Nhà thờ'),
    (CTTGTN_NIEMPHATDUONG, 'Niệm phật đường'),
    (CTTGTN_THANHDUONG, 'Thánh đường'),
    (CTTGTN_THANHTHAT, 'Thánh thất'),
    (CTTGTN_TSTCTG, 'Trụ sở của tổ chức tôn giáo'),
    (CTTGTN_TUDUONG, 'Từ đường'),
]

# Xếp hạng di tích
CTTGTN_XEPHANG_QGDB = 1
CTTGTN_XEPHANG_QG = 2
CTTGTN_XEPHANG_TINH = 3
CTTGTN_XEPHANG_0 = 4
CTTGTN_XEPHANG_CHOICES = [
    (CTTGTN_XEPHANG_QGDB, 'Di tích cấp quốc gia đặc biệt'),
    (CTTGTN_XEPHANG_QG, 'Di tích cấp quốc gia'),
    (CTTGTN_XEPHANG_TINH, 'Di tích cấp tỉnh'),
    (CTTGTN_XEPHANG_0, 'Chưa xếp hạng di tích'),
]

### Bảng Trụ sở cơ quan nhà nước
# Đối tượng Trụ sở cơ quan nhà nước
TSCQNN_CQCM = 'CV01'
TSCQNN_CQDANG = 'CV02'
TSCQNN_TOAAN = 'CV03'
TSCQNN_TSBO = 'CV04'
TSCQNN_TSCP = 'CV05'
TSCQNN_TSTCCTXH = 'CV06'
TSCQNN_TSUBNDH = 'CV07'
TSCQNN_TSUBNDT = 'CV08'
TSCQNN_TSUBNDX = 'CV09'
TSCQNN_VKS = 'CV10'
TSCQNN_CHOICES = [
    (TSCQNN_CQCM, 'Cơ quan chuyên môn'),
    (TSCQNN_CQDANG, 'Cơ quan Đảng'),
    (TSCQNN_TOAAN, 'Toà án'),
    (TSCQNN_TSBO, 'Trụ sở các Bộ'),
    (TSCQNN_TSCP, 'Trụ sở Chính Phủ'),
    (TSCQNN_TSTCCTXH, 'Trụ sở tổ chức chính trị - xã hội'),
    (TSCQNN_TSUBNDH, 'Trụ sở UBND cấp Huyện'),
    (TSCQNN_TSUBNDT, 'Trụ sở UBND cấp Tỉnh'),
    (TSCQNN_TSUBNDX, 'Trụ sở UBND cấp Xã'),
    (TSCQNN_VKS, 'Viện kiểm sát'),
]

### Bảng Công trình công nghiệp
# Đối tượng Công trình công nghiệp
CTCN_BECHUANHIENLIEU = 'CD01'
CTCN_CTTHUYDIEN = 'CD02'
CTCN_COTTHAPDIENGIO = 'CD03'
CTCN_CUAHAMLOCUAMO = 'CD04'
CTCN_GIANKHOAN = 'CD05'
CTCN_KHO = 'CD06'
CTCN_KHUKHAITHAC = 'CD07'
CTCN_LONUNG = 'CD08'
CTCN_NHAMAY = 'CD09'
CTCN_ONGKHOI = 'CD10'
CTCN_TBA = 'CD11'
CTCN_TCKHL = 'CD12'
CTCN_CHOICES = [
    (CTCN_BECHUANHIENLIEU, 'Bể chứa nhiên liệu'),
    (CTCN_CTTHUYDIEN, 'Công trình thủy điện'),
    (CTCN_COTTHAPDIENGIO, 'Cột tháp điện gió'),
    (CTCN_CUAHAMLOCUAMO, 'Cửa hầm lò của mỏ'),
    (CTCN_GIANKHOAN, 'Giàn khoan, tháp khai thác'),
    (CTCN_KHO, 'Kho'),
    (CTCN_KHUKHAITHAC, 'Khu khai thác'),
    (CTCN_LONUNG, 'Lò nung'),
    (CTCN_NHAMAY, 'Nhà máy'),
    (CTCN_ONGKHOI, 'Ống khói'),
    (CTCN_TBA, 'Trạm biến áp'),
    (CTCN_TCKHL, 'Trạm chiết khí hóa lỏng'),
]

# Loại Công trình công nghiệp
CTCN_LOAI_SXVLXD = 1
CTCN_LOAI_LKCK = 2
CTCN_LOAI_KTCBKS = 3
CTCN_LOAI_DAUKHI = 4
CTCN_LOAI_NANGLUONG = 5
CTCN_LOAI_HOACHAT = 6
CTCN_LOAI_CNTP = 7
CTCN_LOAI_CNTD = 8
CTCN_LOAI_CNCBNTHS = 9
CTCN_LOAI_CHOICES = [
    (CTCN_LOAI_SXVLXD, 'Sản xuất vật liệu xây dựng'),
    (CTCN_LOAI_LKCK, 'Luyện kim và cơ khí chế tạo'),
    (CTCN_LOAI_KTCBKS, 'Khai thác mỏ và chế biến khoáng sản'),
    (CTCN_LOAI_DAUKHI, 'Dầu khí'),
    (CTCN_LOAI_NANGLUONG, 'Năng lượng'),
    (CTCN_LOAI_HOACHAT, 'Hóa chất'),
    (CTCN_LOAI_CNTP, 'Công nghiệp thực phẩm'),
    (CTCN_LOAI_CNTD, 'Công nghiệp tiêu dùng'),
    (CTCN_LOAI_CNCBNTHS, 'Công nghiệp chế biến nông, thủy và hải sản'),
]

### Bảng Cơ sở sản xuất nông lâm nghiệp
# Đối tượng Cơ sở sản xuất nông lâm nghiệp
CSSXNLN_CSSXGC = 'CB01'
CSSXNLN_GN = 'CB02'
CSSXNLN_KNTTS = 'CB03'
CSSXNLN_LAMTRUONG = 'CB04'
CSSXNLN_NONGTRUONG = 'CB05'
CSSXNLN_RUONGMUOI = 'CB06'
CSSXNLN_TRANGTRAI = 'CB07'
CSSXNLN_CHOICES = [
    (CSSXNLN_CSSXGC, 'Cơ sở sản xuất giống cây, con'),
    (CSSXNLN_GN, 'Guồng nước'),
    (CSSXNLN_KNTTS, 'Khu nuôi trồng thủy sản'),
    (CSSXNLN_LAMTRUONG, 'Lâm trường'),
    (CSSXNLN_NONGTRUONG, 'Nông trường'),
    (CSSXNLN_RUONGMUOI, 'Ruộng muối'),
    (CSSXNLN_TRANGTRAI, 'Trang trại'),
]

### Bảng Khu chức năng đặc thù
# Đối tượng Khu chức năng đặc thù
KCNDT_KCX = 'CT01'
KCNDT_KCNC = 'CT02'
KCNDT_KCN = 'CT03'
KCNDT_KDL = 'CT04'
KCNDT_KKT = 'CT05'
KCNDT_KNCDT = 'CT06'
KCNDT_KTDTT = 'CT07'
KCNDT_CHOICES = [
    (KCNDT_KCX, 'Khu chế xuất'),
    (KCNDT_KCNC, 'Khu công nghệ cao'),
    (KCNDT_KCN, 'Khu công nghiệp'),
    (KCNDT_KDL, 'Khu du lịch'),
    (KCNDT_KKT, 'Khu kinh tế'),
    (KCNDT_KNCDT, 'Khu nghiên cứu đào tạo'),
    (KCNDT_KTDTT, 'Khu thể dục thể thao'),
]

### Bảng Công trình xử lý chát thải
# Đối tượng Công trình xử lý chát thải
CTXLCT_BCLR = 'CO01'
CTXLCT_CSXLCTNH = 'CO02'
CTXLCT_CSXLCTR = 'CO03'
CTXLCT_CSXLNT = 'CO04'
CTXLCT_KXLCT = 'CO05'
CTXLCT_TTCCR = 'CO06'
CTXLCT_CHOICES = [
    (CTXLCT_BCLR, 'Bãi chôn lấp rác'),
    (CTXLCT_CSXLCTNH, 'Cơ sở xử lý chất thải nguy hại'),
    (CTXLCT_CSXLCTR, 'Cơ sở xử lý chất thải rắn'),
    (CTXLCT_CSXLNT, 'Cơ sở xử lý nước thải'),
    (CTXLCT_KXLCT, 'Khu xử lý chất thải'),
    (CTXLCT_TTCCR, 'Trạm trung chuyển chất thải rắn'),
]

### Bảng Công trình an ninh
# Đối tượng Công trình an ninh
CTAN_DONCA = 'CC01'
CTAN_TSCA = 'CC02'
CTAN_TCT = 'CC03'
CTAN_TTPCCC = 'CC04'
CTAN_CHOICES = [
    (CTAN_DONCA, 'Đồn công an'),
    (CTAN_TSCA, 'Trụ sở công an'),
    (CTAN_TCT, 'Trại cải tạo'),
    (CTAN_TTPCCC, 'Trung tâm phòng cháy chữa cháy'),
]

### Bảng Công trình quốc phòng
# Đối tượng Công trình quốc phòng
CTQP_CUAKHAU = 'CH01'
CTQP_DOANHTRAI = 'CH02'
CTQP_TSQP = 'CH03'
CTQP_CHOICES = [
    (CTQP_CUAKHAU, 'Cửa khẩu'),
    (CTQP_DOANHTRAI, 'Doanh trại quân đội'),
    (CTQP_TSQP, 'Trụ sở quốc phòng'),
]

