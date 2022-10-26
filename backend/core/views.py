from django.db.models import Sum, Count, F
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, permission_classes, api_view, authentication_classes
from drf_yasg.utils import swagger_auto_schema

from jwtauth.permissions import (
    IsSuperUser,
    IsAdminData,
)
from .utils import constants



@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated,])
@swagger_auto_schema(auto_schema=None)
def NotifyDetail(request, *args, **kwargs):
    """
        Trả về giá trị trường thongBao của bản ghi được chọn
    """
    id = kwargs.get('id')
    app_model = kwargs.get('app_model')
    model_name = kwargs.get('model_name')
    model = ContentType.objects.get(app_label=app_model, model=model_name).model_class()

    return Response({'data': model.objects.get(maNhanDang=id).thongBao})


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsSuperUser|IsAdminData])
@swagger_auto_schema(auto_schema=None)
def NotifyUpdate(request, *args, **kwargs):
    """ 
        Cập nhật giá trị trường thông báo của bản ghi được chọn
    """
    id = kwargs.get('id')
    detail = kwargs.get('detail')
    app_model = kwargs.get('app_model')
    model_name = kwargs.get('model_name')
    model = ContentType.objects.get(app_label=app_model, model=model_name).model_class()
    item = get_object_or_404(model.objects.all(), pk=id)

    if item:
        model.objects.filter(pk=id).update(thongBao=detail)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# funtions
def convert_dict(dict):
    """
        {'a': 'x', 'b':2} ---> {'x': 2}
    """
    return {dict.get(list(dict)[0]) : dict.get(list(dict)[1])}


def calculate_data_statistic(type, model, user):
    """
        Trả về dữ liệu thống kê cho model theo type
        Ví dụ: type=loaiDonVi, moel=DonVi --> Thống kê đơn vị theo loại đơn vị
        Kết quả: [{'text': None, 'count': 1}, {'text': 'Đào tạo', 'count': 1}, {'text': 'Chiến đấu', 'count': 2}]
        Hàm này hiện tại chỉ áp dụng đối với model DonVi và TrangBiKhiTai

        Thống kê đơn vị thì tất cả tài khoản đều có thể xem
        Thống kê trang bị chỉ superadmin mới xem toàn bộ, các tài khoản khác thuộc đơn vị nào thì xem đơn vị đó
    """
    from quanlydonvi.models import DonVi
    from quanlytbkt.models import TrangBiKhiTai

    if model == DonVi or (user.is_superuser and model == TrangBiKhiTai):
        data = (model.objects.annotate(text=F(type)).values('text').annotate(value=Count('maNhanDang'))).order_by()
    else:
        data = (model.objects.filter(donVi=user.donVi).annotate(text=F(type)).values('text').annotate(value=Count('maNhanDang'))).order_by()

    result = {}
    for item in data:
        result.update(convert_dict(item))

    return result

# API statistic
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
@swagger_auto_schema(auto_schema=None)
def StatisticInitComponents(request, *args, **kwargs):
    """
        Khởi tạo các kiểu thống kê
    """
    return Response({'data': constants.STATISTIC_TYPE}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
@swagger_auto_schema(auto_schema=None)
def DataStatistic(request, *args, **kwargs):
    """
        Trả về dữ liệu cho từng loại thống kê
    """
    try:
        app_name = kwargs.pop('app')
        model_name = kwargs.get('model')
        type_statistic = kwargs.get('type')
        model = ContentType.objects.get(app_label=app_name, model=model_name).model_class()

        data = calculate_data_statistic(type_statistic, model, request.user)

        return Response({'data': data}, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
