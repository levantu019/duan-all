from pyexpat import model
from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from .models import(
    NVDH,
    DiemNVDH,
    TuyenNVDH,
    VungNVDH,
    DonVi,
    NVBP,
    PhuongAnViTri,
    PhuongAnTuyen,
    PhuongAnVung,
    PheDuyetPhuongAnViTri,
    PheDuyetPhuongAnTuyen,
    PheDuyetPhuongAnVung,
    PheDuyetChungNVBP,
    GanLucLuong,
    PheDuyetPhuongAnGanLucLuong
)


# 0. Choices Soạn thảo kế hoạch
def ChoicesSTKHSerializer(choices):
    data = []
    for item in choices:
        data.append({"text": item[1], "value": item[0]})

    return data


# 1. Nhiệm vụ điều hành
class NVDHSerialiser(serializers_gis.GeoModelSerializer):
    class Meta:
        model = NVDH
        fields = '__all__'


# 2. Điểm NVDH
class DiemNVDHSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = DiemNVDH
        fields = '__all__'
        geo_field = 'geoDiem'


# 3. Tuyến NVDH
class TuyenNVDHSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = TuyenNVDH
        fields = '__all__'
        geo_field = 'geoTuyen'


# 4. Vùng NVDH
class VungNVDHSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = VungNVDH
        fields = '__all__'
        geo_field = 'geoVung'


# 5. Đơn vị
class DonViSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = DonVi
        fields = '__all__'
        geo_field = 'geoDV'


# 6. Nhiệm vụ bộ phận
class NVBPSerialiser(serializers_gis.GeoModelSerializer):
    class Meta:
        model = NVBP
        fields = '__all__'


# 7. Phương án vị trí
class PAViTriSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PhuongAnViTri
        fields = '__all__'
        geo_field = 'geoPAVT'


# 8. Phê duyệt phương án vị trí
class PDPAViTriSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PheDuyetPhuongAnViTri
        fields = '__all__'
        geo_field = 'geoCMPAVT'


# 9. Phương án tuyến
class PATuyenSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PhuongAnTuyen
        fields = '__all__'
        geo_field = 'geoPATuyen'


# 10. Phê duyệt phương án tuyến
class PDPATuyenSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PheDuyetPhuongAnTuyen
        fields = '__all__'
        geo_field = 'geoCMPATuyen'


# 11. Phương án vùng
class PAVungSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PhuongAnVung
        fields = '__all__'
        geo_field = 'geoPAVung'


# 12. Phê duyệt phương án vùng
class PDPAVungSerialiser(serializers_gis.GeoFeatureModelSerializer):
    class Meta:
        model = PheDuyetPhuongAnVung
        fields = '__all__'
        geo_field = 'geoCMPAVung'


# 13. Phê duyệt chung
class PDChungNVBPSerialiser(serializers_gis.GeoModelSerializer):
    class Meta:
        model = PheDuyetChungNVBP
        fields = '__all__'


# 14. Gán lực lượng
class GanLLSerialiser(serializers_gis.GeoModelSerializer):
    class Meta:
        model = GanLucLuong
        fields = '__all__'


# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLSerialiser(serializers_gis.GeoModelSerializer):
    class Meta:
        model = PheDuyetPhuongAnGanLucLuong
        fields = '__all__'


