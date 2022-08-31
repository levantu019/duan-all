from django.http import JsonResponse
from django.apps import apps
from django.shortcuts import render

from rest_framework import views, viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from nendialy.utils import JSONChoices

from .models import (
    NhomDuLieu,
    LoaiStyle,
    LopDuLieu,
    Style,
    DuLieuDaPhuongTien,
    MetaData
)

from .serializers import (
    NhomDuLieuSerialiser,
    LoaiStyleSerialiser,
    LopDuLieuSerialiser,
    StyleSerialiser,
    MultiMediaSerialiser,
    MetaDataSerialiser
)


# 
@api_view(['GET'])
@swagger_auto_schema(operation_description="Get all values of specified field")
def getValueFields(request, *args, **kwargs):
    """
        Lấy danh sách tất cả giá trị thuộc các trường chỉ định
        Sử dụng app_label và model_name
        ex: .../multimedia/value-fields/<app_label>/<model_name>?fields_name=field1&fields_name=...
    """
    try:
        app_label = kwargs['app_label']
        model_name = kwargs['model_name']
        field_default = kwargs['field_name']
        fields = request.query_params.getlist('fields_name')

        model = apps.get_model(app_label, model_name)
        value_fields = model.objects.all().values(field_default, *fields)

        return Response(data=list(value_fields), status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


# 
@api_view(['GET'])
@swagger_auto_schema(operation_description="Get app name and table name from id of table")
def getApp_Model(request, *args, **kwargs):    
    """
        Lấy tên nhóm dữ liệu của lớp dữ liệu
    """
    try:
        id_model = kwargs['id_model']

        lopDL = LopDuLieu.objects.filter(maLop=int(id_model)).first()

        if lopDL is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tenLop = lopDL.tenLop
            tenNhom = lopDL.maNhom.tenNhom
            print(tenNhom, tenLop)

            return Response(data={'app_label': tenNhom, 'model_name': tenLop}, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# 2. Loại Style
class LoaiStyleViewSet(viewsets.ModelViewSet):
    queryset = LoaiStyle.objects.all()
    serializer_class = LoaiStyleSerialiser

# 3. Lớp dữ liệu
class LopDuLieuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LopDuLieu.objects.all()
    serializer_class = LopDuLieuSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-lop')
    def choices_kieuLop(self, request):
        try:
            choices = LopDuLieu.kieuLop.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# 4. Style
class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-dinh-dang-style')
    def choices_kieuDinhDangStyle(self, request):
        try:
            choices = Style.kieuDinhDangStyle.field.choices
            data = JSONChoices.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

