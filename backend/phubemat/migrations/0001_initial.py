# Generated by Django 3.2.13 on 2022-06-21 07:11

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
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HA01', 'HA01')], max_length=50)),
                ('thucVat', models.IntegerField(choices=[(1, 'Có thực vật che phủ'), (2, 'Không có thực vật che phủ')])),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BeMatKhuDanCu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HA02', 'HA02')], max_length=50)),
                ('thucVat', models.IntegerField(choices=[(1, 'Có thực vật che phủ'), (2, 'Không có thực vật che phủ')])),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CayDocLap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('HE03', 'Cây độc lập'), ('HE04', 'Cụm cây độc lập')], max_length=50)),
                ('tenCay', models.CharField(max_length=255)),
                ('chieuCao', models.FloatField()),
                ('GM_Point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DatTrong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HC01', 'HC01')], max_length=50)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NuocMat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HD01', 'HD01')], max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RanhGioiPhuBeMat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('maDoiTuong', models.CharField(choices=[('HG01', 'HG01')], max_length=50)),
                ('loaiRanhGioiPhuBeMat', models.IntegerField(choices=[(1, 'Thực vật'), (2, 'Khác'), (3, 'Ranh giới khu bảo tồn thiên nhiên')])),
                ('GM_Curve', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4756)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ThucVatDayBien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maNhanDang', models.CharField(max_length=50)),
                ('phienBan', models.IntegerField()),
                ('ngayPhienBan', models.DateTimeField()),
                ('giaTriDoChinhXacMatPhang', models.FloatField(blank=True, null=True)),
                ('nguyenNhanThayDoi', models.CharField(blank=True, max_length=250, null=True)),
                ('GM_Surface', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('maDoiTuong', models.CharField(choices=[('HK01', 'Cỏ biển'), ('HK02', 'Rong, tảo'), ('HK03', 'Thực vật khác')], max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]