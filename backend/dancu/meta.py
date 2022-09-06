from . import models

# 1.Khu dân cư
class KDCMeta:
    class Meta:
        model = models.KhuDanCu
        fields = '__all__'
        geo_field = 'GM_Surface'

# 2. Nhà
class Surface_NMeta:
    class Meta:
        model = models.Surface_Nha
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_NMeta:
    class Meta:
        model = models.Point_Nha
        fields = '__all__'
        geo_field = 'GM_Point'

# 3. Công trình phụ trợ
class Surface_CTPTMeta:
    class Meta:
        model = models.Surface_CongTrinhPhuTro
        fields = '__all__'
        geo_field = 'GM_Surface'
class Curve_CTPTMeta:
    class Meta:
        model = models.Curve_CongTrinhPhuTro
        fields = '__all__'
        geo_field = 'GM_Curve'

# 4. Khối nhà
class KhoiNhaMeta:
    class Meta:
        model = models.KhoiNha
        fields = '__all__'
        geo_field = 'GM_Surface'

# 5. Địa danh dân cư
class DDDCMeta:
    class Meta:
        model = models.DiaDanhDanCu
        fields = '__all__'
        geo_field = 'GM_Point'

# 6. Hạ tầng kỹ thuật khác
class Surface_HTKTKMeta:
    class Meta:
        model = models.Surface_HaTangKyThuatKhac
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_HTKTKMeta:
    class Meta:
        model = models.Point_HaTangKyThuatKhac
        fields = '__all__'
        geo_field = 'GM_Point'

# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGMeta:
    class Meta:
        model = models.TramKhiTuongThuyVanQuocGia
        fields = '__all__'
        geo_field = 'GM_Surface'

# 8. Trạm quan trắc môi trường
class TQTMTMeta:
    class Meta:
        model = models.TramQuanTracMoiTruong
        fields = '__all__'
        geo_field = 'GM_Surface'

# 9. Trạm quan trắc tài nguyên nước
class TQTTNNMeta:
    class Meta:
        model = models.TramQuanTracTaiNguyenNuoc
        fields = '__all__'
        geo_field = 'GM_Surface'

# 10. Đường dây tải điện
class DDTDMeta:
    class Meta:
        model = models.DuongDayTaiDien
        fields = '__all__'
        geo_field = 'GM_Curve'

# 11. Cột điện
class CotDienMeta:
    class Meta:
        model = models.CotDien
        fields = '__all__'
        geo_field = 'GM_Point'

# 12. Đường ống dẫn
class DODMeta:
    class Meta:
        model = models.DuongOngDan
        fields = '__all__'
        geo_field = 'GM_Curve'

# 13. Ranh giới
class RanhGioiMeta:
    class Meta:
        model = models.RanhGioi
        fields = '__all__'
        geo_field = 'GM_Curve'

# 14. Công trình y tế
class Surface_CTYTMeta:
    class Meta:
        model = models.Surface_CongTrinhYTe
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTYTMeta:
    class Meta:
        model = models.Point_CongTrinhYTe
        fields = '__all__'
        geo_field = 'GM_Point'

# 15. Công trình giáo dục
class Surface_CTGDMeta:
    class Meta:
        model = models.Surface_CongTrinhGiaoDuc
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTGDMeta:
    class Meta:
        model = models.Point_CongTrinhGiaoDuc
        fields = '__all__'
        geo_field = 'GM_Point'

# 16. Công trình thể thao
class Surface_CTTTMeta:
    class Meta:
        model = models.Surface_CongTrinhTheThao
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTTTMeta:
    class Meta:
        model = models.Point_CongTrinhTheThao
        fields = '__all__'
        geo_field = 'GM_Point'

# 17. Công trình văn hoá
class Surface_CTVHMeta:
    class Meta:
        model = models.Surface_CongTrinhVanHoa
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTVHMeta:
    class Meta:
        model = models.Point_CongTrinhVanHoa
        fields = '__all__'
        geo_field = 'GM_Point'

# 18. Công trình thương mại dịch vụ
class Surface_CTTMDVMeta:
    class Meta:
        model = models.Surface_CongTrinhThuongMaiDichVu
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTTMDVMeta:
    class Meta:
        model = models.Point_CongTrinhThuongMaiDichVu
        fields = '__all__'
        geo_field = 'GM_Point'

# 19. Công trình tôn giáo tín ngưỡng
class Surface_CTTGTNMeta:
    class Meta:
        model = models.Surface_CongTrinhTonGiaoTinNguong
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTTGTNMeta:
    class Meta:
        model = models.Point_CongTrinhTonGiaoTinNguong
        fields = '__all__'
        geo_field = 'GM_Point'

# 20. Trụ sở cơ quan nhà nước
class Surface_TSCQNNMeta:
    class Meta:
        model = models.Surface_TruSoCoQuanNhaNuoc
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_TSCQNNMeta:
    class Meta:
        model = models.Point_TruSoCoQuanNhaNuoc
        fields = '__all__'
        geo_field = 'GM_Point'

# 21. Công trình công nghiệp
class Surface_CTCNMeta:
    class Meta:
        model = models.Surface_CongTrinhCongNghiep
        fields = '__all__'
        geo_field = 'GM_Surface'
class Curve_CTCNMeta:
    class Meta:
        model = models.Curve_CongTrinhCongNghiep
        fields = '__all__'
        geo_field = 'GM_Curve'
class Point_CTCNMeta:
    class Meta:
        model = models.Point_CongTrinhCongNghiep
        fields = '__all__'
        geo_field = 'GM_Point'

# 22. Cơ sở sản xuất nông lâm nghiệp
class Surface_CSSXNLNMeta:
    class Meta:
        model = models.Surface_CoSoSanXuatNongLamNghiep
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CSSXNLNMeta:
    class Meta:
        model = models.Point_CoSoSanXuatNongLamNghiep
        fields = '__all__'
        geo_field = 'GM_Point'

# 23. Khu chức năng đặc thù
class KCNDTMeta:
    class Meta:
        model = models.KhuChucNangDacThu
        fields = '__all__'
        geo_field = 'GM_Surface'

# 24. Công trình xử lý chất thải
class Surface_CTXLCTMeta:
    class Meta:
        model = models.Surface_CongTrinhXuLyChatThai
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTXLCTMeta:
    class Meta:
        model = models.Point_CongTrinhXuLyChatThai
        fields = '__all__'
        geo_field = 'GM_Point'

# 25. Công trình an ninh
class Surface_CTANMeta:
    class Meta:
        model = models.Surface_CongTrinhAnNinh
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTANMeta:
    class Meta:
        model = models.Point_CongTrinhAnNinh
        fields = '__all__'
        geo_field = 'GM_Point'

# 26. Công trình quốc phòng
class Surface_CTQPMeta:
    class Meta:
        model = models.Surface_CongTrinhQuocPhong
        fields = '__all__'
        geo_field = 'GM_Surface'
class Point_CTQPMeta:
    class Meta:
        model = models.Point_CongTrinhQuocPhong
        fields = '__all__'
        geo_field = 'GM_Point'
