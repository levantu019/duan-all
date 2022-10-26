from django.apps import AppConfig


class QuanlytbktConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quanlytbkt'

    verbose_name = "Quản lý trang bị khí tài"
    verbose_name_plural = "Quản lý trang bị khí tài"

    construct_tree = [
        {
            "type": "group",
            "text": "Danh mục dùng chung",
            "models": ["XuatXu", "LoaiTrangBiKhiTai", "TinhTrang", "PhanCapChatLuong"]
        },
        {
            "type": "single",
            "models": ["TrangBiKhiTai", "DuLieuDaPhuongTien"]
        }
    ]
    
    app_icon = "fa fa-screwdriver-wrench"
