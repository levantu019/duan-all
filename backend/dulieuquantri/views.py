from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .utils import jsonData

from . import models, serializers


# 1. Loại đơn vị

# 2. Cấp đơn vị

# 3. Đơn vị
class DonViViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DonVi.objects.all()
    serializer_class = serializers.DonViSerializer
    
# 4. Loại trang bị

# 5. Xuất xứ

# 6. Tình trạng trang bị

# 7. Biên chế trang bị

# 8. Phụ kiện thiết bị
