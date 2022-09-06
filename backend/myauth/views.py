from rest_framework.decorators import api_view

from django.contrib import admin
from django import forms
from django.http import HttpResponse

from . import admin as my_admin
from . import models

def update_form(request, *args, **kwargs):
    try:
        class CustomForm(my_admin.TestModelAdminForm):
            maTinh = forms.IntegerField(required=False, label='Mã tỉnh')
            model = models.TestModel

        class CustomAdmin(my_admin.TestModelAdmin):
            form = CustomForm

        admin.site.unregister(models.TestModel)
        admin.site.register(models.TestModel, CustomAdmin)

        return HttpResponse('ok')
    except Exception as e:
        return HttpResponse('Error: ', e)
