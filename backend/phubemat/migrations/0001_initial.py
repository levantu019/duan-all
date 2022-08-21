# Generated by Django 3.2.13 on 2022-08-21 02:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeMatCongTrinh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HA01', 'HA01')], max_length=50, verbose_name='Mã đối tượng')),
                ('thucVat', models.IntegerField(choices=[(1, 'Có thực vật che phủ'), (2, 'Không có thực vật che phủ')], verbose_name='Thực vật')),
            ],
            options={
                'verbose_name': 'Bề mặt công trình',
                'verbose_name_plural': 'Bề mặt công trình',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BeMatKhuDanCu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HA02', 'HA02')], max_length=50, verbose_name='Mã đối tượng')),
                ('thucVat', models.IntegerField(choices=[(1, 'Có thực vật che phủ'), (2, 'Không có thực vật che phủ')], verbose_name='Thực vật')),
            ],
            options={
                'verbose_name': 'Bề mặt khu dân cư',
                'verbose_name_plural': 'Bề mặt khu dân cư',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CayDocLap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('maDoiTuong', models.CharField(choices=[('HE03', 'Cây độc lập'), ('HE04', 'Cụm cây độc lập')], max_length=50, verbose_name='Mã đối tượng')),
                ('tenCay', models.CharField(max_length=255, verbose_name='Tên cây')),
                ('chieuCao', models.FloatField(verbose_name='Chiều cao')),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Cây độc lập',
                'verbose_name_plural': 'Cây độc lập',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DatTrong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HC01', 'HC01')], max_length=50, verbose_name='Mã đối tượng')),
                ('ten', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên')),
            ],
            options={
                'verbose_name': 'Đất trống',
                'verbose_name_plural': 'Đất trống',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NuocMat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HD01', 'HD01')], max_length=50, verbose_name='Mã đối tượng')),
            ],
            options={
                'verbose_name': 'Nước mặt',
                'verbose_name_plural': 'Nước mặt',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RanhGioiPhuBeMat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('maDoiTuong', models.CharField(choices=[('HG01', 'HG01')], max_length=50, verbose_name='Mã đối tượng')),
                ('loaiRanhGioiPhuBeMat', models.IntegerField(choices=[(1, 'Thực vật'), (2, 'Khác'), (3, 'Ranh giới khu bảo tồn thiên nhiên')], verbose_name='Loại')),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
            ],
            options={
                'verbose_name': 'Ranh giới phủ bề mặt',
                'verbose_name_plural': 'Ranh giới phủ bề mặt',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ThucVatDayBien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HK01', 'Cỏ biển'), ('HK02', 'Rong, tảo'), ('HK03', 'Thực vật khác')], max_length=50, verbose_name='Mã đối tượng')),
            ],
            options={
                'verbose_name': 'Thực vật đáy biển',
                'verbose_name_plural': 'Thực vật đáy biển',
                'ordering': ['id'],
            },
        ),
    ]
