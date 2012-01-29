from django.http import Http404
from django.views.generic.list_detail import object_list
from django.views.generic.create_update \
     import create_object, update_object, delete_object
from django.db.models import get_model

def lista(request, model):
    model_object = get_model('meals', model)
    if model_object:
        model_list = model_object.objects.all()
    else:
        raise Http404()

    return object_list(request, queryset=model_list)

def adiciona_ou_atualiza(request, model, key=None):
    model_object = get_model('meals', model)
    if model_object:
        if key:
            return update_object(
                request,
                model=model_object,
                object_id=key,
                post_save_redirect='/meals/lista/%s/' % model,
            )
        else:
            return create_object(
                request,
                model=model_object,
                post_save_redirect='/meals/lista/%s/' % model,
            )
    else:
        raise Http404()

def remove(request, model, key):
    model_object = get_model('meals', model)
    if model_object:
        return delete_object(
             request,
             model=model_object,
             object_id=key,
             post_delete_redirect='/meals/lista/%s/' % model,
             template_name='object_confirm_delete.html',
         )
    else:
        raise Http404()
