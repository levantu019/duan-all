from django.urls import path
from . import views

app_name = 'nendialy'

urlpatterns = [
    path('import-data', views.ImportFileDataView.as_view(), name='import-data'),
]
