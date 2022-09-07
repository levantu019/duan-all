from django.contrib import admin
from django import forms
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from . import models

class TestModelAdminForm(BaseDynamicEntityForm):
    model = models.TestModel

class TestModelAdmin(BaseEntityAdmin):
    class Media:
        js = ('extra/js/popper.min.js', 'extra/js/modal.js', )
    change_list_template = "admin/add_button_change_list.html"
    form = TestModelAdminForm


# register
from django.conf import settings
from .apps import MyauthConfig as app
if settings.ENABLE_APPS[app.name]:
    admin.site.register(models.TestModel, TestModelAdmin)
