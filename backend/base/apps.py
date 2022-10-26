from django.contrib.admin.apps import AdminConfig

class BaseConfig(AdminConfig):
    default_site = 'base.admin.MyAdminSite'

    type_app = 'config'
