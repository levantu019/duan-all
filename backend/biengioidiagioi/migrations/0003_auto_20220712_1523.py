# Generated by Django 3.2.13 on 2022-07-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biengioidiagioi', '0002_alter_vungbien_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diaphanhanhchinhtrenbien',
            options={'ordering': ['id'], 'verbose_name': 'Địa phận hành chính trên biển', 'verbose_name_plural': 'Địa phận hành chính trên biển'},
        ),
        migrations.AlterModelOptions(
            name='duongranhgioihanhchinhtrenbien',
            options={'ordering': ['id'], 'verbose_name': 'Đường ranh giới hành chính trên biển', 'verbose_name_plural': 'Đường ranh giới hành chính trên biển'},
        ),
        migrations.AlterModelOptions(
            name='vungbien',
            options={'ordering': ['id'], 'verbose_name': 'Vùng biển', 'verbose_name_plural': 'Vùng biển'},
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='dientich',
            field=models.FloatField(blank=True, null=True, verbose_name='Diện tích'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='maDoiTuong',
            field=models.CharField(choices=[('AE01', 'Địa phận hành chính cấp huyện trên biển'), ('AE02', 'Địa phận hành chính cấp tỉnh trên biển'), ('AE03', 'Địa phận hành chính cấp xã trên biển')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='maDonViHanhChinh',
            field=models.CharField(max_length=20, verbose_name='Mã đơn vị hành chính'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diaphanhanhchinhtrenbien',
            name='ten',
            field=models.CharField(max_length=255, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='chieuDai',
            field=models.FloatField(verbose_name='Chiều dài'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='loaiHienTrangPhapLy',
            field=models.IntegerField(choices=[(1, 'Xác định'), (0, 'Chưa xác định')], verbose_name='Loại hiện trạng pháp lý'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='maDoiTuong',
            field=models.CharField(choices=[('AE04', 'Đường ranh giới hành chính cấp huyện trên biển'), ('AE05', 'Đường ranh giới hành chính cấp tỉnh trên biển'), ('AE05', 'Đường ranh giới hành chính cấp xã trên biển')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='duongranhgioihanhchinhtrenbien',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='dientich',
            field=models.FloatField(blank=True, null=True, verbose_name='Diện tích'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='maDoiTuong',
            field=models.CharField(choices=[('AB07', 'Lãnh hải'), ('AB11', 'Vùng nội thuỷ'), ('AB12', 'Vùng nước lịch sử'), ('AB13', 'Vùng tiếp giáp lãnh hải')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='vungbien',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
    ]
