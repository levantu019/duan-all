# ---------------------------------------------------------
# -------------------- Dữ liệu quản trị --------------------------
# ---------------------------------------------------------
### Bảng Biên chế trang bị
# Phân cấp chất lượng
BCTB_PCCL_CHOICES = [
    (1, 'Cấp 1: Trang bị còn đồng bộ, sử dụng tốt và đang trong thời gian bảo hành'),
    (2, 'Cấp 2: Sử dụng tốt, đồng bộ, hết thời gian bảo hành'),
    (3, 'Cấp 3: Hư hỏng nhẹ, có thể tự khắc phục hoặc sửa chữa nhỏ'),
    (4, 'Cấp 4: Mất tính đồng bộ, hư hỏng nặng'),
    (5, 'Cấp 5: Hỏng hóc không có khả năng sửa chữa hoặc sữa chữa không hiệu quả'),
]

# Phân bổ trang bị
BCTB_PBTB_CHOICES = [
    (1, 'Đang sử dụng'),
    (2, 'Cất giữ kho bộ, ngành'),
    (3, 'Cất giữ kho đơn vị')
]

# Đề nghị
BCTB_DN_CHOICES = [
    (1, 'Đề nghị điều chuyển'),
    (2, 'Xin thanh xử lý tài sản'),
]


### Bảng Phụ kiện thiết bị
# Trạng thái
PKTB_TT_CHOICES = [
    (1, 'Đang sử dụng tốt'),
    (2, 'Hỏng hóc')
]


### Bảng Group
OPTIONAL = 0
ADMIN = 1
ADMIN_DATA = 2
USER_LEVEL_1 = 3
USER_LEVEL_2 = 4
USER_LEVEL_3 = 5
GROUP_LEVEL_CHOICES = [
    (OPTIONAL, 'Tuỳ chỉnh'),
    (ADMIN, 'Quản trị hệ thống (toàn quyền)'), 
    (ADMIN_DATA, 'Quản trị dữ liệu (được phép biên tập dữ liệu)'),
    (USER_LEVEL_1, 'Người dùng cấp 1 (cơ quan cấp điều hành trong soạn thảo kế hoạch)'),
    (USER_LEVEL_2, 'Người dùng cấp 2 (cơ quan cấp bộ phận trong soạn thảo kế hoạch)'),
    (USER_LEVEL_3, 'Người dùng cấp 3 (khai thác dữ liệu)')
]


import datetime
YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))