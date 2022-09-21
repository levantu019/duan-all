from django.http import JsonResponse
from django.apps import apps
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from rest_framework import views, viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from drf_yasg.utils import swagger_auto_schema

from nendialy.utils import jsonData

from . import models, serializers

# 
@api_view(['GET'])
@swagger_auto_schema(operation_description="Get all values of specified field", auto_schema=None)
def getValueFields(request, *args, **kwargs):
    """
        Lấy danh sách tất cả giá trị thuộc các trường chỉ định
        Sử dụng app_label và model_name
        ex: .../multi-media/value-fields/<app_label>/<model_name>?fields_name=field1&fields_name=...
    """
    try:
        app_label = kwargs.get('app_label')
        model_name = kwargs.get('model_name')
        field_default = kwargs.get('field_name')
        fields = request.query_params.getlist('fields_name')

        model = apps.get_model(app_label, model_name)
        value_fields = model.objects.all().values(field_default, *fields)

        return Response(data=list(value_fields), status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data=e, status=status.HTTP_404_NOT_FOUND)


# 
@api_view(['GET'])
@swagger_auto_schema(operation_description="Get app name and table name from id of table", auto_schema=None)
def getApp_Model(request, *args, **kwargs):    
    """
        Lấy tên nhóm dữ liệu của lớp dữ liệu
    """
    try:
        id_model = kwargs.get('id_model')

        lopDL = models.LopDuLieu.objects.get(maNhanDang=id_model)

        if lopDL is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tenLop = id_model
            tenNhom = lopDL.nhomDL.maNhanDang

            return Response(data={'app_label': tenNhom, 'model_name': tenLop}, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

# 
class GetModelName(viewsets.ViewSet):
    """
        API get model name from app name
    """
    swagger_schema = None

    def list(self, request):
        data = [{'name': item.model, 'label': item.name} for item in ContentType.objects.all()]
        return Response(data=data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk=None):
        if pk:
            app = models.NhomDuLieu.objects.get(maNhanDang=pk)
            model_inApp = [{'name': item.model, 'label': item.model_class()._meta.verbose_name} for item in ContentType.objects.filter(app_label=pk)]
            model_added = [{'name': item.maNhanDang, 'label': item.tenHienThiLop} for item in models.LopDuLieu.objects.filter(nhomDL=app)]
            data = []

            for item in model_inApp:
                if item not in model_added:
                    data.append(item)

            return Response(data=data, status=status.HTTP_200_OK)


# 1. Nhóm dữ liệu
class NhomDuLieuViewSet(viewsets.ModelViewSet):
    queryset = models.NhomDuLieu.objects.all()
    serializer_class = serializers.NhomDuLieuSerialiser

# 2. Loại Style
class LoaiStyleViewSet(viewsets.ModelViewSet):
    queryset = models.LoaiStyle.objects.all()
    serializer_class = serializers.LoaiStyleSerialiser

# 3. Lớp dữ liệu
class LopDuLieuViewSet(viewsets.ModelViewSet):
    queryset = models.LopDuLieu.objects.all()
    serializer_class = serializers.LopDuLieuSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-lop')
    def choices_kieuLop(self, request):
        try:
            choices = models.LopDuLieu.kieuLop.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# 4. Style
class StyleViewSet(viewsets.ModelViewSet):
    queryset = models.Style.objects.all()
    serializer_class = serializers.StyleSerialiser

    @action(methods=['get'], detail=False, url_path='kieu-dinh-dang-style')
    def choices_kieuDinhDangStyle(self, request):
        try:
            choices = models.Style.kieuDinhDangStyle.field.choices
            data = jsonData.choices_to_json(choices)
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

