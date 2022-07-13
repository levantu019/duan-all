# Generated by Django 3.2.13 on 2022-07-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diahinh', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatday',
            options={'ordering': ['id'], 'verbose_name': 'Chất đáy', 'verbose_name_plural': 'Chất đáy'},
        ),
        migrations.AlterModelOptions(
            name='diahinhdacbietdaybien',
            options={'ordering': ['id'], 'verbose_name': 'Địa hình đặc biệt đáy biển', 'verbose_name_plural': 'Địa hình đặc biệt đáy biển'},
        ),
        migrations.AlterModelOptions(
            name='diamao',
            options={'ordering': ['id'], 'verbose_name': 'Địa mạo', 'verbose_name_plural': 'Địa mạo'},
        ),
        migrations.AlterModelOptions(
            name='diemdocao',
            options={'ordering': ['id'], 'verbose_name': 'Điểm độ cao', 'verbose_name_plural': 'Điểm độ cao'},
        ),
        migrations.AlterModelOptions(
            name='diemdosau',
            options={'ordering': ['id'], 'verbose_name': 'Điểm độ sâu', 'verbose_name_plural': 'Điểm độ sâu'},
        ),
        migrations.AlterModelOptions(
            name='duongbinhdo',
            options={'ordering': ['id'], 'verbose_name': 'Đường bình độ', 'verbose_name_plural': 'Đường bình độ'},
        ),
        migrations.AlterModelOptions(
            name='duongbinhdosau',
            options={'ordering': ['id'], 'verbose_name': 'Đường bình độ sâu', 'verbose_name_plural': 'Đường bình độ sâu'},
        ),
        migrations.AlterModelOptions(
            name='hokhoandiachat',
            options={'ordering': ['id'], 'verbose_name': 'Hố khoan địa chất', 'verbose_name_plural': 'Hố khoan địa chất'},
        ),
        migrations.AlterModelOptions(
            name='loaidiachat',
            options={'ordering': ['id'], 'verbose_name': 'Loại Địa chất', 'verbose_name_plural': 'Loại Địa chất'},
        ),
        migrations.AlterModelOptions(
            name='lopluoitamgiacbatquytac',
            options={'ordering': ['id'], 'verbose_name': 'Lớp lưới tam giác bất quy tắc (TIN)', 'verbose_name_plural': 'Lớp lưới tam giác bất quy tắc (TIN)'},
        ),
        migrations.AlterModelOptions(
            name='lopraster',
            options={'ordering': ['id'], 'verbose_name': 'Lớp Raster', 'verbose_name_plural': 'Lớp Raster'},
        ),
        migrations.AlterModelOptions(
            name='matcatdienhinh',
            options={'ordering': ['id'], 'verbose_name': 'Mặt cắt điển hình địa chất', 'verbose_name_plural': 'Mặt cắt điển hình địa chất'},
        ),
        migrations.AlterModelOptions(
            name='mohinhsodocaogoclopdiem',
            options={'ordering': ['id'], 'verbose_name': 'Mô hình số độ cao gốc lớp điểm', 'verbose_name_plural': 'Mô hình số độ cao gốc lớp điểm'},
        ),
        migrations.AlterModelOptions(
            name='mohinhsodocaogoclopduong',
            options={'ordering': ['id'], 'verbose_name': 'Mô hình số độ cao gốc lớp đường', 'verbose_name_plural': 'Mô hình số độ cao gốc lớp đường'},
        ),
        migrations.AlterModelOptions(
            name='mohinhsodocaogoclopvung',
            options={'ordering': ['id'], 'verbose_name': 'Mô hình số độ cao gốc lớp vùng', 'verbose_name_plural': 'Mô hình số độ cao gốc lớp vùng'},
        ),
        migrations.AlterModelOptions(
            name='mohinhsodocaogoclopvungbientap',
            options={'ordering': ['id'], 'verbose_name': 'Mô hình số độ cao gốc lớp vùng biển tập', 'verbose_name_plural': 'Mô hình số độ cao gốc lớp vùng biển tập'},
        ),
        migrations.AlterModelOptions(
            name='solieuhkdc',
            options={'ordering': ['id'], 'verbose_name': 'Số liệu hố khoan địa chất', 'verbose_name_plural': 'Số liệu hố khoan địa chất'},
        ),
        migrations.AlterField(
            model_name='chatday',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='loaiChatDay',
            field=models.IntegerField(choices=[(1, 'Bùn'), (2, 'Cát'), (3, 'San hô'), (4, 'Đá'), (5, 'Bùn, cát'), (6, 'Cát, san hô'), (7, 'Cát, sỏi'), (8, 'Đá, san hô'), (9, 'Đá, sỏi'), (10, 'Vỏ sò, ốc'), (11, 'Loại khác')], verbose_name='Loại'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='maDoiTuong',
            field=models.CharField(choices=[('ED01', 'ED01')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='chatday',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='maDoiTuong',
            field=models.CharField(choices=[('ED04', 'Khe rãnh máng ngầm'), ('ED05', 'Núi lửa dưới biển'), ('ED06', 'Sườn đất ngầm dốc đứng')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diahinhdacbietdaybien',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='dongLucDiaMao',
            field=models.CharField(max_length=255, verbose_name='Động lực'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='ghichuDiaMao',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='maDiaMao',
            field=models.CharField(max_length=50, verbose_name='Mã địa mạo'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='motaDiaMao',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='tenDiaMao',
            field=models.CharField(max_length=255, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='diamao',
            name='tyleDiaMao',
            field=models.FloatField(verbose_name='Tỷ lệ'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='doCao',
            field=models.FloatField(verbose_name='Độ cao'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='maDoiTuong',
            field=models.CharField(choices=[('EA01', 'EA01')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diemdocao',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='doSau',
            field=models.FloatField(verbose_name='Độ sâu'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='maDoiTuong',
            field=models.CharField(choices=[('ED02', 'ED02')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diemdosau',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='doCao',
            field=models.FloatField(verbose_name='Độ cao'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='loaiDuongBinhDo',
            field=models.IntegerField(choices=[(1, 'Cơ bản'), (2, 'Nửa khoảng cao đều'), (3, 'Phụ'), (4, 'Nháp')], verbose_name='Loại đường bình độ'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='loaiKhoangCaoDeu',
            field=models.IntegerField(choices=[(1, '0,5 m'), (2, '1,0 m'), (4, '2,5 m'), (5, '5,0 m'), (6, '10,0 m')], verbose_name='Loại khoảng cao đều'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='maDoiTuong',
            field=models.CharField(choices=[('EA02', 'EA02')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='duongbinhdo',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='doSau',
            field=models.FloatField(verbose_name='Độ sâu'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='loaiDuongBinhDo',
            field=models.IntegerField(choices=[(1, 'Cơ bản'), (2, 'Nửa khoảng cao đều'), (3, 'Phụ'), (4, 'Nháp')], verbose_name='Loại đường bình độ'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='loaiKhoangCaoDeu',
            field=models.IntegerField(choices=[(1, '0,5 m'), (2, '1,0 m'), (3, '2,0 m'), (4, '2,5 m'), (5, '5,0 m'), (6, '10,0 m')], verbose_name='Loại khoảng cao đều'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='maDoiTuong',
            field=models.CharField(choices=[('ED03', 'ED03')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='duongbinhdosau',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='dosauHoKhoanDiaChat',
            field=models.FloatField(verbose_name='Độ sâu'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='ghichuHoKhoanDiaChat',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='hinhanhHoKhoanDiaChat',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Hình ảnh'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='maHoKhoanDiaChat',
            field=models.CharField(max_length=50, verbose_name='Mã hố khoan'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='motaHoKhoanDiaChat',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='hokhoandiachat',
            name='tenHoKhoanDiaChat',
            field=models.CharField(max_length=255, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='kieuDiaChatCongTrinh',
            field=models.CharField(max_length=255, verbose_name='Kiểu địa chất công trình'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='kieuThachHoc',
            field=models.CharField(max_length=255, verbose_name='Kiểu thạch học'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='kyHieu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ký hiệu'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='maLoaiDC',
            field=models.CharField(max_length=50, verbose_name='Mã loại địa chất'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='moTa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='phanHeThachHoc',
            field=models.CharField(max_length=255, verbose_name='Phân hệ thạch học'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='loaidiachat',
            name='tuoiDiaChatCongTrinh',
            field=models.FloatField(verbose_name='Tuổi địa chất công trình'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='doChinhXac',
            field=models.FloatField(verbose_name='Độ chính xác'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='lopluoitamgiacbatquytac',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='duongDanDEMRaster',
            field=models.CharField(max_length=255, verbose_name='Đường dẫn DEM'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='maDEMRaster',
            field=models.CharField(max_length=50, verbose_name='Mã DEM Raster'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='moTaDEM',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='lopraster',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='ghiChu',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='hinhAnh',
            field=models.ImageField(upload_to='images/', verbose_name='Hình ảnh'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='maMCDienHinh',
            field=models.CharField(max_length=50, verbose_name='Mã mặt cắt'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='moTa',
            field=models.CharField(max_length=500, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='ten',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='tyLeDung',
            field=models.FloatField(verbose_name='Tỷ lệ đứng'),
        ),
        migrations.AlterField(
            model_name='matcatdienhinh',
            name='tyLeNgang',
            field=models.FloatField(verbose_name='Tỷ lệ ngang'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='maDoiTuong',
            field=models.CharField(choices=[('EA01', 'Điểm độ cao'), ('ED02', 'Điểm độ sâu'), ('EE01', 'Khối điểm Lidar'), ('EE02', 'Khối điểm đo sâu'), ('EE03', 'Khối điểm')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopdiem',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='maDoiTuong',
            field=models.CharField(choices=[('EA02', 'Đường bình độ'), ('EC01', 'Bờ dốc tự nhiên'), ('EC02', 'Dòng đá'), ('EC03', 'Địa hình bậc thang'), ('EC04', 'Địa hình cắt xẻ nhân tạo'), ('EC05', 'Khe rãnh xói mòn'), ('EC06', 'Sườn đứt gãy'), ('EC07', 'Sườn sụt lở'), ('EC08', 'Vách đứng'), ('ED03', 'Đường bình độ sâu'), ('ED04', 'Khe rãnh máng ngầm'), ('ED06', 'Sườn đất ngầm dốc đứng'), ('EE04', 'Đường mô tả đặc trưng địa hình'), ('KE03', 'Đường bờ nước'), ('KE05', 'Đường mép nước')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopduong',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='maDoiTuong',
            field=models.CharField(choices=[('EE05', 'Vùng biển'), ('EE06', 'Vùng mặt nước tĩnh lặng')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvung',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='maDoiTuong',
            field=models.CharField(choices=[('EE07', 'Khu vực bị che khuất'), ('EE08', 'Phạm vi khu vực thành lập mô hình số độ cao')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='mohinhsodocaogoclopvungbientap',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='CDKNBaoHoa',
            field=models.FloatField(blank=True, null=True, verbose_name='CDKN bão hoà'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='CDKNHeSoMem',
            field=models.FloatField(blank=True, null=True, verbose_name='CDKN hệ số mềm'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='CDKNKho',
            field=models.FloatField(blank=True, null=True, verbose_name='CDKN kho'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='DoAmTuNhien',
            field=models.FloatField(blank=True, null=True, verbose_name='Độ ẩm tự nhiên'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='DoBaoHoa',
            field=models.FloatField(blank=True, null=True, verbose_name='Độ bão hoà'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='DoLoRong',
            field=models.FloatField(blank=True, null=True, verbose_name='Do lo rong'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='DungTrongMaxCat',
            field=models.FloatField(blank=True, null=True, verbose_name='Dung trong max cat'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='DungTrongMinCat',
            field=models.FloatField(blank=True, null=True, verbose_name='Dung trong min cat'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='GocNghiKho',
            field=models.FloatField(blank=True, null=True, verbose_name='Goc nghi kho'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='GocNghiUot',
            field=models.FloatField(blank=True, null=True, verbose_name='Goc nghi uot'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='HSRongLonNhat',
            field=models.FloatField(blank=True, null=True, verbose_name='Hệ số rong lớn nhất'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='HSRongNhoNhat',
            field=models.FloatField(blank=True, null=True, verbose_name='Hệ số rong nhỏ nhất'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='HeSoRong',
            field=models.FloatField(blank=True, null=True, verbose_name='Hệ số rong'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='KLRieng',
            field=models.FloatField(blank=True, null=True, verbose_name='KL riêng'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='KLTheTichKho',
            field=models.FloatField(blank=True, null=True, verbose_name='KL thể tích kho'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='KLTheTichTuNhien',
            field=models.FloatField(blank=True, null=True, verbose_name='KL thể tích tự nhiên'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='TinhCoLyDa_DoKheHo',
            field=models.FloatField(blank=True, null=True, verbose_name='Tinh co ly da do ke ho'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='TinhCoLyDa_DoRong',
            field=models.FloatField(blank=True, null=True, verbose_name='Tinh co ly da độ rộng'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='TinhCoLyDa_KLRieng',
            field=models.FloatField(blank=True, null=True, verbose_name='Tinh co ly da KL riêng'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='TinhCoLyDa_KLTTTN',
            field=models.FloatField(blank=True, null=True, verbose_name='Tinh co ly da KLTTTN'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='TinhCoLyDa_TyLeKheHo',
            field=models.FloatField(blank=True, null=True, verbose_name='Tinh co ly da tỷ lệ khe hở'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='dosauBDLaymauHKDC',
            field=models.FloatField(verbose_name='Độ sâu BD lấy mẫu'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='dosauKTLaymauHKDC',
            field=models.FloatField(verbose_name='Độ sâu KT lấy mẫu'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='lopHKDC',
            field=models.CharField(max_length=500, verbose_name='Lớp hố khoan địa chất'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='maSolieuHoKhoanDC',
            field=models.CharField(max_length=50, verbose_name='Mã số liệu'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='soHieuMau',
            field=models.CharField(max_length=500, verbose_name='Số hiệu mẫu'),
        ),
        migrations.AlterField(
            model_name='solieuhkdc',
            name='sohieuTNghiemHKDC',
            field=models.CharField(max_length=500, verbose_name='Số hiệu thí nghiệm'),
        ),
    ]
