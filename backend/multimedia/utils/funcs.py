import os

from django.apps import apps
from django.contrib.contenttypes.models import ContentType


# 
def choices_to_json(choices):
    data = []
    for item in choices:
        data.append({"text": item[1], "value": item[0]})

    return data


# Upload to
def multimedia_upload_to(instance, filename):
    if 'image' in instance.pathDuLieu.file.content_type:
        return 'images/{}'.format(filename)

    return 'other/'


# Create choices for NhomDuLieu
def choices_NhomDL():

    """
        Lọc ra tất cả app_label (ngoại trừ 1 số mặc định của hệ thống) mà chưa được thêm vào bảng NhomDuLieu
    """
    from multimedia.models import NhomDuLieu

    app_default = ('eav', 'sessions', 'auth', 'admin', 'contenttypes',)
    app_added = [item['maNhanDang'] for item in NhomDuLieu.objects.values('maNhanDang')]
    app_own = []
    app_labels = ContentType.objects.values('app_label').distinct('app_label')

    for app_label in app_labels:
        app_label = app_label.get('app_label')
        if (app_label not in app_default) and (app_label not in app_added):
            app_verbose_name = apps.get_app_config(app_label).verbose_name
            app_own.append((app_label, app_verbose_name))

    return app_own

