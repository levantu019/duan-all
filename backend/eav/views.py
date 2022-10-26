from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from drf_yasg.utils import swagger_auto_schema

from . import models, serializers
from jwtauth.permissions import IsSuperUser

class AttributeView(View):
    """
    API create custom field
    """
    swagger_schema = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsSuperUser]

    def post(self, request):
        name = request.POST['name']
        data_type = request.POST['data_type']
        description = request.POST['description']
        entity = request.POST['entity']
        app_model = entity.split('.')

        try:
            if request.POST['is_required'] == 'on':
                is_required = True
            else:
                is_required = False
        except:
            is_required = False


        try:
            contenttype_model = ContentType.objects.get(app_label=app_model[0], model=app_model[1])
            new_attribute = models.Attribute(datatype=data_type, name=name, description=description, required=is_required)
            new_attribute.save()
            new_attribute.entity_ct.add(contenttype_model)

            messages.success(request, _('Add {} field successful'.format(name)))
        except Exception as e:
            messages.error(request, _("Can't add {} field because some error: {}".format(name, e)))
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# 
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsSuperUser])
@swagger_auto_schema(auto_schema=None)
def getAttrByEntity(request, *args, **kwargs):
    try:
        app_model = kwargs['app_model'].split('.')

        model_contentype = ContentType.objects.get(app_label=app_model[0], model=app_model[1])

        data = models.Attribute.objects.filter_by_entity(model_contentype)
        data = serializers.AttributeSerializer(data, many=True).data

        return Response({'data': data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)