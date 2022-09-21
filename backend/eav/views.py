from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from . import models, serializers

class AttributeView(View):
    def post(self, request):
        id = request.POST['id']
        name = request.POST['name']
        data_type = request.POST['data_type']
        description = request.POST['description']
        display_order = request.POST['display_order']
        try:
            if request.POST['is_required'] == 'on':
                is_required = True
            else:
                is_required = False
        except:
            is_required = False

        if id == '':
            entity = request.POST['entity']
            app_model = entity.split('.')

            try:
                new_attribute = models.Attribute(datatype=data_type, name=name, description=description, required=is_required, display_order=display_order)
                new_attribute.save()
                new_attribute.entity_ct.add(ContentType.objects.get(app_label=app_model[0], model=app_model[1]))

                messages.success(request, _('Add {} field successful'.format(name)))
            except Exception as e:
                messages.error(request, _("Can't add {} field because some error: {}".format(name, e)))
                
        else:
            try:
                models.Attribute.objects.filter(id=int(id)).update(datatype=data_type, name=name, description=description, required=is_required, display_order=display_order)
                messages.success(request, _('Update {} field successful'.format(name)))
            except Exception as e:
                messages.error(request, _("Can't update {} field because some error: {}".format(name, e)))
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# 
# def delete_attribute(request, id):
    # try:        
    #     delete_attr = models.Attribute.objects.get(id=id)
    #     name = delete_attr.name
    #     delete_attr.delete()
    #     messages.success(request, _('Delete {} field successful'.format(name)))
    # except Exception as e:
    #     messages.error(request, _("Can't delete field because some error: {}".format(e)))

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    # return render(request, 'admin/delete_object_protected.html')

# 
@api_view(['GET'])
def getAttrByEntity(request, *args, **kwargs):
    try:
        app_model = kwargs['app_model'].split('.')

        model_contentype = ContentType.objects.get(app_label=app_model[0], model=app_model[1])

        data = models.Attribute.objects.filter_by_entity(model_contentype)
        data = serializers.AttributeSerializer(data, many=True).data

        return Response({'data': data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)