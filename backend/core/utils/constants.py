# Các kiểu thống kê
STATISTIC_DONVI_LOAI = 'donvi_loai'
STATISTIC_DONVI_CAP = 'donvi_cap'
STATISTIC_TBKT_DVIQL = 'tbkt_dviql'
STATISTIC_TBKT_LOAI = 'tbkt_loai'
STATISTIC_TBKT_XUATXU = 'tbkt_xuatxu'
STATISTIC_TBKT_NAMSX = 'tbkt_namsx'
STATISTIC_TBKT_TTHD = 'tbkt_tthd'
STATISTIC_TBKT_PCCL = 'tbkt_pccl'
STATISTIC_TYPE = {
    "quanlydonvi_donvi": {
        "app": "quanlydonvi",
        "model": "donvi",
        "title": "Đơn vị",
        "components": [
            {
                "key": STATISTIC_DONVI_LOAI,
                "value": "loaiDonVi__ten",
                "text": "Loại đơn vị",
                "title": "đơn vị theo loại",
                "instance": None,
            },
            {
                "key": STATISTIC_DONVI_CAP,
                "value": "capDonVi__ten",
                "text": "Cấp đơn vị",
                "title": "đơn vị theo cấp",
                "instance": None,
            },
        ]
    },
    "quanlytbkt_trangbikhitai": {
        "app": "quanlytbkt",
        "model": "trangbikhitai",
        "title": "Trang bị khí tài",
        "components": [
             {
                "key": STATISTIC_TBKT_DVIQL,
                "value": "donVi__ten",
                "text": "Đơn vị quản lý",
                "title": "theo đơn vị quản lý",
                "instance": None,
            },
            {
                "key": STATISTIC_TBKT_LOAI,
                "value": "loaiTrangBiKhiTai__ten",
                "text": "Loại trang bị",
                "title": "theo loại trang bị",
                "instance": None,
            },
            {
                "key": STATISTIC_TBKT_XUATXU,
                "value": "xuatXu__ten",
                "text": "Xuất xứ",
                "title": "theo xuất xứ",
                "instance": None,
            },
            {
                "key": STATISTIC_TBKT_NAMSX,
                "value": "namSanXuat",
                "text": "Năm sản xuất",
                "title": "theo năm sản xuất",
                "instance": None,
            },
            {
                "key": STATISTIC_TBKT_TTHD,
                "value": "tinhTrang__ten",
                "text": "Tình trạng hoạt động",
                "title": "theo tình trạng hoạt động",
                "instance": None,
            },
            {
                "key": STATISTIC_TBKT_PCCL,
                "value": "phanCapChatLuong__ten",
                "text": "Phân cấp chất lượng",
                "title": "theo phân cấp chất lượng",
                "instance": None,
            },
        ]
    }
}