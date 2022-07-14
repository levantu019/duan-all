# Generated by Django 3.2.13 on 2022-07-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosododac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diemdodacquocgia',
            options={'ordering': ['id'], 'verbose_name': 'Điểm đo đạc quốc gia', 'verbose_name_plural': 'Điểm đo đạc quốc gia'},
        ),
        migrations.AlterModelOptions(
            name='diemgocdodacquocgia',
            options={'ordering': ['id'], 'verbose_name': 'Điểm gốc đo đạc quốc gia', 'verbose_name_plural': 'Điểm gốc đo đạc quốc gia'},
        ),
        migrations.AlterModelOptions(
            name='tramdinhvivetinhquocgia',
            options={'ordering': ['id'], 'verbose_name': 'Trạm định vị vệ tinh quốc gia', 'verbose_name_plural': 'Trạm định vị vệ tinh quốc gia'},
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='doCao',
            field=models.FloatField(verbose_name='Độ cao'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='loaiCapHang',
            field=models.IntegerField(choices=[(1, 'Cấp cơ sở'), (2, 'Cấp 0'), (3, 'Hạng I'), (4, 'Hạng II'), (5, 'Hạng III')], verbose_name='Loại cấp hạng'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='loaiMoc',
            field=models.IntegerField(choices=[(1, 'Chôn'), (2, 'Gắn'), (3, 'Khác')], verbose_name='Loại mốc'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='maDoiTuong',
            field=models.CharField(choices=[('BC01', 'Điểm độ cao quốc gia'), ('BC02', 'Điểm tọa độ quốc gia'), ('BC03', 'Điểm tọa độ và độ cao quốc gia'), ('BC04', 'Điểm trọng lực quốc gia')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemdodacquocgia',
            name='soHieuDiem',
            field=models.CharField(max_length=50, verbose_name='Số hiệu điểm'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='doCao',
            field=models.FloatField(verbose_name='Độ cao'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='maDoiTuong',
            field=models.CharField(choices=[('BA01', 'Điểm gốc độ cao quốc gia'), ('BA02', 'Điểm gốc toạ độ quốc gia'), ('BA03', 'Điểm gốc trọng lực quốc gia')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='diemgocdodacquocgia',
            name='soHieuDiem',
            field=models.CharField(max_length=50, verbose_name='Số hiệu điểm'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='giaTriDoChinhXacMatPhang',
            field=models.FloatField(blank=True, null=True, verbose_name='Giá trị độ chính xác mặt phẳng'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='loaiTramDinhViVeTinh',
            field=models.IntegerField(choices=[(1, 'Trạm tham chiếu cơ sở hoạt động liên tục'), (2, 'Trạm tham chiếu hoạt động liên tục')], verbose_name='Loại'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='maDoiTuong',
            field=models.CharField(choices=[('BD02', 'BD02')], max_length=50, verbose_name='Mã đối tượng'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='maNhanDang',
            field=models.CharField(max_length=50, verbose_name='Mã nhận dạng'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='ngayPhienBan',
            field=models.DateTimeField(verbose_name='Ngày phiên bản'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='nguyenNhanThayDoi',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nguyên nhân thay đổi'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='phienBan',
            field=models.IntegerField(verbose_name='Phiên bản'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='soHieuDiem',
            field=models.CharField(max_length=50, verbose_name='Số hiệu điểm'),
        ),
        migrations.AlterField(
            model_name='tramdinhvivetinhquocgia',
            name='ten',
            field=models.CharField(max_length=255, verbose_name='Tên'),
        ),
    ]