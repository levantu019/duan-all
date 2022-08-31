# ---------------------------------------------------------
# -------------------- Media --------------------------
# ---------------------------------------------------------
### Bảng Lớp dữ liệu
# Kiểu lớp
LDL_KIEU_DIEM = 1
LDL_KIEU_DUONG = 2
LDL_KIEU_VUNG = 3
LDL_KIEU_BIEUDO = 4
LDL_KIEU_HUONG = 5
LDL_KIEU_KHAC = 6
LDL_KIEU_CHOICES = [
    (LDL_KIEU_DIEM, 'Lớp điểm'),
    (LDL_KIEU_DUONG, 'Lớp đường'),
    (LDL_KIEU_VUNG, 'Lớp vùng'),
    (LDL_KIEU_BIEUDO, 'Lớp biểu đồ'),
    (LDL_KIEU_HUONG, 'Lớp hướng'),
    (LDL_KIEU_KHAC, 'Lớp khác'),
]

### Bảng Style
# Kiểu định dạng style
STYLE_KIEU_XML = 1
STYLE_KIEU_CSS = 2
STYLE_KIEU_CHOICES = [
    (STYLE_KIEU_XML, 'XML'),
    (STYLE_KIEU_CSS, 'CSS'),
]