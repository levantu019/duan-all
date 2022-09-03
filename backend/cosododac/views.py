from rest_framework import viewsets, permissions, status

from .import models, serializers


# 1. Điểm gốc đo đạc quốc gia
class DGDDQGViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiemGocDoDacQuocGia.objects.all()
    serializer_class = serializers.DGDDQGSerializer
    # swagger_schema = None

    # Phải đăng nhập mới dùng được API này
    # permission_classes = [permissions.IsAuthenticated]

    # Bất kỳ người dùng nào cũng thực hiện được phương thức GET (list)
    # Các phương thức còn lại bắt buộc phải đăng nhập mới dùng được
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny]

    #     return [permissions.IsAuthenticated]


# 2. Điểm đo đạc quốc gia
class DDDQGViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DiemDoDacQuocGia.objects.all()
    serializer_class = serializers.DDDQGSerializer


# 3. Trạm định vị vệ tinh quốc gia
class TDVVTQGViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TramDinhViVeTinhQuocGia.objects.all()
    serializer_class = serializers.TDVVTQGSerializer