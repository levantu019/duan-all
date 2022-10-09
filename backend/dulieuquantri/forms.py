from django.forms import ModelForm
from django.contrib.auth.models import Group
from django import forms

from quanlytaikhoan.utils import choices

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    roles = forms.ChoiceField(choices=choices.GROUP_LEVEL_CHOICES, label='Nhóm quyền có sẵn', required=False, 
        help_text='Tuỳ chọn các nhóm được xây dựng sẵn'
    )

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)


# 
