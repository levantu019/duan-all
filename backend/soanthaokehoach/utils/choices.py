# ---------------------------------------------------------
# -------------------- Soạn thảo kế hoạch --------------------------
# ---------------------------------------------------------
### Bảng Nhiệm vụ điều hành
# Kiểu NVDH
NVDH_KIEU_BTCT = 1
NVDH_KIEU_TKCN = 2
NVDH_KIEU_STVKTC = 3
NVDH_KIEU_QLCLCT = 4
NVDH_KIEU_CHOICES = [
    (NVDH_KIEU_BTCT, 'Nhiệm vụ bố trí công trình'),
    (NVDH_KIEU_TKCN, 'Nhiệm vụ tìm kiếm cứu nạn'),
    (NVDH_KIEU_STVKTC, 'Nhiệm vụ soạn thảo văn kiện tác chiến'),
    (NVDH_KIEU_QLCLCT, 'Nhiệm vụ quản lý chất lượng công trình')
]


### Bảng Nhiệm vụ bộ phận
# Trạng thái NVBP
NVBP_TT_1 = 1
NVBP_TT_2 = 2
NVBP_TT_3 = 3
NVBP_TT_CHOICES = [
    (NVBP_TT_1, 'Nhiệm vụ giao lần đầu'),
    (NVBP_TT_2, 'Nhiệm vụ đã giao và đang giám sát thực hiện'),
    (NVBP_TT_3, 'Nhiệm vụ đã kết thúc hoàn thành')
]


### Bảng Phương án vị trí
# Kiểu PAVT
PAVT_KIEU_1 = 1
PAVT_KIEU_2 = 2
PAVT_KIEU_3 = 3
PAVT_KIEU_CHOICES = [
    (PAVT_KIEU_1, 'Điểm bố trí công trình'),
    (PAVT_KIEU_2, 'Điểm xuất phát'),
    (PAVT_KIEU_3, 'Điểm đích'),
]

# Trạng thái phương án
PA_TT_1 = 1
PA_TT_2 = 2
PA_TT_3 = 3
PA_TT_4 = 4
PA_TT_CHOICES = [
    (PA_TT_1, 'Phương án mới, chưa phê duyệt'),
    (PA_TT_2, 'Phương án mới, đã phê duyệt'),
    (PA_TT_3, 'Phương án chỉnh sửa, đã phê duyệt'),
    (PA_TT_4, 'Phương án chỉnh sửa, chưa phê duyệt'),
]


### Bảng Phương án tuyến
# Kiểu phương án
PAT_KIEU_1 = 1
PAT_KIEU_2 = 2
PAT_KIEU_CHOICES = [
    (PAT_KIEU_1, 'Tuyến bố trí công trình'),
    (PAT_KIEU_2, 'Tuyến hành quân')
]


### Bảng phương án vùng
# Kiểu phương án
PAV_KIEU_1 = 1
PAV_KIEU_2 = 2
PAV_KIEU_3 = 3
PAV_KIEU_CHOICES = [
    (PAV_KIEU_1, 'Vùng bố trí công trình'),
    (PAV_KIEU_2, 'Vùng tìm kiếm'),
    (PAV_KIEU_3, 'Vùng tập kết')
]


### Bảng Phê duyệt phương án
# Trạng thái
PDPA_TT_1 = 1
PDPA_TT_2 = 2
PDPA_TT_3 = 3
PDPA_TT_CHOICES = [
    (PDPA_TT_1, 'Phê duyệt'),
    (PDPA_TT_2, 'Chỉnh sửa phương án'),
    (PDPA_TT_3, 'Bổ sung phương án')
]


### Bảng Phê duyệt chung NVBP
# Trạng thái
PDCNVBP_TT_1 = 1
PDCNVBP_TT_2 = 2
PDCNVBP_TT_3 = 3
PDCNVBP_TT_4 = 4
PDCNVBP_TT_CHOICES = [
    (PDCNVBP_TT_1, 'Phê duyệt'),
    (PDCNVBP_TT_2, 'Chỉnh sửa phương án'),
    (PDCNVBP_TT_3, 'Bổ sung phương án'),
    (PDCNVBP_TT_4, 'Kết thúc')
]