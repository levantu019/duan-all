### Bảng Group
OPTIONAL = 6
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


# Giới tính
GT_NAM = 'nam'
GT_NU = 'nu'
GT_KHAC = 'khac'
GT_CHOICES = [
    (GT_NAM, 'Nam'),
    (GT_NU, 'Nu'),
    (GT_KHAC, 'Khác'),
]