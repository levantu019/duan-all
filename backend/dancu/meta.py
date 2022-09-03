from . import models

# 1.Khu dân cư
class KDCMeta:
    model = models.KhuDanCu
    fields = '__all__'
    geo_field = 'GM_Surface'

# 2. Nhà
class Surface_NMeta:
    model = models.Surface_Nha
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_NMeta:
    model = models.Point_Nha
    fields = '__all__'
    geo_field = 'GM_Point'

# 3. Công trình phụ trợ
class Surface_CTPTMeta:
    model = models.Surface_CongTrinhPhuTro
    fields = '__all__'
    geo_field = 'GM_Surface'
class Curve_CTPTMeta:
    model = models.Curve_CongTrinhPhuTro
    fields = '__all__'
    geo_field = 'GM_Curve'

# 4. Khối nhà
class KhoiNhaMeta:
    model = models.KhoiNha
    fields = '__all__'
    geo_field = 'GM_Surface'

# 5. Địa danh dân cư
class DDDCMeta:
    model = models.DiaDanhDanCu
    fields = '__all__'
    geo_field = 'GM_Point'

# 6. Hạ tầng kỹ thuật khác
class Surface_HTKTKMeta:
    model = models.Surface_HaTangKyThuatKhac
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_HTKTKMeta:
    model = models.Point_HaTangKyThuatKhac
    fields = '__all__'
    geo_field = 'GM_Point'

# 7. Trạm khí tượng thuỷ văn quốc gia
class TKTTVQGMeta:
    model = models.TramKhiTuongThuyVanQuocGia
    fields = '__all__'
    geo_field = 'GM_Surface'

# 8. Trạm quan trắc môi trường
class TQTMTMeta:
    model = models.TramQuanTracMoiTruong
    fields = '__all__'
    geo_field = 'GM_Surface'

# 9. Trạm quan trắc tài nguyên nước
class TQTTNNMeta:
    model = models.TramQuanTracTaiNguyenNuoc
    fields = '__all__'
    geo_field = 'GM_Surface'

# 10. Đường dây tải điện
class DDTDMeta:
    model = models.DuongDayTaiDien
    fields = '__all__'
    geo_field = 'GM_Curve'

# 11. Cột điện
class CotDienMeta:
    model = models.CotDien
    fields = '__all__'
    geo_field = 'GM_Point'

# 12. Đường ống dẫn
class DODMeta:
    model = models.DuongOngDan
    fields = '__all__'
    geo_field = 'GM_Curve'

# 13. Ranh giới
class RanhGioiMeta:
    model = models.RanhGioi
    fields = '__all__'
    geo_field = 'GM_Curve'

# 14. Công trình y tế
class Surface_CTYTMeta:
    model = models.Surface_CongTrinhYTe
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTYTMeta:
    model = models.Point_CongTrinhYTe
    fields = '__all__'
    geo_field = 'GM_Point'

# 15. Công trình giáo dục
class Surface_CTGDMeta:
    model = models.Surface_CongTrinhGiaoDuc
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTGDMeta:
    model = models.Point_CongTrinhGiaoDuc
    fields = '__all__'
    geo_field = 'GM_Point'

# 16. Công trình thể thao
class Surface_CTTTMeta:
    model = models.Surface_CongTrinhTheThao
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTTTMeta:
    model = models.Point_CongTrinhTheThao
    fields = '__all__'
    geo_field = 'GM_Point'

# 17. Công trình văn hoá
class Surface_CTVHMeta:
    model = models.Surface_CongTrinhVanHoa
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTVHMeta:
    model = models.Point_CongTrinhVanHoa
    fields = '__all__'
    geo_field = 'GM_Point'

# 18. Công trình thương mại dịch vụ
class Surface_CTTMDVMeta:
    model = models.Surface_CongTrinhThuongMaiDichVu
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTTMDVMeta:
    model = models.Point_CongTrinhThuongMaiDichVu
    fields = '__all__'
    geo_field = 'GM_Point'

# 19. Công trình tôn giáo tín ngưỡng
class Surface_CTTGTNMeta:
    model = models.Surface_CongTrinhTonGiaoTinNguong
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTTGTNMeta:
    model = models.Point_CongTrinhTonGiaoTinNguong
    fields = '__all__'
    geo_field = 'GM_Point'

# 20. Trụ sở cơ quan nhà nước
class Surface_TSCQNNMeta:
    model = models.Surface_TruSoCoQuanNhaNuoc
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_TSCQNNMeta:
    model = models.Point_TruSoCoQuanNhaNuoc
    fields = '__all__'
    geo_field = 'GM_Point'

# 21. Công trình công nghiệp
class Surface_CTCNMeta:
    model = models.Surface_CongTrinhCongNghiep
    fields = '__all__'
    geo_field = 'GM_Surface'
class Curve_CTCNMeta:
    model = models.Curve_CongTrinhCongNghiep
    fields = '__all__'
    geo_field = 'GM_Curve'
class Point_CTCNMeta:
    model = models.Point_CongTrinhCongNghiep
    fields = '__all__'
    geo_field = 'GM_Point'

# 22. Cơ sở sản xuất nông lâm nghiệp
class Surface_CSSXNLNMeta:
    model = models.Surface_CoSoSanXuatNongLamNghiep
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CSSXNLNMeta:
    model = models.Point_CoSoSanXuatNongLamNghiep
    fields = '__all__'
    geo_field = 'GM_Point'

# 23. Khu chức năng đặc thù
class KCNDTMeta:
    model = models.KhuChucNangDacThu
    fields = '__all__'
    geo_field = 'GM_Surface'

# 24. Công trình xử lý chất thải
class Surface_CTXLCTMeta:
    model = models.Surface_CongTrinhXuLyChatThai
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTXLCTMeta:
    model = models.Point_CongTrinhXuLyChatThai
    fields = '__all__'
    geo_field = 'GM_Point'

# 25. Công trình an ninh
class Surface_CTANMeta:
    model = models.Surface_CongTrinhAnNinh
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTANMeta:
    model = models.Point_CongTrinhAnNinh
    fields = '__all__'
    geo_field = 'GM_Point'

# 26. Công trình quốc phòng
class Surface_CTQPMeta:
    model = models.Surface_CongTrinhQuocPhong
    fields = '__all__'
    geo_field = 'GM_Surface'
class Point_CTQPMeta:
    model = models.Point_CongTrinhQuocPhong
    fields = '__all__'
    geo_field = 'GM_Point'
