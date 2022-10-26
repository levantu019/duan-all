from django import template
from django.contrib.admin.templatetags.admin_list import items_for_result, result_list as admin_list_result_list, ResultList
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType

def compute_level(obj):
    level = 1
    while obj.parent:
        level += 1
        obj = obj.parent

    return level

# 
def sort_context(model):
    roots = [item.maNhanDang for item in model.objects.all() if not item.parent]
    query = '''
        with RECURSIVE cte as 
        (
            select "{pk}", {field_parent} from {db_table} where "{pk}"=%s
            union all
            select e."{pk}", e.{field_parent} from {db_table} e inner join cte on e.{field_parent}=cte."{pk}"
        )
        select * from cte;
        '''.format(db_table=model.objects.model._meta.db_table, field_parent='parent_id', pk='maNhanDang')
    
    data = []
    for item in roots:
        data.extend(list(model.objects.raw(query, [item])))

    return data

def results(cl, data):
    if cl.formset:
        for res, form in zip(data, cl.formset.forms):
            yield ResultList(form, items_for_result(cl, res, form))
    else:
        for res in data:
            yield ResultList(None, items_for_result(cl, res, None))


def tree_result_list(cl):
    app_label = cl.opts.app_label
    model_name = cl.opts.model_name
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()

    if set(cl.result_list) == set(model.objects.all()):
        data = sort_context(model)
    else:
        data = cl.result_list

    data_results = list(results(cl, data))
    num_ele = len(data_results)
    extra_context = []

    for idx in range(num_ele):
        # idx_model = num_ele - idx - 1
        if data[idx].parent:
            parent_id = data[idx].parent.maNhanDang
        else:
            parent_id = '0'
        
        # th tag
        th_tag = data_results[idx][1]
        th_tag = th_tag[:4] + 'data-column="name" ' + th_tag[4:]
        data_results[idx][1] = mark_safe(th_tag)

        extra_context.append({'obj': data_results[idx], 'id': data[idx].maNhanDang, 'parent': parent_id, 'level': compute_level(data[idx]), 'app_label': app_label, 'model_name': model_name})

    mycl = admin_list_result_list(cl)
    mycl.update({'results': extra_context})
    return mycl

register = template.Library()
register.inclusion_tag('admin/change_list_result_treetable.html')(tree_result_list)