from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets
from rest_framework import serializers

from . import models

class AttributeView(View):
    def post(self, request):
        name = request.POST['name']
        data_type = request.POST['data_type']
        description = request.POST['description']
        display_order = request.POST['display_order']
        entity = request.POST['entity']

        app_model = entity.split('.')
        
        try:
            is_required = True or request.POST['is_required']
        except:
            is_required = False

        try:
            new_attribute = models.Attribute(datatype=data_type, name=name, description=description, required=is_required, display_order=display_order)
            new_attribute.save()
            new_attribute.entity_ct.add(ContentType.objects.get(app_label=app_model[0], model=app_model[1]))

            messages.success(self.request, _('Add {} field successful'.format(name)))
        except Exception as e:
            messages.error(self.request, _("Can't add {} field because some error: {}".format(name, e)))
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = '__all__'

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = AttributeSerializer