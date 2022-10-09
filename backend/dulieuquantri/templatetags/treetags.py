from django import template
from django.contrib.admin.templatetags.admin_list import results, result_list as admin_list_result_list
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType

from operator import itemgetter
from itertools import groupby

def compute_level(obj):
    level = 1
    while obj.parent:
        level += 1
        obj = obj.parent

    return level

# 
def sort_context(context):
    """
        context = [{'obj': , 'id': , 'parent': , 'level': }]
    """
    result = []
    context = sorted(context, key=itemgetter('id'))
    pass

def result_list(cl):
    app_label = cl.opts.app_label
    model_name = cl.opts.model_name

    data_results = list(results(cl))
    model = ContentType.objects.get(app_label=app_label, model=model_name).model_class()
    obj_all = model.objects.all().reverse()
    num_ele = len(list(results(cl)))
    extra_context = []

    for idx in range(num_ele):
        idx_model = num_ele - idx - 1
        if obj_all[idx_model].parent:
            parent_id = obj_all[idx_model].parent.id
        else:
            parent_id = ''
        
        # th tag
        th_tag = data_results[idx][1]
        th_tag = th_tag[:4] + 'data-column="name" ' + th_tag[4:]
        data_results[idx][1] = mark_safe(th_tag)

        extra_context.append({'obj': data_results[idx], 'id': obj_all[idx_model].id, 'parent': parent_id, 'level': compute_level(obj_all[idx_model]), 'app_label': app_label, 'model_name': model_name})
        
    # extra_context = sorted(extra_context, key=itemgetter('parent', 'id'))

    mycl = admin_list_result_list(cl)
    mycl.update({'results': extra_context})
    return mycl

register = template.Library()
register.inclusion_tag('admin/change_list_result_treetable.html')(result_list)