# Generated by Django 3.2.13 on 2022-06-21 07:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CongTrinhAnNinh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CC01', 'Đồn công an'), ('CC02', 'Trụ sở công an'), ('CC03', 'Trại cải tạo'), ('CC04', 'Trung tâm phòng cháy chữa cháy')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhCongNghiep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CD01', 'Bể chứa nhiên liệu'), ('CD02', 'Công trình thủy điện'), ('CD03', 'Cột tháp điện gió'), ('CD04', 'Cửa hầm lò của mỏ'), ('CD05', 'Giàn khoan, tháp khai thác'), ('CD06', 'Kho'), ('CD07', 'Khu khai thác'), ('CD08', 'Lò nung'), ('CD09', 'Nhà máy'), ('CD10', 'Ống khói'), ('CD11', 'Trạm biến áp'), ('CD12', 'Trạm chiết khí hóa lỏng')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('loaiCongTrinhCongNghiep', models.IntegerField(choices=[(1, 'Sản xuất vật liệu xây dựng'), (2, 'Luyện kim và cơ khí chế tạo'), (3, 'Khai thác mỏ và chế biến khoáng sản'), (4, 'Dầu khí'), (5, 'Năng lượng'), (6, 'Hóa chất'), (7, 'Công nghiệp thực phẩm'), (8, 'Công nghiệp tiêu dùng'), (9, 'Công nghiệp chế biến nông, thủy và hải sản')])),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhGiaoDuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CE01', 'Trung tâm giáo dục thường xuyên'), ('CE02', 'Trung tâm kỹ thuật tổng hợp - hướng nghiệp'), ('CE03', 'Trường cao đẳng'), ('CE04', 'Trường đại học'), ('CE05', 'Trường dân tộc nội trú'), ('CE06', 'Trường dạy nghề'), ('CE07', 'Trường giáo dưỡng'), ('CE08', 'Trường mầm non'), ('CE09', 'Trường phổ thông có nhiều cấp học'), ('CE10', 'Trường phổ thông năng khiếu'), ('CE11', 'Trường tiểu học'), ('CE12', 'Trường trung học cơ sở'), ('CE13', 'Trường trung học phổ thông')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhPhuTro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CG01', 'Bậc thềm'), ('CG02', 'Cầu thang ngoài trời'), ('CG03', 'Hành lang'), ('CG04', 'Lối xuống tầng hầm')], max_length=50)),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhQuocPhong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CH01', 'Cửa khẩu'), ('CH02', 'Doanh trại quân đội'), ('CH03', 'Trụ sở quốc phòng')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhTheThao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CK01', 'Bể bơi'), ('CK02', 'Nhà thi đấu'), ('CK03', 'Sân gôn'), ('CK04', 'Sân thể thao'), ('CK05', 'Sân vận động'), ('CK06', 'Trung tâm thể dục thể thao'), ('CK07', 'Trường đua, trường bắn')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhThuongMaiDichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CL01', 'Bãi tắm'), ('CL02', 'Bưu cục'), ('CL03', 'Bưu điện'), ('CL04', 'Các công trình dịch vụ khác'), ('CL05', 'Chợ'), ('CL06', 'Cửa hàng'), ('CL07', 'Điểm bưu điện - văn hóa xã'), ('CL08', 'Khách sạn'), ('CL09', 'Ngân hàng'), ('CL10', 'Nhà hàng'), ('CL11', 'Nhà khách'), ('CL12', 'Nhà lắp đặt thiết bị thông tin'), ('CL13', 'Siêu thị'), ('CL15', 'Trạm xăng, dầu'), ('CL16', 'Trung tâm thương mại')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhTonGiaoTinNguong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CM01', 'Chùa'), ('CM02', 'Cơ sở đào tạo tôn giáo'), ('CM03', 'Công trình tôn giáo khác'), ('CM04', 'Đền'), ('CM05', 'Đình'), ('CM06', 'Gác chuông'), ('CM07', 'MiếU'), ('CM08', 'Nhà nguyện'), ('CM09', 'Nhà thờ'), ('CM10', 'Niệm phật đường'), ('CM11', 'Thánh đường'), ('CM12', 'Thánh thất'), ('CM13', 'Trụ sở của tổ chức tôn giáo'), ('CM14', 'Từ đường')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('xepHangDiTich', models.IntegerField(choices=[(1, 'Di tích cấp quốc gia đặc biệt'), (2, 'Di tích cấp quốc gia'), (3, 'Di tích cấp tỉnh'), (4, 'Chưa xếp hạng di tích')])),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhVanHoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CN01', 'Bảo tàng'), ('CN02', 'Chòi cao, tháp cao'), ('CN03', 'Cổng'), ('CN04', 'Công trình di tích'), ('CN05', 'Công trình vui chơi, giải trí'), ('CN06', 'Công viên'), ('CN07', 'Cột cờ'), ('CN08', 'Cột đồng hồ'), ('CN09', 'Đài phun nước'), ('CN10', 'Đài tưởng niệm'), ('CN11', 'Lăng tẩm'), ('CN12', 'Lô cốt'), ('CN13', 'Nhà hát'), ('CN14', 'Nhà văn hóa'), ('CN15', 'Quảng trường'), ('CN16', 'Rạp chiếu phim'), ('CN17', 'Rạp xiếc'), ('CN18', 'Tháp cổ'), ('CN19', 'Thư viện'), ('CN20', 'Triển lãm'), ('CN21', 'Trung tâm hội nghị'), ('CN22', 'Tượng đài'), ('CN23', 'Vườn hoa')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('xepHangDiTich', models.IntegerField(choices=[(1, 'Di tích cấp quốc gia đặc biệt'), (2, 'Di tích cấp quốc gia'), (3, 'Di tích cấp tỉnh'), (4, 'Chưa xếp hạng di tích')])),
                ('chieuCao', models.FloatField(blank=True, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhXuLyChatThai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CO01', 'Bãi chôn lấp rác'), ('CO02', 'Cơ sở xử lý chất thải nguy hại'), ('CO03', 'Cơ sở xử lý chất thải rắn'), ('CO04', 'Cơ sở xử lý nước thải'), ('CO05', 'Khu xử lý chất thải'), ('CO06', 'Trạm trung chuyển chất thải rắn')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CongTrinhYTe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CP01', 'Bệnh viện'), ('CP02', 'Cơ sở phòng chống dịch bệnh'), ('CP03', 'Cơ sở y tế khác'), ('CP04', 'Nhà hộ sinh'), ('CP05', 'Phòng khám'), ('CP06', 'Trạm y tế'), ('CP07', 'Trung tâm điều dưỡng'), ('CP08', 'Trung tâm y tế')], max_length=50)),
                ('capYTe', models.IntegerField(choices=[(1, 'Hạng đặc biệt'), (2, 'Hạng 1'), (3, 'Hạng 2'), (4, 'Hạng 3'), (5, 'Hạng 4')])),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CoSoSanXuatNongLamNghiep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CB01', 'Cơ sở sản xuất giống cây, con'), ('CB02', 'Guồng nước'), ('CB03', 'Khu nuôi trồng thủy sản'), ('CB04', 'Lâm trường'), ('CB05', 'Nông trường'), ('CB06', 'Ruộng muối'), ('CB07', 'Trang trại')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CotDien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR06', 'CR06')], max_length=50)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DiaDanhDanCu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('DA02', 'DA02')], max_length=50)),
                ('danhTuChung', models.IntegerField(choices=[(1, 'Ấp'), (2, 'Bản'), (3, 'Buôn'), (4, 'Chòm'), (5, 'Khu dân cư'), (6, 'Khu tập thể'), (7, 'Khu đô thị'), (8, 'Làng'), (9, 'Lũng'), (10, 'Plei'), (11, 'Tổ dân phố'), (12, 'Trại'), (13, 'Xóm'), (27, 'Thôn'), (28, 'Cụm dân cư'), (29, 'Khóm'), (30, 'Khối phố'), (31, 'Khu phố'), (32, 'Tổ dân cư')])),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DuongDayTaiDien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR09', 'CR09')], max_length=50)),
                ('dienAp', models.FloatField()),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DuongOngDan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR11', 'CR11')], max_length=50)),
                ('loaiOngDan', models.IntegerField(choices=[(1, 'Nước'), (2, 'Khí'), (3, 'Dầu')])),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HaTangKyThuatKhac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR01', 'Cơ sở hỏa táng'), ('CR02', 'Công trình đang xây dựng'), ('CR03', 'Công trình xử lý bùn'), ('CR04', 'Công trình xử lý nước sạch'), ('CR05', 'Cột đèn chiếu sáng'), ('CR13', 'Họng nước chữa cháy'), ('CR14', 'Mộ độc lập'), ('CR15', 'Nghĩa trang'), ('CR16', 'Nghĩa trang liệt sỹ'), ('CR17', 'Nhà máy nước'), ('CR18', 'Nhà tang lễ'), ('CR19', 'Tháp nước, bể nước'), ('CR23', 'Trạm thu phát sóng')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('chieuCao', models.FloatField(blank=True, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='KhoiNha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CA01', 'CA01')], max_length=50)),
                ('nhomSoTang', models.IntegerField(choices=[(1, 'Đặc biệt'), (2, 'Cấp I'), (3, 'Cấp II'), (4, 'Cấp III'), (5, 'Cấp IV')])),
                ('nhomChieuCao', models.IntegerField(choices=[(1, 'Đặc biệt'), (2, 'Cấp I'), (3, 'Cấp II'), (4, 'Cấp III'), (5, 'Cấp IV')])),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='KhuChucNangDacThu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CT01', 'Khu chế xuất'), ('CT02', 'Khu công nghệ cao'), ('CT03', 'Khu công nghiệp'), ('CT04', 'Khu du lịch'), ('CT05', 'Khu kinh tế'), ('CT06', 'Khu nghiên cứu đào tạo'), ('CT07', 'Khu thể dục thể thao')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='KhuDanCu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CA02', 'CA02')], max_length=50)),
                ('loaiKhuDanCu', models.IntegerField(choices=[(1, 'Đô thị'), (2, 'Nông thôn')])),
                ('soDan', models.IntegerField(blank=True, null=True)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Nha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CA04', 'CA04')], max_length=50)),
                ('loaiNha', models.IntegerField(choices=[(1, 'Chung cư'), (2, 'Nhà riêng'), (3, 'An ninh, Quốc phòng'), (4, 'Cơ quan nhà nước'), (5, 'Trụ sở làm việc'), (6, 'Hỗn hợp'), (7, 'Nhà công trình công cộng'), (8, 'Nhà công trình công nghiệp'), (9, 'Nhà công trình hạ tầng kỹ thuật'), (10, 'Nhà cơ sở sản xuất nông lâm nghiệp'), (11, 'Nhà khu chức năng đặc thù'), (12, 'Nhà phụ trọ dân sinh')])),
                ('mucDoKienCo', models.IntegerField(choices=[(1, 'Kiên cố'), (2, 'Bán kiên cố'), (3, 'Không kiên cố'), (4, 'Đơn sơ')])),
                ('chieuCao', models.FloatField()),
                ('soTang', models.IntegerField()),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('diaChi', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RanhGioi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(max_length=50)),
                ('loaiRanhGioi', models.IntegerField(choices=[('CU01', 'Hàng rào'), ('CU02', 'Ranh giới khu cấm'), ('CU03', 'Ranh giới sử dụng đất'), ('CU04', 'Thành lũy'), ('CU05', 'Tường vây')])),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TramKhiTuongThuyVanQuocGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR20', 'CR20')], max_length=50)),
                ('loaiTramKhiTuongThuyVan', models.IntegerField(choices=[(1, 'Trạm khí tượng bề mặt'), (2, 'Trạm khí tượng trên cao'), (3, 'Trạm ra đa thời tiết'), (4, 'Trạm khí tượng nông nghiệp'), (5, 'Trạm thủy văn'), (6, 'Trạm hải văn'), (7, 'Trạm đo mưa'), (8, 'Trạm định vị sét'), (9, 'Trạm giám sát biến đổi khí hậu'), (10, 'Trạm chuyên đề')])),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TramQuanTracMoiTruong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR21', 'CR21')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TramQuanTracTaiNguyenNuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CR22', 'CR22')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TruSoCoQuanNhaNuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('CV01', 'Cơ quan chuyên môn'), ('CV02', 'Cơ quan Đảng'), ('CV03', 'Toà án'), ('CV04', 'Trụ sở các Bộ'), ('CV05', 'Trụ sở Chính Phủ'), ('CV06', 'Trụ sở tổ chức chính trị - xã hội'), ('CV07', 'Trụ sở UBND cấp Huyện'), ('CV08', 'Trụ sở UBND cấp Tỉnh'), ('CV09', 'Trụ sở UBND cấp Xã'), ('CV10', 'Viện kiểm sát')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
