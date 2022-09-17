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