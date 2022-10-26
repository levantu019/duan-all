from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


models = apps.all_models
def perm_type_app(type_app=None):
    if not type_app:
        return Permission.objects.all()

    perms = []

    for item in list(apps.get_app_configs()): 
        if hasattr(item, 'type_app'):
            if item.type_app == type_app:
                for model in apps.all_models[item.name]:
                    content_type = ContentType.objects.get(app_label=item.name, model=model)
                    perms.append(Permission.objects.filter(content_type=content_type))

    return perms
