from django.forms import ModelForm
from django.contrib.auth.models import Group
from django import forms
from django.core.exceptions import ValidationError

from quanlytaikhoan.utils import choices
from quanlytaikhoan.models import NhomTaiKhoan

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
class NhomTaiKhoanForm(forms.models.BaseInlineFormSet):
    # def is_valid(self):
    #     return super(NhomTaiKhoanForm, self).is_valid() and \
    #                 not any([bool(e) for e in self.errors])

    def clean_role(self,form):
        """
        """
        try:
            role = form.cleaned_data['role']
            if not role:
                raise ValidationError("Lựa chọn nhóm quyền")
        except:
            raise ValidationError("Lựa chọn nhóm quyền")


    def clean(self):
        super(NhomTaiKhoanForm, self).clean()

        for form in self.forms:
            self.clean_role(form)