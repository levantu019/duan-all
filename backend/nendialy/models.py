from django.contrib.gis.db import models

# Models

# -------------------- Nền địa lý 2000, 5000, 1000 --------------------
# Abstract
class NenDiaLy2N5N10N(models.Model):
    """
    + Abstract model
    + Fields:
        - maNhanDang (primary key)
        - phienBan
        - ngayPhienBan
        - giaTriDoChinhXacMatPhang
        - nguyenNhanThayDoi
    """
    class Meta:
        abstract = True

    # Fields
    maNhanDang = models.CharField(max_length=50, verbose_name='Mã nhận dạng', primary_key=True, db_column='manhandang')
    phienBan = models.IntegerField(verbose_name='Phiên bản', db_column='phienban')
    ngayPhienBan = models.DateTimeField(verbose_name='Ngày phiên bản', db_column='ngayphienban')
    giaTriDoChinhXacMatPhang = models.FloatField(null=True, blank=True, verbose_name='Giá trị độ chính xác mặt phẳng', db_column='giatridochinhxacmatphang')
    nguyenNhanThayDoi = models.CharField(max_length=250, null=True, blank=True, verbose_name='Nguyên nhân thay đổi', db_column='nguyennhanthaydoi')