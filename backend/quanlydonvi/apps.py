from django.apps import AppConfig


class QuanlydonviConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quanlydonvi'

    verbose_name = "Quản lý đơn vị"
    verbose_name_plural = "Quản lý đơn vị"

    construct_tree = [
        {
            "type": "group",
            "text": "Danh mục dùng chung",
            "models": ["LoaiDonVi", "CapDonVi"]
        },
        {
            "type": "single",
            "models": ["DonVi"]
        },
        {
            "type": "extra",
            "text" : "Tuỳ chọn",
            "items": [
                {
                    "text": 'Bản đồ đơn vị',
                    "url": '/quanlydonvi/donvi/map/'
                },
            ]
        }
    ]
    
    app_icon = "fa fa-map-location"
