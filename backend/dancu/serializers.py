from rest_framework import serializers as serializers
from rest_framework_gis import serializers as serializers_gis


from .models import (
    KhuDanCu,
    Nha,
    CongTrinhPhuTro,
    KhoiNha,
    DiaDanhDanCu,
    HaTangKyThuatKhac,
    TramKhiTuongThuyVanQuocGia,
    TramQuanTracMoiTruong,
    TramQuanTracTaiNguyenNuoc,
    DuongDayTaiDien,
    CotDien,
    DuongOngDan,
    RanhGioi,
    CongTrinhYTe,
    CongTrinhGiaoDuc,
    CongTrinhTheThao,
    CongTrinhVanHoa,
    CongTrinhThuongMaiDichVu,
    CongTrinhTonGiaoTinNguong,
    TruSoCoQuanNhaNuoc,
    CongTrinhCongNghiep,
    CoSoSanXuatNongLamNghiep,
    KhuChucNangDacThu,
    CongTrinhXuLyChatThai,
    CongTrinhAnNinh,
    CongTrinhQuocPhong
)


# 1.Khu dân cư
class KDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = KhuDanCu
        fields = '__all__'


# 2. Nhà
class NSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = Nha
        fields = '__all__'


# 3. Công trình phụ trợ
class CTPTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhPhuTro
        fields = '__all__'


# 4. Khối nhà
class KNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = KhoiNha
        fields = '__all__'


# 5. Địa danh dân cư
class DDDCSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DiaDanhDanCu
        fields = '__all__'


# 6. Hạ tầng kỹ thuật khác
class HTKTKSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = HaTangKyThuatKhac
        fields = '__all__'


# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TramKhiTuongThuyVanQuocGia
        fields = '__all__'


# 8. Trạm quan trắc môi trường
class TQTMTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TramQuanTracMoiTruong
        fields = '__all__'


# 9. Trạm quan trắc tài nguyên nước
class TQTTNNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TramQuanTracTaiNguyenNuoc
        fields = '__all__'


# 10. Đường dây tải điện
class DDTDSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongDayTaiDien
        fields = '__all__'


# 11. Cột điện
class COTDIENSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CotDien
        fields = '__all__'


# 12. Đường ống dẫn
class DODSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = DuongOngDan
        fields = '__all__'


# 13. Ranh giới
class RGSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = RanhGioi
        fields = '__all__'


# 14. Công trình y tế
class CTYTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhYTe
        fields = '__all__'


# 15. Công trình giáo dục
class CTGDSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhGiaoDuc
        fields = '__all__'


# 16. Công trình thể thao
class CTTTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhTheThao
        fields = '__all__'


# 17. Công trình văn hoá
class CTVHSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhVanHoa
        fields = '__all__'


# 18. Công trình thương mại dịch vụ
class CTTMDVSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhThuongMaiDichVu
        fields = '__all__'


# 19. Công trình tôn giáo tín ngưỡng
class CTTGTNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhTonGiaoTinNguong
        fields = '__all__'


# 20. Trụ sở cơ quan nhà nước
class TSCQNNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = TruSoCoQuanNhaNuoc
        fields = '__all__'


# 21. Công trình công nghiệp
class CTCNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhCongNghiep
        fields = '__all__'


# 22. Cơ sở sản xuất nông lâm nghiệp
class CSSXNLNSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CoSoSanXuatNongLamNghiep
        fields = '__all__'


# 23. Khu chức năng đặc thù
class KCNDTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = KhuChucNangDacThu
        fields = '__all__'


# 24. Công trình xử lý chát thải
class CTXLCTSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhXuLyChatThai
        fields = '__all__'


# 25. Công trình an ninh
class CTANSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhAnNinh
        fields = '__all__'

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['GM_Point'] = {
    #         "geometry": ret['GM_Point'],
    #         "srs": CongTrinhAnNinh.objects.last().GM_Point.crs.srid
    #     }
    #     # ret['GM_Point'] = {**ret['GM_Point'], "crs": CongTrinhAnNinh.objects.first().GM_Point.crs.srid}

        
    #     return ret

    # def create(self, validated_data):
    #     ctan = CongTrinhAnNinh(**validated_data)
    #     ctan.set_GM_Point(GEOSGeometry(validated_data['GM_Point']))
    #     ctan.save()
    #     print(ctan.GM_Point.crs.srid)
    #     return ctan

    # def to_internal_value(self, data):
    #     data['GM_Point'] = data['GM_Point']["geometry"]
    #     return super().to_internal_value(data)


# 26. Công trình quốc phòng
class CTQPSerializer(serializers_gis.GeoModelSerializer):
    class Meta:
        model = CongTrinhQuocPhong
        fields = '__all__'


