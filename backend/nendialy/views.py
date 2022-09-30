from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.contenttypes.models import ContentType
from .utils import readDataFromDB, config

# Create your views here.
class ImportFileDataView(View):
    def post(self, request, *args, **kwargs):
        # info
        entity = request.POST.get('entity')
        app_model = entity.split('.')
        model = ContentType.objects.get(app_label=app_model[0], model=app_model[1]).model_class()

        dbms = request.POST.get('db_type')
        host = request.POST.get('host')
        port = request.POST.get('port')
        username = request.POST.get('username')
        password = request.POST.get('password')
        db_name = request.POST.get('db_name')
        table_name = request.POST.get('table_name')

        # 
        try:
            MoselSerializer = config.create_serializer(model)

            if dbms == 'postgresql':
                data = readDataFromDB.dataFromPostgres(host, port, username, password, db_name, table_name, model)
                for item in data:
                    serializer = MoselSerializer(data=item)
                    if serializer.is_valid():
                        serializer.save()
            else:
                messages.warning(request, "{} chưa được hỗ trợ".format(dbms))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))          
        except:
            messages.error(request, "Can't connect to database")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


        messages.success(request, "Dữ liệu đã được cập nhật")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))