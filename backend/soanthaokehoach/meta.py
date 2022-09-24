from . import models

# 1. Nhiệm vụ điều hành
class NVDHMeta:
    class Meta:
        model = models.NVDH
        fields = '__all__'
        read_only_fields = ['maNhanDang']


# 2. Điểm NVDH
class DiemNVDHMeta:
    class Meta:
        model = models.DiemNVDH
        fields = '__all__'
        geo_field = 'geoDiem'
        read_only_fields = ['maNhanDang']


# 3. Tuyến NVDH
class TuyenNVDHMeta:
    class Meta:
        model = models.TuyenNVDH
        fields = '__all__'
        geo_field = 'geoTuyen'
        read_only_fields = ['maNhanDang']


# 4. Vùng NVDH
class VungNVDHMeta:
    class Meta:
        model = models.VungNVDH
        fields = '__all__'
        geo_field = 'geoVung'
        read_only_fields = ['maNhanDang']


# 5. Đơn vị
class DonViMeta:
    class Meta:
        model = models.DonVi
        fields = '__all__'
        geo_field = 'geoDV'
        read_only_fields = ['maNhanDang']


# 6. Nhiệm vụ bộ phận
class NVBPMeta:
    class Meta:
        model = models.NVBP
        fields = '__all__'
        read_only_fields = ['maNhanDang']


# 7. Phương án vị trí
class PAViTriMeta:
    class Meta:
        model = models.PhuongAnViTri
        fields = '__all__'
        geo_field = 'geoPAVT'
        read_only_fields = ['maNhanDang']


# 8. Phê duyệt phương án vị trí
class PDPAViTriMeta:
    class Meta:
        model = models.PheDuyetPhuongAnViTri
        fields = '__all__'
        geo_field = 'geoCMPAVT'
        read_only_fields = ['maNhanDang']


# 9. Phương án tuyến
class PATuyenMeta:
    class Meta:
        model = models.PhuongAnTuyen
        fields = '__all__'
        geo_field = 'geoPATuyen'
        read_only_fields = ['maNhanDang']


# 10. Phê duyệt phương án tuyến
class PDPATuyenMeta:
    class Meta:
        model = models.PheDuyetPhuongAnTuyen
        fields = '__all__'
        geo_field = 'geoCMPATuyen'
        read_only_fields = ['maNhanDang']


# 11. Phương án vùng
class PAVungMeta:
    class Meta:
        model = models.PhuongAnVung
        fields = '__all__'
        geo_field = 'geoPAVung'
        read_only_fields = ['maNhanDang']


# 12. Phê duyệt phương án vùng
class PDPAVungMeta:
    class Meta:
        model = models.PheDuyetPhuongAnVung
        fields = '__all__'
        geo_field = 'geoCMPAVung'
        read_only_fields = ['maNhanDang']


# 13. Phê duyệt chung
class PDChungNVBPMeta:
    class Meta:
        model = models.PheDuyetChungNVBP
        fields = '__all__'
        read_only_fields = ['maNhanDang']


# 14. Gán lực lượng
class GanLLMeta:
    class Meta:
        model = models.GanLucLuong
        fields = '__all__'
        read_only_fields = ['maNhanDang']


# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLMeta:
    class Meta:
        model = models.PheDuyetPhuongAnGanLucLuong
        fields = '__all__'
        read_only_fields = ['maNhanDang']


