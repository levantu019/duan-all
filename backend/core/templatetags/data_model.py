from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import F

register = template.Library()

@register.simple_tag
def data_all(app_label, model_name):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()

    return model.objects.all()

@register.simple_tag
def data_fields(app_label, model_name, *fields):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()

    return model.objects.values(*fields)

@register.simple_tag
def data_obj(app_label, model_name, pk=None):
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()

    if pk:
        return model.objects.get(pk=pk)
    return None
    
# @register.simple_tag
# def extract_data_field(full_data, field):
#     """
#         Trả về tất cả các giá trị có trong trường field
#     """
#     result = full_data.annotate(data_field=F(field)).values("")

#     for item in full_data:
#         result.append(getattr(item, "maNhanDang"))

#     return result