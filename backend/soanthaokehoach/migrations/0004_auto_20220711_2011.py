# Generated by Django 3.2.13 on 2022-07-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soanthaokehoach', '0003_auto_20220630_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diemnvdh',
            name='tenDiem',
            field=models.CharField(max_length=100, verbose_name='Tên điểm'),
        ),
        migrations.AlterField(
            model_name='nvdh',
            name='kieuNVDH',
            field=models.IntegerField(choices=[(1, 'Nhiệm vụ bố trí công trình'), (2, 'Nhiệm vụ tìm kiếm cứu nạn'), (3, 'Nhiệm vụ soạn thảo văn kiện tác chiến'), (4, 'Nhiệm vụ quản lý chất lượng công trình')], verbose_name='Kiểu NVDH'),
        ),
    ]
