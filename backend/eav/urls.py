from django.urls import path
from . import views


app_name = 'eav'

urlpatterns = [
    path('attr/attr-by-entity/<str:app_model>', views.getAttrByEntity, name='attr-by-entity'),
    # path('attr/delete-attr/<int:id>', views.delete_attribute, name='delete-attribute'),
    path('attr/actions-attr', views.AttributeView.as_view(), name='actions-attr'),
]