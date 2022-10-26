from django.contrib.admin import helpers, widgets
from django.contrib import messages
from django.core.exceptions import (
    FieldDoesNotExist, FieldError, PermissionDenied, ValidationError,
)
from django.utils.translation import gettext as _, ngettext
from django.contrib.admin.utils import (
    NestedObjects, construct_change_message, flatten_fieldsets,
    get_deleted_objects, lookup_needs_distinct, model_format_dict,
    model_ngettext, quote, unquote,
)

class IncorrectLookupParameters(Exception):
    pass

def changelist_view(_self, _request, extra_context=None):
        """
        The 'change list' admin view for this model.
        """
        from django.contrib.admin.views.main import ERROR_FLAG
        opts = _self.model._meta
        app_label = opts.app_label

        try:
            cl = _self.get_changelist_instance(_request)
        except IncorrectLookupParameters:
            return None

        # If the _request was POSTed, this might be a bulk action or a bulk
        # edit. Try to look up an action or confirmation first, but if this
        # isn't an action the POST will fall through to the bulk edit check,
        # below.
        action_failed = False
        selected = _request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)

        actions = _self.get_actions(_request)
        # Actions with no confirmation
        if (actions and _request.method == 'POST' and
                'index' in _request.POST and '_save' not in _request.POST):
            if selected:
                response = _self.response_action(_request, queryset=cl.get_queryset(_request))
                if response:
                    return response
                else:
                    action_failed = True
            else:
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                _self.message_user(_request, msg, messages.WARNING)
                action_failed = True

        # Actions with confirmation
        if (actions and _request.method == 'POST' and
                helpers.ACTION_CHECKBOX_NAME in _request.POST and
                'index' not in _request.POST and '_save' not in _request.POST):
            if selected:
                response = _self.response_action(_request, queryset=cl.get_queryset(_request))
                if response:
                    return response
                else:
                    action_failed = True

        if action_failed:
            return None

        # If we're allowing changelist editing, we need to construct a formset
        # for the changelist given all the fields to be edited. Then we'll
        # use the formset to validate/process POSTed data.
        formset = cl.formset = None

        # Handle POSTed bulk-edit data.
        if _request.method == 'POST' and cl.list_editable and '_save' in _request.POST:
            if not _self.has_change_permission(_request):
                raise PermissionDenied
            FormSet = _self.get_changelist_formset(_request)
            modified_objects = _self._get_list_editable_queryset(_request, FormSet.get_default_prefix())
            formset = cl.formset = FormSet(_request.POST, _request.FILES, queryset=modified_objects)
            if formset.is_valid():
                changecount = 0
                for form in formset.forms:
                    if form.has_changed():
                        obj = _self.save_form(_request, form, change=True)
                        _self.save_model(_request, obj, form, change=True)
                        _self.save_related(_request, form, formsets=[], change=True)
                        change_msg = _self.construct_change_message(_request, form, None)
                        _self.log_change(_request, obj, change_msg)
                        changecount += 1

                if changecount:
                    msg = ngettext(
                        "%(count)s %(name)s was changed successfully.",
                        "%(count)s %(name)s were changed successfully.",
                        changecount
                    ) % {
                        'count': changecount,
                        'name': model_ngettext(opts, changecount),
                    }
                    _self.message_user(_request, msg, messages.SUCCESS)

                # return HttpResponseRedirect(_request.get_full_path())

        # Handle GET -- construct a formset for display.
        elif cl.list_editable and _self.has_change_permission(_request):
            FormSet = _self.get_changelist_formset(_request)
            formset = cl.formset = FormSet(queryset=cl.result_list)

        # Build the list of media to be used by the formset.
        if formset:
            media = _self.media + formset.media
        else:
            media = _self.media

        # Build the action form and populate it with available actions.
        if actions:
            action_form = _self.action_form(auto_id=None)
            action_form.fields['action'].choices = _self.get_action_choices(_request)
            media += action_form.media
        else:
            action_form = None

        selection_note_all = ngettext(
            '%(total_count)s selected',
            'All %(total_count)s selected',
            cl.result_count
        )

        context = {
            **_self.admin_site.each_context(_request),
            'module_name': str(opts.verbose_name_plural),
            'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
            'selection_note_all': selection_note_all % {'total_count': cl.result_count},
            'title': cl.title,
            'subtitle': None,
            'is_popup': cl.is_popup,
            'to_field': cl.to_field,
            'cl': cl,
            'media': media,
            'has_add_permission': _self.has_add_permission(_request),
            'opts': cl.opts,
            'action_form': action_form,
            'actions_on_top': _self.actions_on_top,
            'actions_on_bottom': _self.actions_on_bottom,
            'actions_selection_counter': _self.actions_selection_counter,
            'preserved_filters': _self.get_preserved_filters(_request),
            **(extra_context or {}),
        }

        _request.current_app = _self.admin_site.name

        return context