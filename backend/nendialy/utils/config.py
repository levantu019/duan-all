from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from django.contrib import messages
from django.urls import path
from django.utils.translation import gettext_lazy as _
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from . import media
from multimedia.models import DuLieuDaPhuongTien, LopDuLieu


NENDIALY_USE_EAV = True
NENDIALY_USE_LOAD_DB = True
NENDIALY_USE_BOTH = True

BASE_FORM = BaseDynamicEntityForm
BASE_ADMIN = BaseEntityAdmin

if not NENDIALY_USE_BOTH:
    BASE_FORM = ModelForm
    BASE_ADMIN = ModelAdmin


class AdminCommon:
    class Media:
        js = media.JS_ADMIN_BASE

    if NENDIALY_USE_BOTH:
        change_list_template = "admin/button_load_data.html"

    #
    def save_model(self, request, obj, form, change):
        try:
            images = request.FILES.getlist("images")
            model_name = obj.__class__._meta.model_name
            lopDL = LopDuLieu.objects.get(maNhanDang=model_name)

            if images:
                for image in images:
                    DuLieuDaPhuongTien.objects.create(pathDuLieu=image, lopDL=lopDL, maNhanDangObj=obj.maNhanDang)

        except Exception as e:
            messages.error(request, _("Can't save image because some error: {}".format(e)))

        super().save_model(request, obj, form, change)


# 
def create_serializer(_model):
    from rest_framework_gis import serializers
    
    fields = _model._meta.fields
    geo = ''
    for field in fields:
        if hasattr(field, 'geom_type'):
            geo = field.name
            break

    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = _model
            fields = '__all__'
            if geo != '':
                geo_field = geo

    return ModelSerializer