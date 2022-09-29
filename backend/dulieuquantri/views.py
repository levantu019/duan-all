from django.db.models import Sum, F
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, permission_classes, api_view, authentication_classes
from drf_yasg.utils import swagger_auto_schema

from jwtauth.permissions import (
    IsSuperUser,
    IsAdminData,
)
from .utils import jsonData, choices

from . import models, serializers


# 1. Loại đơn vị

# 2. Cấp đơn vị

# 3. Đơn vị
class DonViViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DonVi.objects.all()
    serializer_class = serializers.DonViSerializer
    
# 4. Loại trang bị khí tài
class LoaiTrangBiKhiTaiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LoaiTrangBiKhiTai.objects.all()
    serializer_class = serializers.LoaiTBKTSerializer

# 5. Xuất xứ

# 6. Tình trạng trang bị

# 7. Biên chế trang bị

# 8. Phụ kiện thiết bị


# funtions
def convert_dict(dict):
    """
        {'a': 'x', 'b':2} ---> {'x': 2}
    """
    return {dict.get(list(dict)[0]) : dict.get(list(dict)[1])}

# API other
# 
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsSuperUser|IsAdminData])
@swagger_auto_schema(auto_schema=None)
def statistic_value(request, *args, **kwargs):
    """
        Thống kê số lượng trang bị khí tài hóa học theo loại 
    """
    try:
        type = kwargs.get('type')
        value = kwargs.get('value')
        app_model = kwargs.get('app_model').split('.')
        model = ContentType.objects.get(app_label=app_model[0], model=app_model[1]).model_class()

        # Name of field name
        field_name = ''
        if model.__name__ == 'ThietBiKhiTai':
            field_name = 'tenPhuKien'
        elif model.__name__ == 'BienCheTrangBi':
            field_name = 'tenTrangBi'
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if type == 'loai':
            loaiTBKT = models.LoaiTrangBiKhiTai.objects.get(maNhanDang=value)
            statistic_type = model.objects.filter(loaiTrangBiKhiTai=loaiTBKT).values(field_name).annotate(count=Sum('soLuong'))
            
            # if len(statistic_type) == 0:
                # statistic_type = models.BienCheTrangBi.objects.filter(loaiTrangBi=loaiTBKT).values('tenTrangBi').annotate(count=Sum('soLuong'))
        elif type == 'xuatxu':
            xuatxu = models.XuatXu.objects.get(maNhanDang=value)
            statistic_type = model.objects.filter(xuatXu=xuatxu).values(field_name).annotate(count=Sum('soLuong'))
        elif type == 'pccl':
            statistic_type = model.objects.filter(phanCapChatLuong=value).values(field_name).annotate(count=Sum('soLuong'))
        elif type == 'donvi':
            donvi = models.DonVi.objects.get(maNhanDang=value)
            if model is models.BienCheTrangBi:
                statistic_type = model.objects.filter(donVi=donvi).values(field_name).annotate(count=Sum('soLuong'))
            else:
                bienCheTB = models.BienCheTrangBi.objects.filter(donVi=donvi)
                statistic_type = model.objects.filter(bienCheTB__in=bienCheTB).values(field_name).annotate(count=Sum('soLuong'))
        elif type == 'tinhtrang':
            tinhtrang = models.TinhTrangTrangBi.objects.get(maNhanDang=value)
            statistic_type = model.objects.filter(tinhTrangTrangBi=tinhtrang).values(field_name).annotate(count=Sum('soLuong'))

        data = {}
        for item in statistic_type:
            data.update(convert_dict(item))

        return Response({'data': data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'data': e}, status=status.HTTP_404_NOT_FOUND)

# 
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsSuperUser|IsAdminData])
@swagger_auto_schema(auto_schema=None)
def statistic_type(request, *args, **kwargs):
    """
        Danh sách các giá trị của mỗi kiểu thống kê
        Ví dụ thống kê thoại laoij trang bị thì lấy danh sách tất cả các loại trang bị
    """
    try:
        type = kwargs.get('type')
        if type == 'loai':
            data = models.LoaiTrangBiKhiTai.objects.annotate(text=F('tenLoaiTrangBi')).annotate(value=F('maNhanDang')).values('value', 'text')
        elif type == 'xuatxu':
            data = models.XuatXu.objects.annotate(text=F('tenXuatXu')).annotate(value=F('maNhanDang')).values('value', 'text')
        elif type == 'pccl':
            data = jsonData.choices_to_json(choices.BCTB_PCCL_CHOICES)
        elif type == 'donvi':
            data = models.DonVi.objects.annotate(text=F('tenDonVi')).annotate(value=F('maNhanDang')).values('value', 'text')
        elif type == 'tinhtrang':
            data = models.TinhTrangTrangBi.objects.annotate(text=F('tenTinhTrangTB')).annotate(value=F('maNhanDang')).values('value', 'text')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response({'data': data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

