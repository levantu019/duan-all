from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    # statistic
    path('statistic/init-comp', views.StatisticInitComponents, name='statistic_init_components'),
    path('statistic/<str:app>/<str:model>/<str:type>', views.DataStatistic, name="data_statistic"),
    
    # confirm
    path('notify-input/detail/<str:app_model>/<str:model_name>/<str:id>', views.NotifyDetail, name='notify_detail'),
    path('notify-input/update/<str:app_model>/<str:model_name>/<str:id>/<str:detail>', views.NotifyUpdate, name='notify_update'),

]
