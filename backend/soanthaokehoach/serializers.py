from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis

from . import meta, models
from .utils import choices as stkh, handleString, constants

# 1. Nhiệm vụ điều hành
class NVDHSerializer(meta.NVDHMeta, serializers.ModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.NVDH, constants.NVDH)

        newIns = models.NVDH.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns

# 2. Điểm NVDH
class DiemNVDHSerializer(meta.DiemNVDHMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.DiemNVDH, constants.DIEM_NVDH)

        newIns = models.DiemNVDH.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 3. Tuyến NVDH
class TuyenNVDHSerializer(meta.TuyenNVDHMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.TuyenNVDH, constants.TUYEN_NVDH)

        newIns = models.TuyenNVDH.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 4. Vùng NVDH
class VungNVDHSerializer(meta.VungNVDHMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.VungNVDH, constants.VUNG_NVDH)

        newIns = models.VungNVDH.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 5. Đơn vị
class DonViSerializer(meta.DonViMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.DonVi, constants.DONVI)

        newIns = models.DonVi.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 6. Nhiệm vụ bộ phận
class NVBPSerializer(meta.NVBPMeta, serializers.ModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.NVBP, constants.NVBP)

        newIns = models.NVBP.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 7. Phương án vị trí
class PAViTriSerializer(meta.PAViTriMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PhuongAnViTri, constants.PA_VTRI)

        newIns = models.PhuongAnViTri.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 8. Phê duyệt phương án vị trí
class PDPAViTriSerializer(meta.PDPAViTriMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PheDuyetPhuongAnViTri, constants.PDPA_VTRI)

        newIns = models.PheDuyetPhuongAnViTri.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 9. Phương án tuyến
class PATuyenSerializer(meta.PATuyenMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PhuongAnTuyen, constants.PA_TUYEN)

        newIns = models.PhuongAnTuyen.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 10. Phê duyệt phương án tuyến
class PDPATuyenSerializer(meta.PDPATuyenMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PheDuyetPhuongAnTuyen, constants.PDPA_TUYEN)

        newIns = models.PheDuyetPhuongAnTuyen.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 11. Phương án vùng
class PAVungSerializer(meta.PAVungMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PhuongAnVung, constants.PA_VUNG)

        newIns = models.PhuongAnVung.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 12. Phê duyệt phương án vùng
class PDPAVungSerializer(meta.PDPAVungMeta, serializers_gis.GeoFeatureModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PheDuyetPhuongAnVung, constants.PDPA_VUNG)

        newIns = models.PheDuyetPhuongAnVung.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 13. Phê duyệt chung
class PDChungNVBPSerializer(meta.PDChungNVBPMeta, serializers.ModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PheDuyetChungNVBP, constants.PD_CHUNG)

        newIns = models.PheDuyetChungNVBP.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 14. Gán lực lượng
class GanLLSerializer(meta.GanLLMeta, serializers.ModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.GanLucLuong, constants.GAN_LL)

        newIns = models.GanLucLuong.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


# 15. Phê duyệt phương án gán lực lượng
class PDPAGanLLSerializer(meta.PDPAGanLLMeta, serializers.ModelSerializer):
    def create(self, validated_data):
        id = handleString.generate_MaNhanDang(models.PheDuyetPhuongAnGanLucLuong, constants.PDPA_GANLL)

        newIns = models.PheDuyetPhuongAnGanLucLuong.objects.create(maNhanDang=id, **validated_data)
        newIns.save()
        return newIns


