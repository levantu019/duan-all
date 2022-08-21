# Generated by Django 3.2.13 on 2022-08-21 02:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiemDoDacQuocGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('soHieuDiem', models.CharField(max_length=50, verbose_name='Số hiệu điểm')),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('maDoiTuong', models.CharField(choices=[('BC01', 'Điểm độ cao quốc gia'), ('BC02', 'Điểm tọa độ quốc gia'), ('BC03', 'Điểm tọa độ và độ cao quốc gia'), ('BC04', 'Điểm trọng lực quốc gia')], max_length=50, verbose_name='Mã đối tượng')),
                ('doCao', models.FloatField(verbose_name='Độ cao')),
                ('loaiMoc', models.IntegerField(choices=[(1, 'Chôn'), (2, 'Gắn'), (3, 'Khác')], verbose_name='Loại mốc')),
                ('loaiCapHang', models.IntegerField(choices=[(1, 'Cấp cơ sở'), (2, 'Cấp 0'), (3, 'Hạng I'), (4, 'Hạng II'), (5, 'Hạng III')], verbose_name='Loại cấp hạng')),
            ],
            options={
                'verbose_name': 'Điểm đo đạc quốc gia',
                'verbose_name_plural': 'Điểm đo đạc quốc gia',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DiemGocDoDacQuocGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('soHieuDiem', models.CharField(max_length=50, verbose_name='Số hiệu điểm')),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('maDoiTuong', models.CharField(choices=[('BA01', 'Điểm gốc độ cao quốc gia'), ('BA02', 'Điểm gốc toạ độ quốc gia'), ('BA03', 'Điểm gốc trọng lực quốc gia')], max_length=50, verbose_name='Mã đối tượng')),
                ('doCao', models.FloatField(verbose_name='Độ cao')),
            ],
            options={
                'verbose_name': 'Điểm gốc đo đạc quốc gia',
                'verbose_name_plural': 'Điểm gốc đo đạc quốc gia',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TramDinhViVeTinhQuocGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50, verbose_name='Mã nhận dạng')),
                ('phienBan', models.IntegerField(verbose_name='Phiên bản')),
                ('ngayPhienBan', models.DateTimeField(verbose_name='Ngày phiên bản')),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng')),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi')),
                ('soHieuDiem', models.CharField(max_length=50, verbose_name='Số hiệu điểm')),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4756)),
                ('maDoiTuong', models.CharField(choices=[('BD02', 'BD02')], max_length=50, verbose_name='Mã đối tượng')),
                ('ten', models.CharField(max_length=255, verbose_name='Tên')),
                ('loaiTramDinhViVeTinh', models.IntegerField(choices=[(1, 'Trạm tham chiếu cơ sở hoạt động liên tục'), (2, 'Trạm tham chiếu hoạt động liên tục')], verbose_name='Loại')),
            ],
            options={
                'verbose_name': 'Trạm định vị vệ tinh quốc gia',
                'verbose_name_plural': 'Trạm định vị vệ tinh quốc gia',
                'ordering': ['id'],
            },
        ),
    ]
