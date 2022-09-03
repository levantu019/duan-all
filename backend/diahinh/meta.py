from . import models

# 1. Điểm độ cao
class DDCMeta:
    model = models.DiemDoCao
    fields = '__all__'
    geo_field = 'GM_Point'


# 2. Đường bình độ
class DBDMeta:
    model = models.DuongBinhDo
    fields = '__all__'
    geo_field = 'GM_Curve'


# 3. Chất đáy
class ChatDayMeta:
    model = models.ChatDay
    fields = '__all__'
    geo_field = 'GM_Point'


# 4. Điểm độ sâu
class DDSMeta:
    model = models.DiemDoSau
    fields = '__all__'
    geo_field = 'GM_Point'


# 5. Đường bình độ sâu
class DBDSMeta:
    model = models.DuongBinhDoSau
    fields = '__all__'
    geo_field = 'GM_Curve'


# 6. Địa hình đặc biệt đáy biển
class Surface_DHDBDBMeta:
    model = models.Surface_DiaHinhDacBietDayBien
    fields = '__all__'
    geo_field = 'GM_Surface'
class Curve_DHDBDBMeta:
    model = models.Curve_DiaHinhDacBietDayBien
    fields = '__all__'
    geo_field = 'GM_Curve'


# 7. Địa mạo
class DiaMaoMeta:
    model = models.DiaMao
    fields = '__all__'
    geo_field = 'GM_Surface'


# 8. Mô hình số độ cao gốc lớp điểm
class DEMGLPMeta:
    model = models.MoHinhSoDoCaoGocLopDiem
    fields = '__all__'
    geo_field = 'GM_Point'


# 9. Mô hình số độ cao gốc lớp đường
class DEMGLLMeta:
    model = models.MoHinhSoDoCaoGocLopDuong
    fields = '__all__'
    geo_field = 'GM_Curve'


# 10. Mô hình số độ cao gốc lớp vùng
class DEMGLAMeta:
    model = models.MoHinhSoDoCaoGocLopVung
    fields = '__all__'
    geo_field = 'GM_Surface'


# 11. Mô hình số độ cao gốc lớp vùng biển tập
class DEMDLVBTMeta:
    model = models.MoHinhSoDoCaoGocLopVungBienTap
    fields = '__all__'
    geo_field = 'GM_Surface'


# # 12. Lớp lưới tam giác bất quy tắc (TIN)
# class LTGBQTSerializer(serializers_gis.GeoModelSerializer):
#     class Meta:
#         model = LopLuoiTamGiacBatQuyTac
#         fields = '__all__'


# # 13. Lớp Raster
# class RSTSerializer(serializers_gis.GeoModelSerializer):
#     class Meta:
#         model = LopRaster
#         fields = '__all__'


# 14. Hố khoan địa chất
class HKDCMeta:
    model = models.HoKhoanDiaChat
    fields = '__all__'
    geo_field = 'GM_Point'


# 15. Số liệu hố khoan địa chất
class SLHKDCMeta:
    model = models.SoLieuHKDC
    fields = '__all__'


# 16. Mặt cắt điển hình địa chất
class MCDHMeta:
    model = models.MatCatDienHinh
    fields = '__all__'
    geo_field = 'GM_Curve'


# 17. Loại Địa chất
class LDCMeta:
    model = models.LoaiDiaChat
    fields = '__all__'
    geo_field = 'GM_Surface'