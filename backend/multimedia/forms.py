from django import forms

from .models import (
    LopDuLieu,
    NhomDuLieu,
    DuLieuDaPhuongTien,
)

from . import models, meta
from .utils import handleString, customFields, constants, funcs
from .utils.config import ENABLE_EAV, enable_eav_cls


# 1. Nhóm dữ liệu
class NhomDuLieuForm(meta.NhomDuLieuMeta, enable_eav_cls(ENABLE_EAV.NhomDL).BASE_FORM):
    def __init__(self, *args, **kwargs):
        super(NhomDuLieuForm, self).__init__(*args, **kwargs)

        # maNhanDang
        id_html_maNhanDang = "dulieudaphuongtien_manhandang"
        self.fields["maNhanDang"].widget = forms.Select(
            attrs={
                "onchange": "getChoiceModels(this.value, '{}'".format(id_html_maNhanDang),
            },
            choices=funcs.choices_NhomDL(),
        )


# 3. Lớp dữ liệu
class LopDuLieuForm(meta.LopDuLieuMeta, enable_eav_cls(ENABLE_EAV.LopDL).BASE_FORM):
    def __init__(self, *args, **kwargs):
        super(LopDuLieuForm, self).__init__(*args, **kwargs)

        # maNhanDang
        id_html_maNhanDang = "dulieudaphuongtien_manhandang"
        self.fields["nhomDL"].widget.widget.attrs.update(
            {
                "onchange": "getChoiceModels(this.value, '{}')".format(id_html_maNhanDang),
            }
        )

        maNhanDang_init = [("", "---------")]
        self.fields["maNhanDang"].widget = forms.Select(
            attrs={
                "id": id_html_maNhanDang,
            },
            choices=maNhanDang_init,
        )


# 5. Dữ liệu đa phương tiện
class DuLieuDaPhuongTienForm(meta.MultiMediaMeta, enable_eav_cls(ENABLE_EAV.MultiMedia).BASE_FORM):
    def __init__(self, *args, **kwargs):
        super(DuLieuDaPhuongTienForm, self).__init__(*args, **kwargs)

        # maNhanDang
        new_maNhanDang = handleString.generate_MaNhanDang(models.DuLieuDaPhuongTien, constants.DL_MULTIMEDIA)

        self.fields["maNhanDang"].widget = customFields.MA_NHAN_DANG(new_maNhanDang, True)

        # maNhanDangObj
        maNhanDangObj_value = ""
        maNhanDangObj_display = "---------"
        try:
            maNhanDangObj_value = kwargs["instance"].maNhanDangObj
            maNhanDangObj_display = kwargs["instance"].maNhanDangObj
        except:
            pass

        id_html_maNhanDangObj = "dulieudaphuongtien_manhandang-obj"
        self.fields["lopDL"].widget.widget.attrs.update(
            {
                "onchange": "getValueFields(this.value, '{}', '{}')".format(id_html_maNhanDangObj, maNhanDangObj_value),
            }
        )

        maNhanDangObj_init = [(maNhanDangObj_value, maNhanDangObj_display)]
        self.fields["maNhanDangObj"].widget = forms.Select(
            attrs={"id": id_html_maNhanDangObj},
            choices=maNhanDangObj_init,
        )
