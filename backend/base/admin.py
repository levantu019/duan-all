from django.contrib import admin
from django.apps import apps
from django.utils.text import capfirst
from django.urls import NoReverseMatch, reverse

# Register your models here.
class MyAdminSite(admin.AdminSite):
    def _build_app_dict(self, request, label=None):
        """
        Build the app dictionary. The optional `label` parameter filters models
        of a specific app.
        """
        app_dict = {}

        if label:
            models = {
                m: m_a for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label
            app_obj = apps.get_app_config(app_label)

            # extra property
            type_app = None
            construct_tree = None
            app_icon = "fa fa-database"

            if hasattr(app_obj, 'type_app'):
                type_app = app_obj.type_app

            if hasattr(app_obj, 'construct_tree'):
                construct_tree = app_obj.construct_tree

            if hasattr(app_obj, 'app_icon'):
                app_icon = app_obj.app_icon

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'object_name': model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_type': type_app,
                    "app_icon": app_icon,
                    'construct_tree': construct_tree,
                    'app_label': app_label,
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=self.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        return app_list

    def index(self, request, extra_context=None):
        user = request.user

        if extra_context is None:
            extra_context = {}

        # Model in Dashboard
        # quanlytbkt.TrangBiKhiTai
        from quanlytbkt.models import TrangBiKhiTai
        from quanlytbkt.admin import TBKTAdmin
        from django.utils.safestring import mark_safe

        app_name = "quanlytbkt"
        model_name = "trangbikhitai"
        pk = 'maNhanDang'

        list_display = ['ten', 'thaoTacNhap']
        list_display_fields = ['Tên', 'Trạng thái dữ liệu']
        list_display_fields.insert(0, 'STT')
        list_display_fields.append('Cha')
        list_display_fields.append('Thao tác')

        if user.is_superuser:
            data = TrangBiKhiTai.objects.all()
        else:
            data = TrangBiKhiTai.objects.filter(donVi=user.donVi)
        
        data = data.filter(congBo=False).values(*list_display, 'parent__ten', pk)
        row_data = []

        for idx, val in enumerate(data, start=1):    
            id = val['maNhanDang']        
            row = (len(list_display) + 2) * '<td>{}</td>'
            row = row.format(idx, *[val[i] for i in filter(lambda x: x != pk, val)])
            if user.is_superuser:
                gr_opts = """
                    <td style='width: 100px; max-width: 120px'>
                        <div class="d-flex justify-content-between">
                            <a href="/{app_name}/{model_name}/{id}/change/"><i class="fa fa-info-circle" style='color: blue;'></i></a>
                                <button onclick="confirm_modal(this)" class="btn-confirm" type="button" data-content="<a style='color:white;' href='/{app_name}/{model_name}/{id}/accept/'>Xác nhận</a>" style="border: none; color: blue; padding: 0; background-color: inherit;">
                                    <i class="fa fa-check-circle"></i>
                                </button>
                            <button type="button" data-toggle="modal" data-target="#notify-input-modal" data-app={app_name} data-model={model_name} data-id={id} style="border: none; color: blue; padding: 0; background-color: inherit;">
                                <i class="fa fa-file-signature"></i>
                            </button>
                        </div>
                    </td>
                """.format(app_name=app_name, model_name=model_name, id=id)
            else:
                gr_opts = """
                    <td>
                        <div class="d-flex justify-content-between">
                            <a href="/{app_name}/{model_name}/change/"><i class="fa fa-info-circle" style='color: blue;'></i></a>
                            <button type="button" data-toggle="modal" data-target="#notify-input-modal" data-app={app_name} data-model={model_name} data-id={id} style="border: none; color: blue; padding: 0; background-color: inherit;">
                                <i class="fa fa-bell"></i>
                            </button>
                        </div>
                    </td>
                """.format(app_name=app_name, model_name=model_name, id=id)
            
            row = row + gr_opts
            row_data.append({'info': mark_safe(row)})
            
        extra_context["data_wating_headers"] = list_display_fields
        extra_context["data_wating_rows"] = row_data
        extra_context["app_model"] = app_name
        extra_context["model_name"] = model_name
        return super(MyAdminSite, self).index(request, extra_context)