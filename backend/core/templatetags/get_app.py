from django import template

register = template.Library()

@register.simple_tag
def get_app_by_type(menu_list, type_app):
    """
        Django trả về danh sách app và model dạng [{'name': , 'app_type': , ..., 'models': []}]
        Thực hiện lấy ra các app có type chỉ định
    """
    result = []
    for item in menu_list:
        if "app_type" in item.keys():
            if item["app_type"] == type_app:
                result.append(item)

    return result


@register.simple_tag
def exclude_app_by_type(menu_list, *types):
    """
        Django trả về danh sách app và model dạng [{'name': , 'app_type': , ..., 'models': []}]
        Thực hiện loại bỏ các app có type chỉ định
    """
    result = []
    for item in menu_list:
        if "app_type" in item.keys():
            for type in types:
                if item["app_type"] != type:
                    result.append(item)

    return result


def get_model_in_app(name, models):
    """
        Sử dụng name (tên model) truy xuất thông tin model trong models
        models là danh sách các model (kèm thông tin) được lấy ra từ app
        Ví dụ: models = [{
            'name': 'Vùng Biển',
            'object_name': 'VungBien',
            ...
        }]
        Thì giá trị trả về là 1 item trong models
    """
    for item in models:
        if name == item['object_name']:
            return item
    
    return None


@register.simple_tag
def reconstruct_app(app):
    """
        Tái cấu trúc dữ liệu app trả về
        Ex: 
        app = {
            'name': 'Biên giới địa giới',
            'type_app': 'nendialy',
            ...,
            'models': [...]
        }
        pattern =   [
                        {
                            "type": "group",
                            "text": "Danh mục dùng chung",
                            "models": ["XuatXu", "LoaiTrangBiKhiTai", "TinhTrang", "PhanCapChatLuong"]
                        },
                        {
                            "type": "single",
                            "models": ["TrangBiKhiTai", "DuLieuDaPhuongTien"]
                        },
                        {
                            "type": "extra",
                            "text" : "Tuỳ chọn",
                            "items": [
                                {
                                    "text": Bản đồ,
                                    "url": ...
                                },
                                ...
                            ]
                        }
                    ]
        type:
            group: các model thuộc 1 nhóm có tên text
            single: nhóm các model không thuộc nhóm
            extra: định nghĩa một số tuỳ chọn mở rộng
    """
    pattern = app["construct_tree"]
    if pattern is None:
        return app

    import copy

    re_app = copy.deepcopy(app)
    app_models = re_app.pop('models')

    for idx, val in enumerate(pattern):
        if "models" in val:
            name_models = val["models"]
            models = []

            for name_model in name_models:
                model = get_model_in_app(name_model, app_models)
                if model is not None:
                    models.append(model)

            pattern[idx]["models"] = models
        elif "items" in val:
            pattern[idx]["items"] = val["items"]
        else:
            pattern[idx].update({"models": None})

    re_app.update({"construct_tree": pattern})

    return re_app
